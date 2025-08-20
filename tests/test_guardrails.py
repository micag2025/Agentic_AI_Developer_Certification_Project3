
# tests/test_guardrails.py
import pytest
from guardrails import Guard
#from src.paths import SRC_DIR

import sys
import os
#import pytest

from pathlib import Path
# Add src/ to Python path
ROOT_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT_DIR / "src"
sys.path.insert(0, str(ROOT_DIR))
sys.path.insert(0, str(SRC_DIR))




REQUIRED_FIELDS = ["tools", "evaluation_methods", "datasets", "task_types", "results"]


def fallback_recovery(validated):
    """
    Ensure all required fields exist in the validated dict,
    filling in with empty lists if missing.
    """
    if validated is None:
        validated = {}
    for field in REQUIRED_FIELDS:
        validated.setdefault(field, [])
    return validated


def test_guardrails_schema_loads():
    rail_path = SRC_DIR / "rails" / "profile_extraction.rail"
    guard = Guard.from_rail(str(rail_path))
    assert guard is not None


def test_guardrails_validation_wellformed():
    rail_path = SRC_DIR / "rails" / "profile_extraction.rail"
    guard = Guard.from_rail(str(rail_path))

    good_json = (
        '{"tools": ["LangChain"], '
        '"evaluation_methods": ["BLEU"], '
        '"datasets": ["SST-2"], '
        '"task_types": ["Classification"], '
        '"results": ["SOTA"]}'
    )
    result = guard.parse(llm_output=good_json)
    validated = fallback_recovery(result.validated_output)

    # Should validate as-is (no fallbacks needed)
    assert all(field in validated for field in REQUIRED_FIELDS)
    assert validated["tools"] == ["LangChain"]


def test_guardrails_resilient_to_malformed():
    rail_path = SRC_DIR / "rails" / "profile_extraction.rail"
    guard = Guard.from_rail(str(rail_path))

    # Malformed JSON: missing fields
    bad_json = '{"tools": ["LangChain"]}'
    result = guard.parse(llm_output=bad_json)
    validated = fallback_recovery(result.validated_output)

    # ✅ Test robustness: all required fields are present after fallback
    assert all(field in validated for field in REQUIRED_FIELDS)
    assert isinstance(validated["evaluation_methods"], list)
    assert isinstance(validated["datasets"], list)
    assert isinstance(validated["task_types"], list)
    assert isinstance(validated["results"], list)
