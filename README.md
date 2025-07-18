# Agentic AI Developer Certification: Productionizing LangGraph-Orchestrated Research Assistant for Ready Tensor

This repository is part of the **Agentic AI Developer Certification program** by [Ready Tensor](https://www.readytensor.ai)
and it is linked to both the publications:**Productionizing Agentic AI Developer Certification: LangGraph-Orchestrated Research Assistant for Ready Tensor** and **Agentic AI Developer Certification: LangGraph-Orchestrated Research Assistant for Ready Tensor** on [Ready Tensor](https://www.readytensor.ai).


## Project Description  
To productionize the multi-agent system created in **Agentic AI Developer Certification: LangGraph-Orchestrated Research Assistant for Ready Tensor** by 
adding robustness, safety, and deployment features through the use of `Guardrails`, `Observability`, `Deployment`, 
`Documentation`. This project reflects the full lifecycle of agentic AI development—from ideation to deployment. 

## Features  
The following additions have been enclosed in the project2:   
• **Guardrails**: Input/output validation, prompt protection, or structured response constraints.   
• **Observability**: Basic logging, user feedback capture, or instrumentation (e.g., using 
LangSmith or custom logs).   
• **Deployment**: Lightweight deployment via (FastAPI, Gradio, or) Streamlit; Hosted locally or on 
a cloud service (Render, Hugging Face, etc.).   
• **Documentation**: Clearly stated limitations and assumptions; Usage guide or demo 
walkthrough; Safety and monitoring considerations.  

_Summary of Additions_

|Area                            | Tools / Practices                                       |
|--------------------------------|---------------------------------------------------------|
| Guardrails                     | Input validat, LangChain parsers, file checks           | to be checked Guardrais.ai vs guardrais.py
| Observability                 | Python logging, node tracing, monitoring                 |
| Deployment                     | Streamlit Cloud, Docker, or CLI runner                  |
| Documentation                  | README, screenshots, docstrings, diagram                |


## Productionize the multi-agent system   

### [Guardrails](https://hub.guardrailsai.com/)  

_Summary Comparison_ 

|Feature                   | Without Guardrails-AI                                                               |With Guardrails-AI
|--------------------------|-------------------------------------------------------------------------------------|----------------
|Output format             |   Free-form text / Raw LLM output (possibly unstructured, noisy)                    | Strict, schema-validated JSON / Structured, validated, and optionally corrected   
|Input flexibility         |   High                                                                              |Moderate (requires `.rail` or schema)
|Retry on invalid format   |   No                                                                                | Yes
|Production-safety         |   Risk of LLM drift                                                                 | Robust
|Dev speed                 |   Quick                                                                             | Requires setup effort

The use of `guardrails-ai` (LLM Output Schema Validator): 
- Enforces that LLM output matches a structured format  
- Uses `.rail` (or Pydantic-like schemas() to validate:  
  - JSON structure  
  - Fields are non-empty    
  - Strings follow a regex pattern    
- Can regenerate LLM responses until they conform

_Step-by-Step Integration Plan (task)_    
 1 Install `guardrails-ai`      
 2 Create a `.rail` schema for publications (rails/profile_extraction.rail) including as fields tools, evaluation methods, datasets, tasks tyoes, results (still to be enclosed Other(queries))      
 3 Update PublicationExplorer.analyze_pub1() & .analyze_pub2() to use Guard  (src/explorer.py)  
 4 Validate the output before updating state    

The system will now validate outputs that contain:    
- **tools** : Lists the software frameworks or libraries explicitly extracted from the publication.      
- **evaluation_methods**: Captures the performance metrics or evaluation strategies described.           
- **datasets** : Reflects benchmark datasets used in the study for training/evaluation.          
- **task_types** : Lists the types of tasks addressed in the paper.      
- **results** : Captures key findings and performance outcomes.   

Each of these lists must be present in the model output for it to pass validation.  
This JSON is structured, machine-readable, and validated, so you can confidently pass it to downstream analytics or use it in reproducibility workflows. 
 

### Observability	Python logging, node tracing, monitoring  
TO BE ENCLOSED   

### Deployment	Streamlit Cloud, Docker, or CLI runner  
TO BE ENCLOSED  

### Documentation	README, screenshots, docstrings, diagram  
TO BE ENCLOSED


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
1. **Clone the repo** and be sure you're on the `main` branch:

   ```
   bash
   git clone https://github.com/micag2025/Agentic_AI_Developer_Certification_Project3
   cd Agentic_AI_Developer_Certification_Project3  
   ```
2. **Install dependencies**   
   Install runtime dependencies (`requirements.txt`) (preferably in a virtual environment):

   ```
   bash
   pip install -r requirements.txt
   ```
   > _Note_ Test dependencies are keeping separated from runtime dependencies (`requirements.txt`) since production systems don't need the test tools. Therefore, by using a `requirements-test.txt` , it is more clear what is needed during development and testing.     

   The `requirements-test.txt` file contains a list of packages needed for testing. You can install this with:  
   ```
   bash  
   pip install -r requirements-test.txt  
   ```

3. **Create and activate a virtual environment (recommended):**            
    ```
    bash
   python3 -m venv .venv
   source .venv/bin/activate       # Linux / macOS
   .\.venv\Scripts\activate      # Windows
   ```
3. **Set up environment variables**  
   Enclose your OpenAI API key and TAVILY API key  to a `.env` file in your the project root:

   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   TAVILY_API_KEY= your_tavily_api_key_here
 
   ```
## Running the Application  
1. **Prepare data**    
   Ensure `project_1_publications.json` is present in the data/ directory (or your configured DATA_DIR).
      > _Note:_ The `sample dataset` is available in the "Datasets" section of the related publication.

3. **Launch the App**     
   Run [Streamlit](https://docs.streamlit.io/) from the project root:  
    
   ```      
   bash    
   streamlit run src/app.py    
   ```    
   
4. **Access the Interface**          
   Open your browser to the local Streamlit URL (usually http://localhost:8501).        

You can now interact with the LangGraph-Orchestrated Research Assistant for Ready Tensor!  


## Running the Application  
To debug `Guardrails` within the full app flow (realistic testing) (to test Guardrails in production context):    

- Run the full Streamlit application:  
  ```    
   bash  
   streamlit run src/app.py  
  ```  
This will:  
- Trigger the PublicationExplorer pipeline
- Automatically invoke analyze_pub1 and analyze_pub2  
- Print the raw vs. validated outputs in the terminal (because of the print() statements)

## Usage Examples   
### Example validated profile guardrails-ai
The outputs can be found in the directory layout outputs/ 

- Selection `Usage Tool` for publ _Core concepts of Agentic AI and AI agents.txt_ 
  - Generated a raw LLM output like:  

  ```
 json   
 { 
  "tools": ["LangGraph", "Microsoft AutoGen"],  
  "evaluation_methods": [],  
  "datasets": []  
 }
```  
 - Guardrails validated it using the .rail schema.    
 - The output matched the expected format, even if some fields (like evaluation_methods) were empty — which is allowed.    


- Selection `Evaluation Methods` for publ _Core concepts of Agentic AI and AI agents.txt_ 

``` 
json 
TO BE ENCLOSED 
```

- Selection `Datasets` for publ _Core concepts of Agentic AI and AI agents.txt_ 

``` 
json 
TO BE ENCLOSED 
```

- Selection `Tasks Types` for publ _Core concepts of Agentic AI and AI agents.txt_ 

``` 
json 
TO BE ENCLOSED 
```

- Selection `Results` for publ _Core concepts of Agentic AI and AI agents.txt_ 

``` 
json 
TO BE ENCLOSED 
```

- Selection `Other(custom)` for publ _Core concepts of Agentic AI and AI agents.txt_ 

`` 
json 
TO BE ENCLOSED 
```


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

