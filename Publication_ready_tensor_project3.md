# Agentic AI Developer Certification: Productionizing LangGraph-Orchestrated Research Assistant for Ready Tensor

## TAGS: AAIDC, AAIDC-M3, Agentic AI, Multi-Agent Systems, AI Agents, Guardrails, Production Systems, Resilience, Security, Testing, UI, API Design, Deployment, Streamlit, Streamlit Cloud, LangChain, LangGraph (Agent), AI Orchestration, Pytest(?)

## Author : Michela Agostini 

## Models : Github

## Dataset: project_1_publications.json

## TL;DR
The Ready Tensor Publication Explorer is an advanced AI-powered tool that utilizes Retrieval-Augmented Generation (RAG) techniques to automate the handling of a sample dataset that contains Ready Tensor technical documentation. By leveraging RAG models, the system delivers accurate and context-aware responses to (natural language) user queries. Integrating OpenAI embeddings, semantic search capabilities, and a user-friendly interface, this tools offers a scalable and efficient solution for Ready Tensor users, developers, researchers, and organizations searching streamlined access to documentation resources enclosed in the Ready Tensor platform by exploring its contents and asking questions.

## Tool Overview & Architecture
This project uses a sample dataset and is built around (is structured on) a modular LangChain-based pipeline.

Sample Dataset:
A collection of 35 Ready Tensor publications, each of them characterised by id, username, license, title, and publication description. There are 6 types of licenses; 27 publications use “MIT” or “CC”, the rest are “none” or missing. Under MIT/CC, reuse is permitted for open source projects.

Features & Modules:
This project is structured on a modular LangChain-based pipeline in which each feature is mapped to the specific tool or module implementing it:

Feature	Tool / Library / Module
Prompt formulation	LangChain PromptTemplate
Vector store retrieval	Chroma Vector Database
LLM-generated response	OpenAI GPT-3.5/4 via LangChain
Document ingestion & embedding	LangChain DocumentLoader, OpenAI Embeddings, Chroma
Minimal UI for interaction	Streamlit (or Flask/FastAPI as implemented)
Example queries, retrieval, response eval	LangChain Chains & Evaluators
Session-based memory/intermediate reasoning	LangChain ReAct, ConversationBuffer
Workflow: The LangChain-based pipeline is designed to:

Generate/process user prompts
Retrieve relevant content using Chroma
Use Large Language Models (LLMs) for context-aware responses
Ingest/index documentation into vector DB
Offer user interface for interaction
Support session memory and intermediate reasoning TO BE VERIFIED
Enable example queries for validation
The core workflow and system architecture of the application are illustrated in the following flowchart.
flowchart_modified

Features
Automated Documentation Ingestion: Efficient extraction and processing of Ready Tensor publications (while preserving structure).
Vector Database Storage (Chroma): Fast, reliable embedding storage and retrieval.
Semantic Search (OpenAI Embeddings): Intelligent, context-aware lookup for relevant documentation.
RAG-Based Q&A: Contextually precise answers to user queries about publications.
Minimal UI: Simple, interactive interface (for exploration).
Scalable and Fast: Handles large datasets with quick indexing and retrieval.
Installation Instructions
This pubblication has a GitHub code repository attached under the "Code" section.

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



