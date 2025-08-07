
# explorer.py

"""
Module for analyzing and comparing scientific publications using LLMs and LangGraph.
"""

from pathlib import Path
from typing import Optional, TypedDict
import os

from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langgraph.graph import StateGraph, END
from langchain_core.messages import SystemMessage
from langchain_community.tools.tavily_search.tool import TavilySearchResults

from guardrails import Guard
from paths import SRC_DIR

import json
from datetime import datetime

#OUTPUT_DIR = Path("outputs")
#OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

PROFILES_DIR = Path("outputs/profiles")
PROFILES_DIR.mkdir(parents=True, exist_ok=True)
COMPARISONS_DIR = Path("outputs/comparisons")
COMPARISONS_DIR.mkdir(parents=True, exist_ok=True)

LOGS_DIR = Path("logs")
LOGS_DIR.mkdir(parents=True, exist_ok=True)


# from paths import SRC_DIR, OUTPUT_DIR

from logger import logger  # ✅ Logging enabled


MAX_CHARS = 12000

class AgentState(TypedDict):
    pub1_path: str
    pub2_path: str
    user_query: str
    pub1_profile: Optional[str]
    pub2_profile: Optional[str]
    comparison: Optional[str]
    trends: Optional[str]
    summary: Optional[str]
    fact_check: Optional[str]
    extra_info: Optional[str]
    lnode: Optional[str]
    count: int

def save_validated_profile(profile: dict, name: str) -> str:
    """
    Save a validated Guardrails profile to a JSON file.

    Args:
        profile (dict): The validated output.
        name (str): Either 'pub1' or 'pub2'.

    Returns:
        str: Path to saved file.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    #file_path = OUTPUT_DIR / f"validated_profile_{name}_{timestamp}.json"
    file_path = PROFILES_DIR / f"validated_profile_{name}_{timestamp}.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(profile, f, indent=2)
    #print(f"✅ Saved validated profile to {file_path}")
    logger.info(f"✅ Saved validated profile to {file_path}")
    return str(file_path)


# Dummy tools for demonstration
class KeywordTagExtractor:
    def run(self, text: str) -> str:
        return "Keywords: NLP, HuggingFace, Evaluation Metrics"


class RAGRetriever:
    def run(self, query: str) -> str:
        return f"Retrieved info for query: {query}"


class PublicationExplorer:
    """
    Main orchestration class for analyzing and comparing two scientific publications.
    """

    def __init__(self):
        self.model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

        # Load guardrails schema
        rail_path = SRC_DIR / "rails" / "profile_extraction.rail"
        self.guard = Guard.from_rail(str(rail_path))

        # Prompts
        
        self.PROFILE_PROMPT = (
            "You are an expert scientific reviewer.\n\n"
            "Extract the following attributes from the publication and return them in **valid JSON format** using these keys:\n"
            "- `tools`: tools and libraries used\n"
            "- `evaluation_methods`: evaluation strategies or metrics\n"
            "- `datasets`: datasets used in the publication\n"
            "- `task_types`: NLP or ML tasks addressed (e.g., text classification, question answering)\n"
            "- `results`: any quantitative or qualitative findings\n\n"
            "Format your response **exactly like this**:\n"
            "{\n"
            '  "tools": ["..."],\n'
            '  "evaluation_methods": ["..."],\n'
            '  "datasets": ["..."],\n'
            '  "task_types": ["..."],\n'
            '  "results": ["..."]\n'
            "}\n\n"
            "Publication:\n{text}"
)

        self.COMPARE_PROMPT = (
            "Compare the two research publications based on:\n"
            "- Tool usage\n- Evaluation methods\n- Task types\n- Datasets\n- Results\n\n"
            "Include similarities, key differences, and contradictions. Query: '{query}'.\n\n"
            "Publication 1 Attributes:\n{pub1_profile}\n\n"
            "Publication 2 Attributes:\n{pub2_profile}"
        )

        self.TREND_PROMPT = (
            "Analyze trends based on the following attributes related to the query: '{query}'.\n\n"
            "**Publication 1:**\n{pub1_profile}\n\n**Publication 2:**\n{pub2_profile}"
        )

        self.SUMMARY_PROMPT = (
            "Summarize the findings from the comparison and trend analysis below.\n\n"
            "**Comparison:**\n{comparison}\n\n**Trends:**\n{trends}"
        )

        self.FACTCHECK_PROMPT = (
            "Fact-check the summary and trends using original publications.\n"
            "Return a list of supported/unsupported claims.\n\n"
            "Comparison:\n{comparison}\n\nTrends:\n{trends}\n\nSummary:\n{summary}\n\n"
            "Publication 1:\n{pub1_text}\n\nPublication 2:\n{pub2_text}"
        )

        self.react_agent = initialize_agent(
            tools=[
                Tool("KeywordTagExtractor", KeywordTagExtractor().run, "Extract keywords."),
                Tool("RAGRetriever", RAGRetriever().run, "Retrieve factual info."),
                Tool("WebSearch", TavilySearchResults().run, "Search web content.")
            ],
            llm=self.model,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=False,
            handle_parsing_errors=True  # ✅ enable fallback for malformed outputs
        )

        self.graph = self._build_graph()

    def _build_graph(self):
        builder = StateGraph(AgentState)
        builder.add_node("analyze_pub1", self.analyze_pub1)
        builder.add_node("analyze_pub2", self.analyze_pub2)
        builder.add_node("compare", self.compare)
        builder.add_node("aggregate_trends", self.aggregate_trends)
        builder.add_node("summarize", self.summarize)
        builder.add_node("fact_check_node", self.fact_check)
        builder.add_node("react_agent_tool", self.react_agent_tool)

        builder.set_entry_point("analyze_pub1")
        builder.add_edge("analyze_pub1", "analyze_pub2")
        builder.add_edge("analyze_pub2", "compare")
        builder.add_edge("compare", "aggregate_trends")
        builder.add_edge("aggregate_trends", "summarize")
        builder.add_edge("summarize", "fact_check_node")
        builder.add_edge("fact_check_node", "react_agent_tool")
        builder.add_edge("react_agent_tool", END)

        return builder.compile()

    def read_txt(self, path: str) -> str:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()[:MAX_CHARS]
        
    def validate_profile(self, raw: str, pub_name: str) -> dict:
        result = self.guard.parse(llm_output=raw)
        validated = result.validated_output or raw

        logger.info(f"[{pub_name.upper()}] Raw: {raw}")
        logger.info(f"[{pub_name.upper()}] Validated: {validated}")

        if isinstance(validated, dict):
            save_validated_profile(validated, pub_name)
        return validated   

    def analyze_pub1(self, state: AgentState) -> AgentState:
        text = self.read_txt(state["pub1_path"])
        prompt = self.PROFILE_PROMPT.replace("{text}", text)
        raw = self.model.invoke([SystemMessage(content=prompt)]).content

        # Validate with Guardrails
        #result = self.guard.parse(llm_output=raw)
        #validated = result.validated_output or raw
        validated = self.validate_profile(raw, "pub1")
        return {**state, "pub1_profile": validated, "lnode": "analyze_pub1", "count": state["count"] + 1}


        # Save validated profile
        #if isinstance(validated, dict):
            #save_validated_profile(validated, "pub1")

        # 🚨 Debug prints
        #print("\n[Raw Model Output]\n", raw)
        #print("\n[Guardrails Validated Output]\n", validated)
        #print("\n[Validation Result Object]\n", result)
        #print("\n[Available Attributes on Result]\n", dir(result))

        #return {**state, "pub1_profile": validated, "lnode": "analyze_pub1", "count": state["count"] + 1}


    def analyze_pub2(self, state: AgentState) -> AgentState:
        text = self.read_txt(state["pub2_path"])
        prompt = self.PROFILE_PROMPT.replace("{text}", text)
        raw = self.model.invoke([SystemMessage(content=prompt)]).content
        validated = self.validate_profile(raw, "pub2")
        # Validate with Guardrails
        #result = self.guard.parse(llm_output=raw)
        #validated = result.validated_output or raw
        # Save validated profile
        #if isinstance(validated, dict):
        #    save_validated_profile(validated, "pub2")

        # 🚨 Debug prints
        #print("\n[Raw Model Output]\n", raw)
        #print("\n[Guardrails Validated Output]\n", validated)
        #print("\n[Validation Result Object]\n", result)
        #print("\n[Available Attributes on Result]\n", dir(result))

        return {**state, "pub2_profile": validated, "lnode": "analyze_pub2", "count": state["count"] + 1}

    def compare(self, state: AgentState) -> AgentState:
        prompt = self.COMPARE_PROMPT.format(
            query=state["user_query"],
            pub1_profile=state["pub1_profile"],
            pub2_profile=state["pub2_profile"]
        )
        response = self.model.invoke([SystemMessage(content=prompt)])
        logger.info("📊 Comparison complete")
        return {**state, "comparison": response.content, "lnode": "compare", "count": state["count"] + 1}

    def aggregate_trends(self, state: AgentState) -> AgentState:
        prompt = self.TREND_PROMPT.format(
            query=state["user_query"],
            pub1_profile=state["pub1_profile"],
            pub2_profile=state["pub2_profile"]
        )
        response = self.model.invoke([SystemMessage(content=prompt)])
        logger.info("📈 Trend aggregation complete")
        return {**state, "trends": response.content, "lnode": "aggregate_trends", "count": state["count"] + 1}

    def summarize(self, state: AgentState) -> AgentState:
        prompt = self.SUMMARY_PROMPT.format(
            comparison=state["comparison"],
            trends=state["trends"]
        )
        response = self.model.invoke([SystemMessage(content=prompt)])
        logger.info("📝 Summary generated")
        return {**state, "summary": response.content, "lnode": "summarize", "count": state["count"] + 1}

    def fact_check(self, state: AgentState) -> AgentState:
        pub1 = self.read_txt(state["pub1_path"])
        pub2 = self.read_txt(state["pub2_path"])
        prompt = self.FACTCHECK_PROMPT.format(
            comparison=state["comparison"],
            trends=state["trends"],
            summary=state["summary"],
            pub1_text=pub1,
            pub2_text=pub2
        )
        response = self.model.invoke([SystemMessage(content=prompt)])
        logger.info("🔍 Fact-check complete")
        return {**state, "fact_check": response.content, "lnode": "fact_check", "count": state["count"] + 1}

    def react_agent_tool(self, state: AgentState) -> AgentState:
        pub1 = self.read_txt(state["pub1_path"])
        pub2 = self.read_txt(state["pub2_path"])
        query = f"Enrich or validate missing insights for query: {state['user_query']}"
        context = f"Publication 1:\n{pub1[:3000]}\n\nPublication 2:\n{pub2[:3000]}"
        response = self.react_agent.run(f"{query}\n\n{context}")
        logger.info("🤖 Agent completed enrichment step")
        return {**state, "extra_info": response, "lnode": "react_agent_tool", "count": state["count"] + 1}
