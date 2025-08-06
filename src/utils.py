
# utils.py

"""
Utility functions for file handling, path safety, and secure display.
"""

import os
import re
from typing import List
from pathlib import Path
from paths import SRC_DIR

def list_text_files(directory: str) -> List[str]:
    """
    Lists all .txt files in the given directory, sorted alphabetically.

    Args:
        directory (str): Path to the directory.

    Returns:
        List[str]: List of .txt filenames in the directory.
    """
    if not os.path.isdir(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")
    return sorted([f for f in os.listdir(directory) if f.endswith(".txt")])


def clean_filename(title: str) -> str:
    """
    Sanitizes a publication title to be a safe filename.

    Args:
        title (str): The title of the publication.

    Returns:
        str: A sanitized filename-safe string.
    """
    return re.sub(r'[^\w\-_ ]', '_', title).strip()


def mask_api_key(key: str, visible_chars: int = 5) -> str:
    """
    Masks the middle part of an API key for secure display.

    Args:
        key (str): The API key to mask.
        visible_chars (int): Number of leading/trailing characters to show.

    Returns:
        str: Masked key.
    """
    if len(key) <= 2 * visible_chars:
        return "*" * len(key)
    return f"{key[:visible_chars]}{'*' * (len(key) - 2 * visible_chars)}{key[-visible_chars:]}"


def ensure_directory_exists(path: str) -> None:
    """
    Ensures a directory exists by creating it if missing.

    Args:
        path (str): Path to the directory.
    """
    os.makedirs(path, exist_ok=True)


#def read_txt_file(path: str) -> str:
#    with open(path, encoding="utf-8") as f:
#        return f.read()
