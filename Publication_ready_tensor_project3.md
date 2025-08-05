# Agentic AI Developer Certification: Productionizing LangGraph-Orchestrated Research Assistant for Ready Tensor

## TAGS: AAIDC, AAIDC-M3, Agentic AI, Multi-Agent Systems, AI Agents, Guardrails, Production Systems, Resilience, Security, Testing, UI, API Design, Deployment, Streamlit, Streamlit Cloud, LangChain, LangGraph (Agent), AI Orchestration, Pytest(?)

## Author : Michela Agostini 

## Models : Github

## Dataset: project_1_publications.json

## TL;DR
TO BE DRAFTED 

## Tool Overview & Architecture
This project uses a sample dataset and is built around (is structured on) a modular LangChain-based pipeline.

### Sample Dataset:
A collection of 35 Ready Tensor publications, each of them characterised by id, username, license, title, and publication description. There are 6 types of licenses; 27 publications use “MIT” or “CC”, the rest are “none” or missing. Under MIT/CC, reuse is permitted for open source projects.

### Features & Modules:
This project is structured on a modular LangChain-based pipeline in which each feature is mapped to the specific tool or module implementing it:


### Workflow: The LangChain-based pipeline is designed to:



## Features

## Installation Instructions
This pubblication has a GitHub code repository attached under the "Code" section.

## Running the Application


### Example UI Screenshots


### Usage Examples


## References
- [LangChain](https://www.langchain.com/langchain)                 
- [Openai API](https://platform.openai.com/account/api-keys)
- [MIT Licence](https://opensource.org/license/mit)
- [Streamlit](https://docs.streamlit.io/)               
- [Ready Tensor Certifications](https://app.readytensor.ai/hubs/ready_tensor_certifications)
- [Technical Evaluation Rubric](https://app.readytensor.ai/publications/WsaE5uxLBqnH)
- [Engage and Inspire: Best Practices for Publishing on Ready Tensor](https://app.readytensor.ai/publications/engage_and_inspire_best_practices_for_publishing_on_ready_tensor_SBgkOyUsP8qQ)
- [The Open Source Repository Guide: Best Practices for Sharing Your AI/ML and Data Science Projects](https://app.readytensor.ai/publications/best-practices-for-ai-project-code-repositories-0llldKKtn8Xb)


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
















Prerequisites: Python 3.10+, pip, and access to the referenced dataset.

Clone the repository
git clone https://github.com/micag2025/Agentic_AI_Developer_Certification-Project_1.git
cd Agentic_AI_Developer_Certification-Project_1
git checkout dev
Create and activate a virtual environment:
python3 -m venv .venv
source .venv/bin/activate        # Linux / macOS
.\.venv\Scripts\activate         # Windows
Set your environment variables:
export OPEN_API_KEY=your_open_api_key_here    # Linux / macOS
set OPEN_API_KEY=your_open_api_key_here       # Windows
Install dependencies:
pip install -r requirements.txt
Running the Application
Launch the App
Note: The sample dataset is available in the "Datasets" section.

streamlit run app/main.py
Open in browser
Streamlit will provide a local URL (usually http://localhost:8501). Open it in your browser.
You can now interact with the Ready Tensor Publication Explorer!

Example UI Screenshots
Home Page
The main landing page of the Ready Tensor Publication Explorer, showing a search bar (selectbox for choosing a publication title and viewing its details) before the chat interface.

Home Page

Publication Search
The search bar interface where users can view and search publications by title. (OR The search bar filters publications by title and the selectbox lists all filtered titles)

Publication Search

Publication Details
Detailed view of the content of the selected publication, selected by title (When a title is selected, its content is shown)

Publication Details

Q&A Chat Interface
Interactive chat interface for asking questions about publications using the RAG-powered assistant.

Q&A Chat Interface

_Note: When a user asks a question in the chat, the agent has access to the content of all publications and can retrieve information from any or all of them to answer the query. The chat input can be used to ask about any aspect of the dataset, including questions that span multiple publications. Therefore, the agent will use the full dataset to answer, not just the selected publication.

Usage Examples
The assistant helps users explore and comprehend Ready Tensor publications. Example general queries might be:

Get a summary:
“What is VAE?”
Extract details from a paper:
“What models or tools were used in these publications?”
Discuss limitations:
“Are there any assumptions or limitations mentioned in these publications?”
Use Cases:

For Ready Tensor Users: Summarize papers or topics, chat with publication content
In Academia: Automate literature reviews, semantic search for proposals
For Developers/Engineers: Extract code examples, compare models
In Enterprises/Institutions: Knowledge management, research assistant for editors
API Documentation
API keys are stored securely in environment variables (for secure access). The API exposes endpoints for querying and interacting with Ready Tensor publications using the RAG pipeline.

Note: All endpoints require authentication using your OPENAI_API_KEY.

References
LangChain
Openai API
MIT Licence
CC Licenses
Streamlit
Ready Tensor Certifications
Technical Evaluation Rubric
Engage and Inspire: Best Practices for Publishing on Ready Tensor
Markdown for Machine Learning Projects: A Comprehensive Guide
The Open Source Repository Guide: Best Practices for Sharing Your AI/ML and Data Science Projects
Contributing
We welcome contributions to improve the Ready Tensor Publication Explorer!

Fork the GitHub repository
Create a feature branch:
git checkout -b your-feature-name
Commit and push your changes
Submit a Pull Request and describe your contribution.
Please follow our code style and guidelines. For questions or suggestions, open an issue.

Future Implementations
We are actively seeking contributors who want to help implement and/or propose the following future features:

Advanced UI/UX: Develop a more intuitive and visually appealing web interface.
Expanded Dataset Support: Enable ingestion of additional publication formats and sources.
Fine-tuned LLM Models: Incorporate domain-specific or fine-tuned LLMs for improved accuracy.
User Authentication & Profiles: Add user management, history tracking, and personalization.
Integration with Ready Tensor Platform: Seamlessly connect with Ready Tensor’s broader ecosystem and APIs.
Export & Reporting: Allow users to export summaries or Q&A sessions in various formats (PDF, CSV, etc).
Feedback & Rating System: Let users rate answers to improve system performance.
Feel free to suggest more ideas by opening an issue or starting a discussion! For bug reports or feature requests, open an issue. For general questions or share your thoughts, start a comment.

License
This publication is licensed under the MIT License.

Contact
chibueze.k.muoneke@gmail.com, michelaagostini73@gmail.com, nyajuaya.j.a@gmail.com

Acknowledgments
This project is part of the Agentic AI Developer Certification program by the Ready Tensor. We appreciate the contributions of the Ready Tensor developer community for their guidance and contributions.



