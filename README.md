# Agentic AI Developer Certification: Productionizing LangGraph-Orchestrated Research Assistant for Ready Tensor

This repository is part of the **Agentic AI Developer Certification program** by [Ready Tensor](https://www.readytensor.ai) and it is linked to the publication **Agentic AI Developer Certification: Productionizing LangGraph-Orchestrated Research Assistant for Ready Tensor**.


## Project Description

The multi-agent system (prototype) developed in the publication [Agentic AI Developer Certification: LangGraph-Orchestrated Research Assistant for Ready Tensor](https://app.readytensor.ai/publications/agentic-ai-developer-certification-langgraph-orchestrated-research-assistant-for-ready-tensor-IQBETLgAsJ9X)  allows users, such as Ready Tensor Users or Developers, to compare the content of two select scientific publications, side-by-side using natural language queries, LangChain, LangGraph, and OpenAI APIs.   
The objective of this project is to take this existing agentic AI system to the next level, making it ready for real-world use, thus transforming this into a tested, safe, user-ready, and portfolio-worthy production-ready AI application (that meets professional standards), (having enclosing) enhancing it for production use by integrating:
- **Guardrails:** Input/output validation, prompt protection, and structured response constraints.
- **Observability:** Logging, feedback capture, and instrumentation.
- **Deployment:** Streamlit-based app, Docker support, and cloud hosting options.(Create an intuitive, user-friendly web interface 
- **Documentation:** Limitations, usage guides, walkthroughs, and safety considerations.

This project demonstrates how to enhance a multi-agent system with robustness, safety, and deployment features, reflecting a full lifecycle from ideation to production. The repository demonstrates best practices for agentic AI development, from initial design to real-world deployment.


## Features

| Area          | Tools / Practices                                    |
|---------------|------------------------------------------------------|
| Guardrails    | Input validation, LangChain parsers, file checks, Guardrails-AI |
| Observability | Python logging, node tracing, monitoring             |
| Deployment    | Streamlit Cloud, Docker, CLI runner                  |
| Documentation | README, screenshots, docstrings, diagrams            |


## Productionize the multi-agent system   

### Guardrails

[Guardrails-AI](https://hub.guardrailsai.com/) is used to enforce structured, validated outputs from LLMs.

#### Comparison Without Guardrails-AI and With Guardrails-AI    

| Feature              | Without Guardrails-AI         | With Guardrails-AI                |
|----------------------|------------------------------|-----------------------------------|
| Output format        | Free-form, unstructured text  | Schema-validated JSON             |
| Input flexibility    | High                         | Moderate (requires schema)        |
| Retry on invalid     | No                           | Yes                               |
| Production-safety    | Risk of LLM drift            | Robust                            |
| Dev speed            | Fast                         | Requires setup effort             |

#### Integration Steps

1. Install `guardrails-ai`.
2. Create a `.rail` schema for publication profiling.
3. Update relevant analysis functions (e.g., `PublicationExplorer.analyze_pub1()`, `PublicationExplorer.analyze_pub2()`). / (src/explorer.py)      
4. Validate outputs before updating state.

**Validated output includes:**  
- `tools`: Frameworks/libraries extracted from publication  
- `evaluation_methods`: Metrics or strategies described  
- `datasets`: Benchmarks used  
- `task_types`: Types of tasks addressed  
- `results`: Key findings
- `user query`: DECIDE WHETHER THIS SHOULD BE ENCLOSED OR NOT

All fields must be present for validation. Structured, machine-readable JSON enables downstream analytics and reproducibility.


### Observability

Basic logging and monitoring are implemented via Python’s logging module and node tracing. Future enhancements will include integration with dedicated observability platforms (e.g., LangSmith). TO BE ENCLOSED  
To productionize the multi-agent system, Observability is a crucial pillar becasue it enables  to monitor, trace, and debug the application effectively during real-world deployment.

Observability in Multi-Agent Systems  
Below is a complete solution that integrates logging, metrics, and execution tracing to provide observability across the LangGraph-Orchestrated Research Assistant for Ready Tensor system.

#### Key Observability Features  


| Feature         | Tool/Technique                       | Purpose                                  |
| --------------- | ------------------------------------ | ---------------------------------------- |
| Structured Logs | Python’s `logging` + JSON formatting | Centralized log collection + readability |
| Metrics         | `prometheus_client` (optional)       | Export request counts, latency, etc.     |
| Tracing         | `uuid` session ID + node info        | Track LLM invocation paths & failures    |

#### Step-by-Step Implementation  
1. Install `Logging Tools`    
2. Create logger.py  

Enhancements to Include
- Structured logging using loguru  
- Session traceability using uuid  
- Centralized logs to both console and file  
- Logging across all major graph nodes  



### Deployment

The application can be run locally via Streamlit, or deployed to cloud platforms like Streamlit Cloud, Docker, or Hugging Face Spaces. TO BE ENCLOSED    

### Documentation (README, screenshots, docstrings, diagram) 

Comprehensive documentation is provided, including:
- Usage instructions
- Screenshots of the Streamlit interface
- Docstrings in code
- Architectural diagrams (Mermaid, Graphviz)

### 🔁 How the Multi-Agent Workflow Was Improved

| Feature              | Before                         | After                                  |
| -------------------  | -------------------------------| ---------------------------------------- |
| Guardrails           | ❌ None                        | ✅ Included .rail schema with fallback |
|Logging               | ⚠️ Basic	                     | ✅ Structured log with timestamps + directory  |
| Output Separation    | ❌ Mixed                       | ✅ outputs/profiles/, outputs/comparison/   |
|Validation            | ❌ Ad-hoc	                    | ✅ Schema-driven, strict validation |
| Resilience           |❌ Fragile                     | ✅ Robust with safe fallbacks and logs |
|Deployment            | ❌ Prototype	                | ✅ Docker + cloud ready|
| Interface            |⚠️ Raw API key in UI           | ✅ Clean sidebar info only |
| Documentation        |⚠️ Incomplete                  | ✅ README.md, deployment.md, code docstrings |

 
## Repository Structure  

```text
/Agentic_AI_Developer_Certification_Project3-main
├── LICENSE
├── README.md                  # Project overview and instructions
├── deployment.md                 # Project overview and instructions
├── requirements-test.txt      # List of packages needed for development and testing
├── requirements.txt           # Project dependencies / # Example environment file storing secret API keys
├── .gitignore        	       # This file specifies the files and folders that should be ignored by Git.
├── .env.example        	     # This file specifies the OPEN API keys required.
├── data/
│   ├── project_1_publications.json  # Sample Ready Tensor dataset
│   ├── sample_publications/         # Directory containing input publication `.txt` files
│   │   ├── <publication1 .txt>      #     ↳ Each text file represents a single publication 
│   │   ├── <publication2 .txt> 
│   │   ├──
├── docs/
│   ├── Untitled diagram _ Mermaid Chart-2025-07-09-115351.png   #  ↳output Mermaid diagram (flowchart) in png
│   ├── langgraph_flowchart.mmd     #  ↳ output file Mermaid diagram (flowchart)
│   ├── publication_flowchart.png   #  ↳ output image file Graphiz
├── examples_screens/
│   ├── <screenshot .jpeg>   # Section of screenshot of example usage of the StreamLit interface 
│   ├──
├── logs/                               # Runtime log output (excluded from Git)
│   └── pipeline.log
├── outputs/                            # Final validated profiles and comparisons
│   ├── profiles/         ← Validated profiles (from Guardrails)
│   │   └── validated_profile_pub1_*.json
│   └── comparisons/      ← Comparison results (HTML + JSON)
│       ├── comparison_pub1_vs_pub2_*.json
│       └── comparison_pub1_vs_pub2_*.html
├── src/                                # This directory holds the source code for the project. 
│   ├── app.py                          # Main Streamlit App
│   ├── explorer.py                     # LLM-based publication comparison engine
│   ├── generate_flowchart_graphviz.py  # Generates a Graphviz PNG diagram of the LangGraph orchestration flow
│   ├── generate_flowchart_mermaid.py   # Generates a Mermaid diagram of the LangGraph orchestration flow
│   ├── loader.py                       # Converts JSON into individual .txt files
│   ├── paths.py                        # Centralized path definitions / This file includes paths to files used in the project.
│   ├── utils.py                        # Helper functions for path and string handling
│   ├── logger.py                       # Centralized log configuration (to be used in the Observability)
│   ├── docs/
│   │   ├── langgraph_flowchart.mmd
│   │   ├── publication_flowchart.png
│   ├── rails/                          # Guardrails XML schemas
│   │   ├── profile_extraction.rail     # .rail schema for publication profiling  (to be used in the Guardrails)
```


## Prerequisites
* Python 3.10+
* An [Openai API](https://platform.openai.com/account/api-keys) key and a [Tavily API](https://www.tavily.com/) key (OPENAI_API_KEY and TAVILY_API_KEY environment variable) 


## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/micag2025/Agentic_AI_Developer_Certification_Project3
   cd Agentic_AI_Developer_Certification_Project3

2. **Install dependencies**
     ```bash
   pip install -r requirements.txt
   # For testing:
   pip install -r requirements-test.txt
     ```

   > _Note_ Test dependencies are keeping separated from runtime dependencies (`requirements.txt`) since production systems don't need the test tools. Therefore, by using a `requirements-test.txt` , it is more clear what is needed during development and testing. The `requirements-test.txt` file contains a list of packages needed for testing.
  
3. **Set up environment variables**  
  Copy `.env.example` to .env and add your OpenAI and Tavily API keys.

4. **(Recommended) Use a virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # Linux/macOS
   .\.venv\Scripts\activate    # Windows
  

### Running the Application

1. Ensure `project_1_publications.json` is present in `data/`.
  > _Note:_ The `sample dataset` is available in the "Datasets" section of the related publication.  
2. Launch the [Streamlit](https://docs.streamlit.io/) app:
   ```bash
   streamlit run src/app.py
          
3. Open your browser to the local Streamlit URL (usually http://localhost:8501).        

You can now interact with the LangGraph-Orchestrated Research Assistant for Ready Tensor!  


To debug `Guardrails` integration, run the app as above and monitor the terminal for raw vs. validated outputs.

This will:  
- Trigger the PublicationExplorer pipeline
- Automatically invoke analyze_pub1 and analyze_pub2  
- Print the raw vs. validated outputs in the terminal (because of the print() statements)


## Usage Examples   
### Example validated profile guardrails-ai
The outputs can be found in the directory layout outputs/ 

Sample validated by Guardrails output:
```json
{
  "tools": ["LangGraph", "Microsoft AutoGen"],
  "evaluation_methods": [],
  "datasets": [],
  "task_types": ["AI Agent", "Autonomous Agents", "Multi-Agent System"],
  "results": []
}
```
Explanation:
If evaluation_methods is empty, it indicates the publication lacks evaluation details or the model did not extract any.

Reasons may include:
No evaluation section in the text
LLM extraction limitations
Preprocessing/truncation
Schema-constrained validation
 - Guardrails validated it using the .rail schema.    
 - The output matched the expected format, even if some fields (like evaluation_methods) were empty — which is allowed.    


### Example Observability	Python logging, node tracing, monitoring      
The output can be foung in /logs 

The logs confirm that your full multi-agent system is running flawlessly with Guardrails + Observability in place. Here's a structured breakdown of what this means and next actions:

✅ Summary of Log Behavior
🔐 Guardrails Output (for both publications)
| Field               | Publication 1                       | Publication 2                            |
| ------------------ | ------------------------------------ | ---------------------------------------- |
| tools              | 	["LangGraph", "Microsoft AutoGen"]  |["PyTorch"]                               |
| evaluation_methods | ❌ Empty → filtered out              | ❌ Empty → filtered out                 |
| datasets           | ❌ Empty → filtered ou               | ❌ Empty → filtered out                 |
| task_types         | ✅ Present                           |✅ Present               |
| results            | ❌ Empty → filtered ou               | ❌ Empty → filtered out                 |

✅ Guardrails successfully removed empty fields from the final validated output, keeping your state clean and safe for downstream processing.

📂 Output Files Created
bash

outputs/
├── validated_profile_pub1_20250802_152830.json
├── validated_profile_pub2_20250802_152831.json
These contain the validated subset of the original profile—only populated fields.

📈 Graph Execution: All Nodes
analyze_pub1 → ✅  
analyze_pub2 → ✅  
compare → ✅  
aggregate_trends → ✅    
summarize → ✅  
fact_check → ✅  
react_agent_tool → ✅  

All are clearly logged and show no signs of error or exception.

🔍 Log Output Interpretation
You’re logging like a production-grade system:

✅ Structured  

- function, line, module, process, thread, etc.

✅ Informative  

- Timestamps  

- Clean tagging: 📊, 📈, 📝, 🔍, 🤖  

✅ Validated Output vs Raw  
You're capturing both Raw: model responses and the Validated: subset. 

### Example Deployment	Streamlit Cloud, Docker, or CLI runner  

### Streamlit App Example
🖥️ _Launch the UI_
```
streamlit run src/app.py
```
📘 _Example Updated Streamlit Interface User and   
![examples_screens/1_Screenshot_improved_initial_StreamLit_interface.jpeg](examples_screens/1_Screenshot_improved_initial_StreamLit_interface.jpeg)

🔍 _Example: Side-by-Side Comparison_  
![examples_screens/2_Screenshot_improved_Streamlit_example_usage1.jpeg](examples_screens/2_Screenshot_improved_Streamlit_example_usage1.jpeg)

📁 Example: Output Summary in the UI message  
![examples_screens/5_Screenshot_improved_message_results_saved_example_usage1.jpeg](examples_screens/5_Screenshot_improved_message_results_saved_example_usage1.jpeg)  

> _Note_ ✅ Changes Applied  
1. 📁 Clear Location Indicators in Sidebar:  
- Where comparison results are saved (outputs/comparisons/)  
- Where validated profiles are saved (outputs/profiles/)    
- Where logs are stored (logs/)  

2. ⬇️ Download Buttons:  
- Download the latest validated profile  
- Download the latest comparison JSON  
- Download the latest log file

Add `File Links` (`Download Buttons`) to let users download the latest validated profile or log file from the interface


Modified version of the app.py with clear messages in the Streamlit interface that:

✅ Inform users:  
📂 Where validated profiles are saved (JSON in outputs/)  
📁 Where logs are stored (in .log format in logs/)  

This version includes a section at the top of the sidebar with helpful information about storage:

all saved outputs (comparison JSON + HTML, validated profiles, and logs) in the UI message

add a kind of introductory information to enhance clarity and sets expectations for the user.  💡 Result in the Streamlit Interface:
This will appear as a well-structured paragraph with bullet points and horizontal divider (---), helping orient the user before they start interacting with the UI.  

update the `app.py` according to the requirement toReplace the sidebar display of API keys with an informative "About this App" section that outlines the stack being used (OpenAI, LangChain, Streamlit), and do not expose API keys or mask them.

revised and production-secure version, keeping all your current logic and modifying just the sidebar contentThese have now been removed. This is a best practice because:  
- Even partial API keys can be scraped or leaked  
- It serves no purpose for most end users

✅ the  app remains functional
Keys are still loaded via os.getenv() using .env  
The app logic (PublicationExplorer()) continues to use them under the hood  
Only the UI is hardened  

To modify your app.py so that it shows "About this App" instead of exposing sensitive API keys (OPENAI_API_KEY, TAVILY_API_KEY), you should:  
Hide or remove any Streamlit output of environment variables (like st.write(os.getenv("OPENAI_API_KEY"))).  
Add a clean "About this App" section with markdown to display the technologies used.  



### Example Documentation	README, screenshots, docstrings, diagram  
TO BE ENCLOSED    


## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


## Contact Information 
If you encounter bugs, have questions, or would like to request a new feature, please [open an issue](https://github.com/micag2025/Agentic_AI_Developer_Certification_Project3/issues) on this repository.  
Contributions and feedback are welcome!

