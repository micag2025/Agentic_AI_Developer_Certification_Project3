# Agentic AI Developer Certification: Productionizing LangGraph-Orchestrated Research Assistant for Ready Tensor

This repository is part of the **Agentic AI Developer Certification program** by [Ready Tensor](https://www.readytensor.ai).
It is based on the publications:
- **Agentic AI Developer Certification: Productionizing LangGraph-Orchestrated Research Assistant for Ready Tensor**
- **Agentic AI Developer Certification: LangGraph-Orchestrated Research Assistant for Ready Tensor** [Add full titles and links if available]

This project demonstrates how to enhance a multi-agent system with robustness, safety, and deployment features, reflecting a full lifecycle from ideation to production.


## Project Description

This project builds on the multi-agent system developed for Ready Tensor (enclose link), enhancing it for production use by integrating:
- **Guardrails:** Input/output validation, prompt protection, and structured response constraints.
- **Observability:** Logging, feedback capture, and instrumentation.
- **Deployment:** Streamlit-based app, Docker support, and cloud hosting options.
- **Documentation:** Limitations, usage guides, walkthroughs, and safety considerations.

The repository demonstrates best practices for agentic AI development, from initial design to real-world deployment.


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

### Deployment

The application can be run locally via Streamlit, or deployed to cloud platforms like Streamlit Cloud, Docker, or Hugging Face Spaces. TO BE ENCLOSED    

### Documentation (README, screenshots, docstrings, diagram) 

Comprehensive documentation is provided, including:
- Usage instructions
- Screenshots of the Streamlit interface
- Docstrings in code
- Architectural diagrams (Mermaid, Graphviz)

  
## Repository Structure  

```text
/Agentic_AI_Developer_Certification_Project3-main
├── LICENSE
├── README.md                  # Project overview and instructions
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
├── outputs/
│   ├── comparison_<pub1>_vs_<pub2>_<timestamp>.json  # Full Comparison Results (from Streamlit app)
│   ├── comparison_<pub1>_vs_<pub2>_<timestamp>.html  # Full Comparison Results (from Streamlit app)
│   ├── validated_profile_pub1_<timestamp>.json  # Validated Profiles (Guardrails-validated JSONs)
│   ├── validated_profile_pub2_<timestamp>.json  # Validated Profiles (Guardrails-validated JSONs)
│   ├──
├── src/                                # This directory holds the source code for the project. It is further divided into various subdirectories:
│   ├── app.py                          # Main Streamlit App
│   ├── explorer.py                     # LLM-based publication comparison engine
│   ├── generate_flowchart_graphviz.py  # Generates a Graphviz PNG diagram of the LangGraph orchestration flow
│   ├── generate_flowchart_mermaid.py   # Generates a Mermaid diagram of the LangGraph orchestration flow
│   ├── loader.py                       # Converts JSON into individual .txt files
│   ├── paths.py                        # Centralized path definitions / This file includes paths to files used in the project.
│   ├── utils.py                        # Helper functions for path and string handling
│   ├── docs/
│   │   ├── langgraph_flowchart.mmd
│   │   ├── publication_flowchart.png
│   ├── rails/
│   │   ├── profile_extraction.rail  # .rail schema for publication profiling  
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
  ```        
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

Sample validated output:
```json
{
  "tools": ["LangGraph", "Microsoft AutoGen"],
  "evaluation_methods": [],
  "datasets": [],
  "task_types": ["AI Agent", "Autonomous Agents", "Multi-Agent System"],
  "results": []
}

Explanation:
If evaluation_methods is empty, it indicates the publication lacks evaluation details or the model did not extract any.

Reasons may include:

No evaluation section in the text
LLM extraction limitations
Preprocessing/truncation
Schema-constrained validation
 - Guardrails validated it using the .rail schema.    
 - The output matched the expected format, even if some fields (like evaluation_methods) were empty — which is allowed.    


- Selection `Evaluation Methods` for publ _Core concepts of Agentic AI and AI agents.txt_ 




In the case, the output from the LLM (validated by Guardrails) is:

```
json
{ 
  "tools": ["LangGraph", "Microsoft AutoGen"],  
  "evaluation_methods": [],  
  "datasets": [],
  "task_types": ["AI Agent", "Autonomous Agents", "Multi-Agent System"],
  "results": []
}
```
If the user selected evaluation_methods, but the corresponding output is an empty list, here's the correct interpretation:

✅ Explanation
**"No evaluation methods were detected or extracted from the given publication content by the LLM."**

This can happen due to several reasons:

🔍 Why evaluation_methods Might Be Empty
**1 The publication content lacks evaluation details.**  
- It's possible the text provided doesn't include sections like “Evaluation”, “Metrics”, “Experiments”, etc.

**LLM extraction limitations.**

- The LLM might have overlooked subtle mentions of evaluation methods or misunderstood their presence due to vague or implicit phrasing.  

**Preprocessing (truncation).**  

- If the publication text was truncated (as you have MAX_CHARS = 12000), the evaluation section may have been cut off.  

**Schema-constrained validation (Guardrails).**  

- If the raw model output had malformed or invalid data under evaluation_methods, Guardrails would sanitize it and return an empty list (as per schema constraints).  

### Example Observability	Python logging, node tracing, monitoring      
TO BE ENCLOSED    

### Example Deployment	Streamlit Cloud, Docker, or CLI runner  
TO BE ENCLOSED    

### Example Documentation	README, screenshots, docstrings, diagram  
TO BE ENCLOSED    



## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


## Contact Information 
If you encounter bugs, have questions, or would like to request a new feature, please [open an issue](https://github.com/micag2025/Agentic_AI_Developer_Certification_Project3/issues) on this repository.  
Contributions and feedback are welcome!

