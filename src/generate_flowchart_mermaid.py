# generate_langgraph_mermaid.py

"""
Generates a Mermaid flowchart of the LangGraph orchestration flow,
prints it to the console, and saves it to docs/langgraph_flowchart.mmd.
"""

import os
#from paths import DOCS_DIR
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(ROOT_DIR, "docs")
os.makedirs(DOCS_DIR, exist_ok=True)
from paths import SRC_DIR





# Mermaid node styles
NODE_STYLES = {
    "analyze_pub1": "#e0f7fa",
    "analyze_pub2": "#e0f7fa",
    "compare": "#fff9c4",
    "aggregate_trends": "#fff9c4",
    "summarize": "#dcedc8",
    "fact_check_node": "#f8bbd0",
    "react_agent_tool": "#d1c4e9"
}

# Flowchart edges
EDGES = [
    ("start", "analyze_pub1"),
    ("analyze_pub1", "analyze_pub2"),
    ("analyze_pub2", "compare"),
    ("compare", "aggregate_trends"),
    ("aggregate_trends", "summarize"),
    ("summarize", "fact_check_node"),
    ("fact_check_node", "react_agent_tool"),
    ("react_agent_tool", "end_node"),
]

def generate_mermaid_code() -> str:
    """
    Builds the raw Mermaid flowchart syntax.
    Returns:
        str: Mermaid code block.
    """
    lines = ["flowchart TD"]
    
    for src, tgt in EDGES:
        lines.append(f"    {src} --> {tgt}")
    
    # Add labeled end node
    lines.append("    end_node[End]")

    # Style nodes
    for node, color in NODE_STYLES.items():
        lines.append(f"    style {node} fill:{color},stroke:#333,stroke-width:1px")

    return "\n".join(lines)

def save_to_file(content: str, filepath: str) -> None:
    """
    Saves Mermaid code to a .mmd file.

    Args:
        content (str): Mermaid code to save.
        filepath (str): Target path to save the file.
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Mermaid code saved to: {filepath}")

if __name__ == "__main__":
    mermaid_code = generate_mermaid_code()
    
    # Print to terminal
    print(mermaid_code)

    # Save to .mmd file in docs/
    output_path = os.path.join(DOCS_DIR, "langgraph_flowchart.mmd")
    save_to_file(mermaid_code, output_path)
