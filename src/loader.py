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

from paths import SRC_DIR
src_dir = Path("src")
#from paths import SRC_DIR

import sys
sys.path.insert(0, str(SRC_DIR.parent))



from src.paths import SAMPLE_PUBLICATION_DIR, COMPARISONS_DIR, PROFILES_DIR
from src.explorer import PublicationExplorer
from src.logger import logger  # ✅ Use central logger


def health_check() -> bool:
    """Simple health check for environment and directories."""
    required_dirs = [SAMPLE_PUBLICATION_DIR, COMPARISONS_DIR, Path("outputs/profiles"), Path("logs")]
    for d in required_dirs:
        if not Path(d).exists():
            logger.error(f"❌ Missing required directory: {d}")
            return False
    if not os.getenv("OPENAI_API_KEY"):
        logger.warning("⚠️ OPENAI_API_KEY not set.")
    return True


def run_app():
    """Main function to run the Streamlit app."""
    # Load environment variables
    load_dotenv()
    openai_key = os.getenv("OPENAI_API_KEY", "")
    tavily_key = os.getenv("TAVILY_API_KEY", "")

    # Streamlit configuration
    st.set_page_config(page_title="Publication Comparator", layout="wide")
    st.title("📊 Scientific Publication Comparator")
    st.caption(
        "Simply select two `.txt` files and a query to compare tools, tasks, datasets, "
        "evaluation methods, and results. The backend ensures structured extraction, "
        "robust validation, and traceable output."
    )

    # Sidebar: About this App
    with st.sidebar:
        st.markdown("## 🤖 About this App")
        st.markdown(
            """
            This AI-powered publication comparison tool leverages:

            - 🔗 **LangChain** for LLM orchestration  
            - 💬 **OpenAI** for fast and reliable LLM interfaces  
            - 🔎 **Tavily** for factual web search enrichment  
            - 🖥 **Streamlit** for building this interactive interface  

            📂 Where comparison results are saved: `outputs/comparisons/`  
            📂 Where validated profiles are saved: `outputs/profiles/`  
            📁 Where logs are stored: `logs/`  
            """
        )

    # Health check
    if not health_check():
        st.error("❌ Health check failed. Please check logs for details.")
        return

    # Load publication files
    pub_dir = Path(SAMPLE_PUBLICATION_DIR)
    pub_files = sorted(f.name for f in pub_dir.glob("*.txt"))
    pub_file_options = [""] + pub_files

    pub1 = st.selectbox("Select Publication 1", pub_file_options, index=0, key="pub1")
    pub2 = st.selectbox("Select Publication 2", pub_file_options, index=0, key="pub2")

    query_options = [""] + [
        "Tool Usage", "Evaluation Methods", "Task Types", "Datasets", "Results", "Other (custom)"
    ]
    query_choice = st.selectbox("Select a query type", query_options, index=0)

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

            with st.spinner("🔍 Processing publications... This may take a moment."):
                result = explorer.graph.invoke(state)

            # ✅ Always save validated profiles
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            if result.get("pub1_profile"):
                profile_path1 = PROFILES_DIR / f"validated_profile_pub1_{timestamp}.json"
                with open(profile_path1, "w", encoding="utf-8") as f:
                    json.dump(result["pub1_profile"], f, indent=2, ensure_ascii=False)

            if result.get("pub2_profile"):
                profile_path2 = PROFILES_DIR / f"validated_profile_pub2_{timestamp}.json"
                with open(profile_path2, "w", encoding="utf-8") as f:
                    json.dump(result["pub2_profile"], f, indent=2, ensure_ascii=False)

                #try:
                    #result = explorer.graph.invoke(state)
                #except Exception as e:
                    #logger.exception("❌ Error during graph execution")
                    #st.error(f"❌ Comparison failed: {e}")
                    #return

            # Display results
            st.subheader("✅ Summary")
            st.text_area("Summary", result.get("summary", "[No summary]"), height=300)

            with st.expander("📘 Fact Check"):
                st.text_area("Fact Check", result.get("fact_check", "[No fact check]"), height=300)

            with st.expander("🧠 Enrichment"):
                st.text_area("ReAct Agent Output", result.get("extra_info", "[No enrichment]"), height=300)

            # Save results
            #timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            base_filename = f"comparison_{Path(pub1).stem}_vs_{Path(pub2).stem}_{timestamp}"
            output_json_path = Path(COMPARISONS_DIR) / f"{base_filename}.json"
            output_html_path = Path(COMPARISONS_DIR) / f"{base_filename}.html"

            try:
                with open(output_json_path, "w", encoding="utf-8") as f:
                    json.dump(result, f, indent=2, ensure_ascii=False)

                html_content = f"""
                <!DOCTYPE html>
                <html lang="en">
                <head><meta charset="UTF-8"><title>Comparison Report</title></head>
                <body>
                    <h1>📊 Scientific Publication Comparison</h1>
                    <p><strong>Query:</strong> {escape(user_query)}</p>
                    <h2>✅ Summary</h2><pre>{escape(result.get("summary", "[No summary]"))}</pre>
                    <h2>📘 Fact Check</h2><pre>{escape(result.get("fact_check", "[No fact check]"))}</pre>
                    <h2>🧠 Enrichment</h2><pre>{escape(result.get("extra_info", "[No enrichment]"))}</pre>
                </body>
                </html>
                """
                with open(output_html_path, "w", encoding="utf-8") as f:
                    f.write(html_content)

                logger.info(f"📝 Results saved: {output_json_path}, {output_html_path}")
                st.success(
                    f"📝 Results saved successfully:\n\n"
                    f"• Validated profiles → `outputs/profiles/`\n"
                    f"• Comparison → `{output_json_path.name}` / `{output_html_path.name}`\n"
                    f"• Logs → `logs/`"
                )
            except Exception as e:
                logger.exception("❌ Failed to save results")
                st.error(f"❌ Failed to save results: {e}")


# ✅ Only run Streamlit app if executed directly, not when imported for testing
if __name__ == "__main__":
    run_app()
