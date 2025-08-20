
# tests/test_explorer.py
import pytest
from unittest.mock import MagicMock


import sys
import os
#import pytest

from pathlib import Path
# Add src/ to Python path
ROOT_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT_DIR / "src"
sys.path.insert(0, str(ROOT_DIR))
sys.path.insert(0, str(SRC_DIR))



from src.explorer import PublicationExplorer





@pytest.fixture
def explorer():
    exp = PublicationExplorer()
    exp.model = MagicMock()
    exp.react_agent = MagicMock()
    return exp


def test_analyze_pub1(explorer, sample_pub_files):
    pub1, pub2 = sample_pub_files
    state = {"pub1_path": pub1, "pub2_path": pub2, "user_query": "Tool Usage", "count": 0}

    explorer.model.invoke.return_value.content = '{"tools": ["HuggingFace"], "evaluation_methods": ["BLEU"], "datasets": [], "task_types": ["NLP"], "results": ["Good performance"]}'
    result = explorer.analyze_pub1(state)

    assert "pub1_profile" in result
    assert isinstance(result["pub1_profile"], dict)
    assert "HuggingFace" in result["pub1_profile"]["tools"]


def test_compare(explorer, sample_pub_files):
    pub1, pub2 = sample_pub_files
    state = {
        "pub1_path": pub1,
        "pub2_path": pub2,
        "user_query": "Datasets",
        "pub1_profile": {"datasets": ["SST-2"]},
        "pub2_profile": {"datasets": ["IMDB"]},
        "count": 0,
    }

    explorer.model.invoke.return_value.content = "Both use benchmark datasets."
    result = explorer.compare(state)

    assert "comparison" in result
    assert "datasets" in result["comparison"].lower()


def test_react_agent_tool(explorer, sample_pub_files):
    pub1, pub2 = sample_pub_files
    state = {"pub1_path": pub1, "pub2_path": pub2, "user_query": "Extra info", "count": 0}

    explorer.react_agent.run.return_value = "Enriched insights."
    result = explorer.react_agent_tool(state)

    assert "extra_info" in result
    assert "insights" in result["extra_info"]
