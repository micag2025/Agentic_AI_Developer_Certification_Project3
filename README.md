# Agentic AI Developer Certification: Production LangGraph-Orchestrated Research Assistant for Ready Tensor

This repository is part of the **Agentic AI Developer Certification program** by [Ready Tensor](https://www.readytensor.ai) and it is linked to the publication **Agentic AI Developer Certification: Productionizing LangGraph-Orchestrated Research Assistant for Ready Tensor**.  


## Project Description  

This project builds upon the multi-agent system (prototype) described in the publication [Agentic AI Developer Certification: LangGraph-Orchestrated Research Assistant for Ready Tensor](https://app.readytensor.ai/publications/agentic-ai-developer-certification-langgraph-orchestrated-research-assistant-for-ready-tensor-IQBETLgAsJ9X). The objective is to advance this prototype to a fully production-ready, robust, and user-friendly agentic AI system. This involves enhancing it with:  

- **Guardrails:**  Input/output validation, prompt protection, and structured response constraints.
- **Observability:**  Logging, feedback capture, and instrumentation.
- **Deployment:** Streamlit-based app, Docker support, and cloud hosting options. An interactive web interface is provided using Streamlit.
- **Documentation:** Limitations, usage guides, walkthroughs, and safety considerations.
This repository demonstrates how to take a multi-agent system from ideation to production, focusing on robustness, safety, and deployment best practices.  


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

Observability is crucial for monitoring, tracing, and debugging the application during (real-world) deployment. Logging and monitoring use Python’s logging module and node tracing. Below is a complete solution that integrates logging and execution tracing to provide observability across the LangGraph-Orchestrated Research Assistant for Ready Tensor system.

#### Key Observability Features  

| Feature         | Tool/Technique                       | Purpose                                  |
| --------------- | ------------------------------------ | ---------------------------------------- |
| Structured Logs | Python’s `logging` + JSON formatting | Centralized log collection + readability |
| Tracing         | `uuid` session ID + node info        | Track LLM invocation paths & failures    |

#### Implementation Steps   
1. Install Logging Tools.      
2. Create `logger.py`.    

#### Enhancements Include:  
- Structured logging using loguru  
- Session traceability via uuid  
- Centralized logs to console and file  
- Logging across all major graph nodes    


### Deployment  

The application runs locally via Streamlit, or can be deployed to cloud platforms such as Streamlit Cloud, Docker, or Hugging Face Spaces. See `deployment.md` for deployment instructions.

Deployment setup considerations:  
- Ensure relevant folders exist (e.g., outputs/profiles/, logs/)  
- Set file permissions or volume mappings for Docker/cloud  
- Set environment variables as needed for UI behavior    


### Documentation  

Comprehensive documentation is provided, including:  
- Clear usage instructions (e.g.: Layout changes and new user interactions(e.g. sidebars, success messages),New UI features or components (e.g. download buttons, explanation sections)),  
- Annotated UI screenshots (Screenshots of the Streamlit interface),
- Code docstrings, ?? 
- Architecture diagrams (Architectural diagrams (Mermaid, Graphviz), 
- Deployment guidance,
- and details on system features and user interactions to support both developers and end users (e.g.: New UI features (e.g., download buttons, explanation sections), User-facing messages (e.g., file save locations/ where files are saved))  


### How the Multi-Agent Workflow Was Improved

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
 > _Note_ Before refers to the workflow in the original publication.  
 
## Repository Structure  

```text
/Agentic_AI_Developer_Certification_Project3-main
├── LICENSE
├── README.md                  # Project overview and instructions
├── deployment.md              # Deployment guide for various environments
├── Dokerfile                  # Instructions for building a Docker image
├── requirements-test.txt      # Development and test dependencies
├── requirements.txt           # Project dependencies 
├── .gitignore        	       # Ignored files and folders
├── .env.example        	     # Example environment file for API keys
├── data/
│   ├── project_1_publications.json  # Sample Ready Tensor dataset
│   ├── sample_publications/         # Input publication `.txt` files
│   │   ├── <publication1 .txt>      #     ↳ Each text file represents a single publication 
│   │   ├── <publication2 .txt> 
├── docs/
│   ├── Untitled diagram _ Mermaid Chart-2025-07-09-115351.png   # output Mermaid diagram (flowchart) in png
│   ├── langgraph_flowchart.mmd                                  #  output file Mermaid diagram (flowchart)
│   ├── publication_flowchart.png                                #  output image file Graphiz
├── examples_screens/
│   ├── <screenshot .jpeg>          # Streamlit interface screenshots
├── logs/                           # Runtime log output 
│   └── pipeline.log
├── outputs/                       # Validated profiles and comparison results
│   ├── profiles/        
│   │   └── validated_profile_pub1_*.json
│   └── comparisons/      
│       ├── comparison_pub1_vs_pub2_*.json
│       └── comparison_pub1_vs_pub2_*.html
├── src/                                # Source code
│   ├── app.py                          # Main Streamlit App
│   ├── explorer.py                     # LLM-based publication comparison engine
│   ├── generate_flowchart_graphviz.py  
│   ├── generate_flowchart_mermaid.py   
│   ├── loader.py                       # Converts JSON into individual .txt files
│   ├── paths.py                        # Centralized path definitions
│   ├── utils.py                        # Helper functions for path and string handling
│   ├── logger.py                       # Centralized log configuration used in the Observability
│   ├── docs/
│   │   ├── langgraph_flowchart.mmd
│   │   ├── publication_flowchart.png
│   ├── rails/                          # Guardrails XML schemas
│   │   ├── profile_extraction.rail     # Guardrails .rail schema schema used in the Guardrails
```


## Prerequisites
- Python 3.10+  
- [Openai API key](https://platform.openai.com/account/api-keys)  
- [Tavily API key](https://www.tavily.com/)  
 (set as OPENAI_API_KEY and TAVILY_API_KEY environment variables)    


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
   > _Note_ Test dependencies are separated from runtime dependencies.   
  
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
   ```
          
3. Open your browser to the local Streamlit URL (usually http://localhost:8501).        

You can now interact with the LangGraph-Orchestrated Research Assistant for Ready Tensor!  

**Output Locations**  
  - 📂 Validated Profiles: `outputs/profiles/*.json`  
  - 📂 Comparison Reports: `outputs/comparison/*.json and .html`    
  - 📁 Log Files: `logs/*.log`    
You can download the latest validated profile and log file directly from the Streamlit interface.

**Debugging Guardrails Integration**:  
Run the app and monitor the terminal for raw vs. validated outputs. The pipeline will:  
- Trigger the PublicationExplorer  
- Invoke analyze_pub1 and analyze_pub2  
- Print both raw and validated outputs in the terminal  

## Usage Examples  
### Example: Validated Profile (Guardrails-AI)
Sample output in `outputs/`:

```json
{
  "tools": ["LangGraph", "Microsoft AutoGen"],
  "evaluation_methods": [],
  "datasets": [],
  "task_types": ["AI Agent", "Autonomous Agents", "Multi-Agent System"],
  "results": []
}
```
If `evaluation_methods` is empty, it means the publication lacks evaluation details or the model did not extract any.  
Guardrails validated the output using the `.rail schema`. The output matched the expected format, even if some fields were empty.

### Example: Observability (Logging, Tracing, Monitoring)     
Logs can be found in `/logs`  

Your (The) system now logs like a production-grade application:  

- **Structured**: Function, line, module, process, thread, etc.  
- **Informative**: Timestamps, clean tagging (📊, 📈, 📝, 🔍, 🤖)
- **Validated Output vs Raw**: Captures both model responses and validated subset.  

### Example: Deployment (Streamlit Cloud, Docker, CLI)
**Streamlit Deployment Notes**  

- Ensure outputs/profiles/, outputs/comparison/, and logs/ directories exist and are writable.  
- Validated profiles and logs are downloadable via the UI.  
- For Docker, map local volumes as needed.  

### Streamlit App Example  
Launch the UI
```
streamlit run src/app.py
```
**Screenshots:**

📘 Initial Streamlit interface
![examples_screens/1_Screenshot_improved_initial_StreamLit_interface.jpeg](examples_screens/1_Screenshot_improved_initial_StreamLit_interface.jpeg)

🔍Side-by-side comparison: 
![examples_screens/2_Screenshot_improved_Streamlit_example_usage1.jpeg](examples_screens/2_Screenshot_improved_Streamlit_example_usage1.jpeg)

📁 Output summary in UI:
![examples_screens/5_Screenshot_improved_message_results_saved_example_usage1.jpeg](examples_screens/5_Screenshot_improved_message_results_saved_example_usage1.jpeg)  

**Key UI Features:**  

1. **Clear Location Indicators**:    
    - Where comparison results, validated profiles, and logs are saved.  
2. **Download Buttons:**
    - Download the latest validated profile, comparison JSON, or log file.
3. **Introductory Information:**    
    - The sidebar provides clear information about storage and outputs.
4. **About this App:**  
    - The sidebar includes a clean section outlining the technologies used. Sensitive API keys are never exposed.


### Example: Documentation (README, Screenshots, Docstrings, Diagrams)
**Streamlit Interface Enhancements:**  

- Sidebar section “About this App” to explain key technologies.  
- Messages clarify where logs and profiles are saved.  
- File download buttons for recent outputs.  
- Improved layout for selecting publications and query types.  


### 📊 Technologies Used  
- [Streamlit](https://docs.streamlit.io/) – UI Framework      
- [LangChain](https://www.langchain.com/langgraph) – LLM Orchestration      
- [OpenAI](https://platform.openai.com/account/api-keys) – LLM backend        
- [Tavily](https://www.tavily.com/) – Web search API    
- [Guardrails](https://hub.guardrailsai.com/)  – Output validation      


### 🔒 Security  
- API keys are never exposed in the interface.    
- All results are stored locally in JSON/HTML format.  
- Logs provide full traceability of the extraction and comparison process.  


## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


## Contact Information 
If you encounter bugs, have questions, or would like to request a new feature, please [open an issue](https://github.com/micag2025/Agentic_AI_Developer_Certification_Project3/issues) on this repository.  Contributions and feedback are welcome!  

