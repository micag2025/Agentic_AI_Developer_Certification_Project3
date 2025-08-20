# paths.py

"""
Project-level path resolution that works in scripts, notebooks, and Streamlit.
"""

from pathlib import Path
import inspect
import os
# Get project root 
# Dynamic resolution for script + notebook/Streamlit
try:
    ROOT_DIR = Path(__file__).resolve().parent.parent
except NameError:
    ROOT_DIR = Path(inspect.stack()[0].filename).resolve().parent.parent


#  Define all paths relative to ROOT_DIR

DATA_DIR = ROOT_DIR / "data"
SAMPLE_PUBLICATION_DIR = DATA_DIR / "sample_publications"
OUTPUTS_DIR = ROOT_DIR / "outputs"

PROFILES_DIR = OUTPUTS_DIR / "profiles"
COMPARISONS_DIR = OUTPUTS_DIR / "comparisons"
TESTS_DIR = ROOT_DIR / "tests"

#PUBLICATION_FPATH = DATA_DIR / "project_1_publications.json"
DOCS_DIR = ROOT_DIR / "docs"
SRC_DIR = ROOT_DIR / "src"
RAILS_DIR = SRC_DIR / "rails"

# Convert to str for os compatibility
DATA_DIR = str(DATA_DIR)
SAMPLE_PUBLICATION_DIR = str(SAMPLE_PUBLICATION_DIR)
OUTPUTS_DIR = str(OUTPUTS_DIR)

#PROFILES_DIR = str(PROFILES_DIR)
#COMPARISONS_DIR = str(COMPARISONS_DIR)

#PUBLICATION_FPATH = str(PUBLICATION_FPATH)
DOCS_DIR = str(DOCS_DIR)
#print(f"[DEBUG] ROOT_DIR resolved to: {ROOT_DIR}")
LOGS_DIR = ROOT_DIR / "logs"



if __name__ == "__main__":
    print("📁 Project Path Summary")
    print(f"ROOT_DIR: {ROOT_DIR}")
    print(f"DATA_DIR: {DATA_DIR}")
    print(f"SRC_DIR: {SRC_DIR}")
    print(f"RAILS_DIR: {RAILS_DIR}")
    print(f"OUTPUTS_DIR: {OUTPUTS_DIR}")
    print(f"SAMPLE_PUBLICATION_DIR: {SAMPLE_PUBLICATION_DIR}")
    print(f"DOCS_DIR: {DOCS_DIR}")
    print(f"LOGS_DIR: {LOGS_DIR}")
    print(f"PROFILES_DIR:{PROFILES_DIR}")
    print(f"COMPARISONS_DIR: {COMPARISONS_DIR}")      
    print(f"TESTS_DIR: {TESTS_DIR}") 
   
