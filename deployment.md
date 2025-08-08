# 🚀 Deployment Guide

This guide explains how to deploy the **Scientific Publication Comparator** application in various environments: local machine, Docker, Streamlit Cloud, and Hugging Face Spaces.

---


## 🏗️ Prerequisites

- **Python:** Version >= 3.10
- **API Keys:**  
  - `OPENAI_API_KEY` (get from [OpenAI](https://platform.openai.com/))
  - `TAVILY_API_KEY` (get from [Tavily](https://tavily.com/))

---


## 📦 Local Deployment

1. **Clone the Repository**
    ```bash
    git clone https://github.com/micag2025/Agentic_AI_Developer_Certification_Project3
    cd Agentic_AI_Developer_Certification_Project3
    ```

2. **Set Up a Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Environment Variables**
    - Create a `.env` file in the project root directory with the following content:
      ```env
      OPENAI_API_KEY=your-openai-key
      TAVILY_API_KEY=your-tavily-key
      ```

5. **Run the Application (Streamlit App)**
    ```bash
    streamlit run src/app.py
    ```
    - The app will be available at: [http://localhost:8501](http://localhost:8501)

---


## 🐳 Docker Deployment

1. **Build the Docker Image**
    ```bash
    docker build -t pub-comparator .
    ```

2. **Run the Docker Container**
    ```bash
    docker run -p 8501:8501 \
      -e OPENAI_API_KEY=your-openai-key \
      -e TAVILY_API_KEY=your-tavily-key \
      pub-comparator
    ```

3. **Access the Application**
    - Visit: [http://localhost:8501](http://localhost:8501)

---


## ☁️ Streamlit Cloud Deployment

1. **Push your project** to GitHub (if not already).
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud) and log in.
3. Click **"New app"** and connect to your repo.
4. Set your **Python version** and **run command**:
    ```bash
    streamlit run src/app.py
    ```
5. **Add environment variables** under “Advanced Settings”:
    - `OPENAI_API_KEY`
    - `TAVILY_API_KEY`
6. Click **"Deploy"**.

- Your app will be available at a URL like:  
  `https://share.streamlit.io/your-username/publication-comparator/main/app.py`

---

## 🌐 Hugging Face Spaces Deployment

1. Go to [huggingface.co/spaces](https://huggingface.co/spaces)
2. **Create a new Space** and choose **Streamlit** as the SDK.
3. **Upload your code** (or connect your repo).
4. Define secrets in the **"Secrets"** tab:
    - `OPENAI_API_KEY`
    - `TAVILY_API_KEY`
5. The app deploys automatically.

---


## 📂 Deployment File Structure (to be reviewed)
.
├── app.py                      # Streamlit entry point  
├── .env                        # Your local secrets  
├── Dockerfile                  # Container definition (if using Docker)  
├── requirements.txt  
├── outputs/  
│   ├── profiles/               # Validated publication profiles (.json)  
│   └── comparison/            # Comparison results (.json, .html)  
├── logs/                       # Log files (.log)  
├── src/  
└── ...  



---

## 📌 Deployment Tips

- **Never hardcode secrets:** Always use environment variables. Add `.env.example` to your repo so others know what’s needed.
- **Restart the app** after updating `.env` or dependencies.
- **Test locally** before deploying to cloud or Docker.
- **Keep dependencies updated** in `requirements.txt`.
- **Check logs** in the `logs/` directory for troubleshooting.

---

## 📄 Example Files

**.env.example**
```env
OPENAI_API_KEY=your-openai-key
TAVILY_API_KEY=your-tavily-key



