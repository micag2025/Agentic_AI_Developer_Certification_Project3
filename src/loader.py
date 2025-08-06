# loader.py

"""
Extracts publications from data/project_1_publications.json and saves each one
as an individual .txt file in data/sample_publications/.
"""


#import os
#from paths import ROOT_DIR

#os.chdir(ROOT_DIR)
#print(f"[DEBUG] Changed working directory to project root: {ROOT_DIR}")




import os
import json
import logging
from typing import Dict, Any

from pathlib import Path
from paths import SRC_DIR
from paths import DATA_DIR, SAMPLE_PUBLICATION_DIR

#from paths import DATA_DIR, SAMPLE_PUBLICATION_DIR
from utils import clean_filename, ensure_directory_exists

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def extract_publications_from_json(data_dir: str, output_dir: str) -> int:
    """
    Loads publications from a JSON file in the data directory and saves each
    publication to a separate .txt file.

    Args:
        data_dir (str): Directory containing the dataset JSON file.
        output_dir (str): Directory to store the extracted .txt files.

    Returns:
        int: Number of publications successfully written.
    """
    ensure_directory_exists(output_dir)

    json_path = f"{data_dir}/project_1_publications.json"

    try:
        with open(json_path, "r", encoding="utf-8") as f:
            publications = json.load(f)
    except FileNotFoundError:
        logger.error(f"❌ File not found: {json_path}")
        return 0
    except json.JSONDecodeError as e:
        logger.error(f"❌ Invalid JSON format: {e}")
        return 0

    saved = 0
    for idx, pub in enumerate(publications):
        title = pub.get("title", f"publication_{idx}")
        safe_title = clean_filename(title)
        file_path = os.path.join(output_dir, f"{safe_title}.txt")

        try:
            with open(file_path, "w", encoding="utf-8") as txt_file:
                txt_file.write(f"{title}\n\n")
                for key, value in pub.items():
                    if key != "title":
                        txt_file.write(f"{key.capitalize()}:\n{value}\n\n")
            saved += 1
        except Exception as e:
            logger.warning(f"⚠️ Failed to write file '{file_path}': {e}")

    logger.info(f"✅ Saved {saved} publications to '{output_dir}'")
    return saved


if __name__ == "__main__":
    logger.info("📦 Extracting publications...")
    logger.debug(f"Using DATA_DIR: {DATA_DIR}")
    logger.debug(f"Saving to: {SAMPLE_PUBLICATION_DIR}")
    extract_publications_from_json(DATA_DIR, SAMPLE_PUBLICATION_DIR)
