
# tests/test_app.py
import pytest
from pathlib import Path
from streamlit.testing.v1 import AppTest

SRC_DIR = Path(__file__).resolve().parents[1] / "src"


@pytest.mark.skipif(not SRC_DIR.joinpath("app.py").exists(), reason="App file missing")
def test_app_runs(monkeypatch):
    """Test that the Streamlit app renders without crashing."""
    at = AppTest.from_file(str(SRC_DIR / "app.py"))
    at.run(timeout=10)

    assert at.title[0].value.startswith("📊") or at.title[0].value.startswith("AI")
