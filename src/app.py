
# app.py

"""
Streamlit UI for comparing scientific publications.
"""

# 🧠 STREAMLIT APP FOR PUBLICATION COMPARATOR

import os
import json
from datetime import datetime
from html import escape
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

from explorer import PublicationExplorer
from src.paths import SAMPLE_PUBLICATION_DIR, COMPARISONS_DIR, OUTPUTS_DIR, LOGS_DIR, PROFILES_DIR

# 🌍 Load .env configuration
load_dotenv()

# 🔐 API keys
openai_key = os.getenv("OPENAI_API_KEY", "")
tavily_key = os.getenv("TAVILY_API_KEY", "")

# 📱 Streamlit UI Setup
st.set_page_config(page_title="Publication Comparator", layout="wide")
#st.title("📊 Scientific Publication Comparator")
st.title("📊 AI-Powered Ready Tensor Publication Comparator")
st.markdown("""
Simply select two `.txt` publication files and a query type to compare:

- Tools  
- Tasks  
- Datasets  
- Evaluation Methods  
- Results  

---

🧠 **The backend ensures**:
- Structured extraction  
- Robust validation  
- Traceable output
""")


# 📂 Sidebar Info
with st.sidebar:
    st.markdown("## 🤖 About this App")
    st.markdown("""
This AI-powered comparison tool uses:

- 🔗 **LangChain** for LLM orchestration  
- 💬 **OpenAI** for LLM completions  
- 🔎 **Tavily** for web-based fact checks  
- 🖥 **Streamlit** for interactive visualization

---
### 📁 Output Locations
- 🧪 Validated profiles → `outputs/profiles/`
- 🔄 Comparisons → `outputs/comparisons/`
- 📝 Logs → `logs/`

---
""")

    # ⬇️ Download buttons
    #profiles_dir = OUTPUTS_DIR / "profiles"
    profiles_dir = PROFILES_DIR
    comparisons_dir = COMPARISONS_DIR
    logs_dir = LOGS_DIR

    latest_profile = sorted(profiles_dir.glob("validated_profile_pub*.json"), reverse=True)
    if latest_profile:
        with open(latest_profile[0], "rb") as f:
            st.download_button("⬇️ Download Latest Validated Profile", f, file_name=latest_profile[0].name)

    latest_cmp = sorted(comparisons_dir.glob("comparison_*.json"), reverse=True)
    if latest_cmp:
        with open(latest_cmp[0], "rb") as f:
            st.download_button("⬇️ Download Latest Comparison", f, file_name=latest_cmp[0].name)

    latest_log = sorted(logs_dir.glob("*.log"), reverse=True)
    if latest_log:
        with open(latest_log[0], "rb") as f:
            st.download_button("⬇️ Download Latest Log", f, file_name=latest_log[0].name)

# 📄 Load publications
pub_dir = Path(SAMPLE_PUBLICATION_DIR)
pub_files = sorted(f.name for f in pub_dir.glob("*.txt"))
pub1 = st.selectbox("Select Publication 1", [""] + pub_files, key="pub1")
pub2 = st.selectbox("Select Publication 2", [""] + pub_files, key="pub2")

# 🧠 Query Selection
query_options = [""] + [
    "Tool Usage", "Evaluation Methods", "Task Types", "Datasets", "Results", "Other (custom)"
]
query_choice = st.selectbox("Select a query type", query_options)

user_query = ""
if query_choice == "Other (custom)":
    user_query = st.text_input("Type your custom query:")
elif query_choice:
    user_query = query_choice

# 🚀 Comparison Trigger
if st.button("🚀 Run Comparison"):
    if not pub1 or not pub2:
        st.warning("Please select both publications before running the comparison.")
    elif not user_query:
        st.warning("Please enter or select a valid query.")
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

        # ✅ Display Results
        st.subheader("✅ Summary")
        st.text_area("Summary", result.get("summary", "[No summary]"), height=300)

        with st.expander("📘 Fact Check"):
            st.text_area("Fact Check", result.get("fact_check", "[No fact check]"), height=300)

        with st.expander("🧠 Enrichment"):
            st.text_area("ReAct Agent Output", result.get("extra_info", "[No enrichment]"), height=300)

        # 📝 Save Results
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_name = f"comparison_{Path(pub1).stem}_vs_{Path(pub2).stem}_{timestamp}"
        json_path = COMPARISONS_DIR / f"{base_name}.json"
        html_path = COMPARISONS_DIR / f"{base_name}.html"

        try:
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2, ensure_ascii=False)


            # Save HTML report
            html_report = f"""
            <!DOCTYPE html>
            <html>
            <head><meta charset="UTF-8"><title>Comparison</title></head>
            <body>
                <h1>📊 Comparison</h1>
                <p><strong>Query:</strong> {escape(user_query)}</p>
                <h2>✅ Summary</h2><pre>{escape(result.get("summary", "[No summary]"))}</pre>
                <h2>📘 Fact Check</h2><pre>{escape(result.get("fact_check", "[No fact check]"))}</pre>
                <h2>🧠 Enrichment</h2><pre>{escape(result.get("extra_info", "[No enrichment]"))}</pre>
            </body>
            </html>
            """
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(html_report)

            # Get latest validated profiles
            #profile_files = sorted((OUTPUTS_DIR / "profiles").glob("validated_profile_pub*.json"), reverse=True)
            profile_files = sorted((PROFILES_DIR).glob("validated_profile_pub*.json"), reverse=True)
            latest_profiles = [p.name for p in profile_files[:2]]  # pub1 and pub2

            # Get latest log
            log_files = sorted((Path("logs")).glob("*.log"), reverse=True)
            latest_log = log_files[0].name if log_files else "No log file found"

            # Display success message
            st.success(
                f"📝 Results saved:\n"
                f"• 🧪 Comparison JSON: `{json_path.name}`\n"
                f"• 📄 Comparison HTML: `{html_path.name}`\n"
                f"• ✅ Validated Profiles: `{', '.join(latest_profiles)}`\n"
                f"• 🗒 Log File: `{latest_log}`"
            )

        except Exception as e:
            st.error(f"❌ Failed to save results: {e}")

            #st.success(f"📝 Results saved:\n• {json_path.name}\n• {html_path.name}")
        #except Exception as e:
            #st.error(f"❌ Failed to save results: {e}")
