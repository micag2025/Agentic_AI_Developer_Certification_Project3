# Agentic AI Developer Certification: Productionizing LangGraph-Orchestrated Research Assistant for Ready Tensor

## TAGS: AAIDC, AAIDC-M3, Agentic AI, Multi-Agent Systems, AI Agents, Guardrails, Production Systems, Resilience, Security, Testing, UI, API Design, Deployment, Streamlit, Streamlit Cloud, LangChain, LangGraph (Agent), AI Orchestration, Pytest(?)

## Author : Michela Agostini, others? 

## Models : Github

## Dataset: project_1_publications.json

## TL;DR
Take your multi-agent system from Module 2 and transform it into a production-grade AI application — tested, safe, user-ready, and portfolio-worthy. This project is based on the multi-agent system built in Module 2: Build a Multi-Agent System. The objective is to take the Module 2 multi-agent prototype and transform it into a production-ready application that meets professional software standards. Thus, the objective of this project is to demonstrate the ability to prepare an agentic AI system for real-world use by enhancing it with the following capabilities:  
- Production Readiness: Transform your prototype into a robust, deployable system    
- Quality Assurance: Implement comprehensive testing strategies for multi-agent workflows    
- Security & Safety: Add guardrails, input validation, and safety mechanisms    
- User Experience: Create an intuitive, user-friendly interface    
- Operational Excellence: Integrate monitoring, logging, and resilience features    
= Documentation: Produce clear technical documentation for maintainability and handoff    

Make it ready for real-world use. Focus on stability, safety, and clarity. The goal is to make the existing system presented in Module2  robust, trustworthy, and easy to use. This is done applying the enhancements listed under the Required Components section — including testing, guardrails, resilience, and documentation — in the context of the specific project.

Required Components:

✅ _Comprehensive Testing Suite_ : Unit tests for individual agent functions and tools, Integration tests for agent-to-agent communication, End-to-end system tests for complete workflows, Test coverage of at least 70% for core functionality.  
✅ _Safety & Security Guardrails_: Input validation and sanitization, Output filtering and content safety measures, Error handling with graceful degradation, Logging for compliance and debugging  
✅ _User Interface_: Interactive web application using Gradio, Streamlit, or similar framework, Intuitive design that abstracts away technical complexity, Clear error messages and user guidance
✅ _Resilience & Monitoring_:Retry logic with exponential backoff for failed tool or LLM calls, Timeout handling to prevent long-running or stalled workflows, Basic loop limits or iteration caps to avoid infinite cycles, Graceful handling of agent failures and timeouts, Logging of failures, retries, and fallback events for debugging and traceability
> _Note_: just choose the ones most relevant to the system’s risks. The goal is to handle failure gracefully and avoid silent breakage.  

✅ _Professional Documentation_:High-level system overview including purpose, architecture, and key components, Deployment and configuration guide with setup, instructions (README, .env.sample, etc.), API or interface specifications and expected input/output formats (if applicable), Logging, health check, and maintenance considerations for long-term use, Troubleshooting guide and FAQ for common issues and recovery steps.  

Example: Publication Assistant for AI Projects 📘
If you built a multi-agent assistant that helps users improve their AI/ML project documentation, the objective of this project is to take it to the next level, having enclosing: 
- Add a clean web interface where users paste their documentation or upload a document and get suggestions in real time  
- Use clear visual cues for improvement areas (titles, tags, summaries, etc.)  
- Add basic input validation and guardrails to avoid unsafe responses  
- Handle errors gracefully for invalid or unsupported submissions  
- Include a basic deployment wrapper using Streamlit


## Tool Overview & Architecture
This project uses a sample dataset and is built around (is structured on) a modular LangChain-based pipeline.

Describes the production system architecture and key improvements
Documents the testing strategy and security implementations
Demonstrates the user interface and operational features


### Sample Dataset:
A collection of 35 Ready Tensor publications, each of them characterised by id, username, license, title, and publication description. There are 6 types of licenses; 27 publications use “MIT” or “CC”, the rest are “none” or missing. Under MIT/CC, reuse is permitted for open source projects.

### Features & Modules:
This project is structured on a modular LangChain-based pipeline in which each feature is mapped to the specific tool or module implementing it:


### Workflow: The LangChain-based pipeline is designed to:



## Features

## Installation Instructions
This pubblication has a GitHub code repository attached under the "Code" section.  
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

### Example UI Screenshots


### Usage Examples


## References
- [Agentic AI Developer Certification: LangGraph-Orchestrated Research Assistant for Ready Tensor](https://app.readytensor.ai/publications/agentic-ai-developer-certification-langgraph-orchestrated-research-assistant-for-ready-tensor-IQBETLgAsJ9X)  
- [LangChain](https://www.langchain.com/langchain)
- [LangGraph](https://www.langchain.com/langgraph)                  
- [Openai API](https://platform.openai.com/account/api-keys)
- [Tavily](https://www.tavily.com/)  
- [MIT Licence](https://opensource.org/license/mit)
- [Streamlit](https://docs.streamlit.io/)
- [Mermaid](https://mermaid.js.org/)               
- [Ready Tensor Certifications](https://app.readytensor.ai/hubs/ready_tensor_certifications)
- [Technical Evaluation Rubric](https://app.readytensor.ai/publications/WsaE5uxLBqnH)
- [Engage and Inspire: Best Practices for Publishing on Ready Tensor](https://app.readytensor.ai/publications/engage_and_inspire_best_practices_for_publishing_on_ready_tensor_SBgkOyUsP8qQ)



## Contributing
We welcome contributions to improve the Ready Tensor Publication Explorer!

1. **Fork** the [GitHub repository](https://github.com/Joshua-Abok/rag_apk)
2. **Create a feature branch:**
   ```bash
   git checkout -b your-feature-name
   ```
3. **Commit and push your changes**
4. **Submit a Pull Request** and describe your contribution.

Please follow our code style and guidelines. For questions or suggestions, [open an issue](LINK TO BE ENCLOSED).

### Future Implementations
We are actively seeking contributors who want to help implement and/or propose the following future features:



Feel free to suggest more ideas by opening an issue or starting a discussion!  For bug reports or feature requests, [open an issue](LINK TO BE ENCLOSED). For general questions or share your thoughts, start a [comment](LINK TO BE ENCLOSED).


## License
This publication is licensed under the [MIT License](LICENSE).


## Contact
michelaagostini73@gmail.com


## Acknowledgments
This project is part of the **Agentic AI Developer Certification**  program by the [Ready Tensor](https://www.readytensor.ai). We appreciate the contributions of the Ready Tensor developer community for their guidance and contributions. 


