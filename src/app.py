
# app.py

"""
Streamlit UI for comparing scientific publications.
"""

import os
import json
from datetime import datetime
from html import escape
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
src_dir = Path("src")
from paths import SRC_DIR
from explorer import PublicationExplorer
#from paths import SAMPLE_PUBLICATION_DIR, OUTPUTS_DIR
from src.paths import SAMPLE_PUBLICATION_DIR, OUTPUTS_DIR

# Load environment variables
load_dotenv()

# Load API keys
openai_key = os.getenv("OPENAI_API_KEY", "")
tavily_key = os.getenv("TAVILY_API_KEY", "")

# Streamlit configuration
st.set_page_config(page_title="Publication Comparator", layout="wide")
st.title("📊 Scientific Publication Comparator")

# Sidebar: API Key status
with st.sidebar:
    st.subheader("🔐 API Keys")
    st.write("✅ OPENAI_API_KEY loaded." if openai_key else "❌ OPENAI_API_KEY not found.")
    st.write("✅ TAVILY_API_KEY loaded." if tavily_key else "❌ TAVILY_API_KEY not found.")
    if openai_key:
        st.text(f"OPENAI: {openai_key[:5]}{'*' * (len(openai_key) - 10)}{openai_key[-5:]}")
    if tavily_key:
        st.text(f"TAVILY: {tavily_key[:5]}*****")

# Load publication files
pub_dir = Path(SAMPLE_PUBLICATION_DIR)
pub_files = sorted(f.name for f in pub_dir.glob("*.txt"))
pub_file_options = [""] + pub_files  # Empty default

pub1 = st.selectbox("Select Publication 1", pub_file_options, index=0, key="pub1")
pub2 = st.selectbox("Select Publication 2", pub_file_options, index=0, key="pub2")

# Query selection with empty default
query_options = [""] + [
    "Tool Usage", "Evaluation Methods", "Task Types", "Datasets", "Results", "Other (custom)"
]
query_choice = st.selectbox("Select a query type", query_options, index=0)

# Handle user query input
if query_choice == "":
    user_query = ""
elif query_choice == "Other (custom)":
    user_query = st.text_input("Type your custom query:")
else:
    user_query = query_choice

# Comparison logic
if st.button("🚀 Run Comparison"):
    if not pub1 or not pub2:
        st.warning("Please select both publications before running the comparison.")
    elif not user_query:
        st.warning("Please select or enter a valid query before running the comparison.")
    else:
        explorer = PublicationExplorer()
        state = {
            "pub1_path": str(pub_dir / pub1),
            "pub2_path": str(pub_dir / pub2),
            "user_query": user_query,
            "pub1_profile": "",
            "pub2_profile": "",
            "comparison": "",
            "trends": "",
            "summary": "",
            "fact_check": "",
            "extra_info": "",
            "lnode": "",
            "count": 0
        }

        #result = explorer.graph.invoke(state)
        with st.spinner("🔍 Processing publications... This may take a moment."):
            result = explorer.graph.invoke(state)


        # Display results
        st.subheader("✅ Summary")
        st.text_area("Summary", result.get("summary", "[No summary]"), height=300)

        with st.expander("📘 Fact Check"):
            st.text_area("Fact Check", result.get("fact_check", "[No fact check]"), height=300)

        with st.expander("🧠 Enrichment"):
            st.text_area("ReAct Agent Output", result.get("extra_info", "[No enrichment]"), height=300)

        # Save results
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_filename = f"comparison_{Path(pub1).stem}_vs_{Path(pub2).stem}_{timestamp}"
        output_json_path = Path(OUTPUTS_DIR) / f"{base_filename}.json"
        output_html_path = Path(OUTPUTS_DIR) / f"{base_filename}.html"

        try:
            # Save JSON
            with open(output_json_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2, ensure_ascii=False)

            # Save HTML
            html_content = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Comparison Report - {escape(pub1)} vs {escape(pub2)}</title>
                <style>
                    body {{ font-family: Arial, sans-serif; margin: 2rem; }}
                    h1 {{ color: #2a4d69; }}
                    h2 {{ color: #4b86b4; }}
                    pre {{ background: #f4f4f4; padding: 1em; border-radius: 5px; overflow-x: auto; }}
                </style>
            </head>
            <body>
                <h1>📊 Scientific Publication Comparison</h1>
                <p><strong>Query:</strong> {escape(user_query)}</p>
                <h2>✅ Summary</h2>
                <pre>{escape(result.get("summary", "[No summary]"))}</pre>
                <h2>📘 Fact Check</h2>
                <pre>{escape(result.get("fact_check", "[No fact check]"))}</pre>
                <h2>🧠 Enrichment</h2>
                <pre>{escape(result.get("extra_info", "[No enrichment]"))}</pre>
            </body>
            </html>
            """
            with open(output_html_path, "w", encoding="utf-8") as f:
                f.write(html_content)

            st.success(f"📝 Results saved:\n• {output_json_path.name}\n• {output_html_path.name}")
        except Exception as e:
            st.error(f"❌ Failed to save results: {e}")
