
# tests/conftest.py
import sys
import os
import pytest
from pathlib import Path

# Add src/ to Python path
ROOT_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT_DIR / "src"
sys.path.insert(0, str(ROOT_DIR))
sys.path.insert(0, str(SRC_DIR))


@pytest.fixture
def sample_pub_files(tmp_path):
    """Create two temporary publication files for testing."""
    pub1 = tmp_path / "pub1.txt"
    pub2 = tmp_path / "pub2.txt"

    pub1.write_text("This is publication 1. It uses HuggingFace and BLEU.")
    pub2.write_text("This is publication 2. It benchmarks transformers on SST-2.")

    return str(pub1), str(pub2)
