import importlib.util
import sys
from pathlib import Path

import pytest


SUMMARIZER_PATH = Path(__file__).with_name("summarize_eval_results.py")
SUMMARIZER_SPEC = importlib.util.spec_from_file_location(
    "summarize_eval_results_under_test",
    SUMMARIZER_PATH,
)
assert SUMMARIZER_SPEC is not None
assert SUMMARIZER_SPEC.loader is not None
summarizer = importlib.util.module_from_spec(SUMMARIZER_SPEC)
sys.modules[SUMMARIZER_SPEC.name] = summarizer
SUMMARIZER_SPEC.loader.exec_module(summarizer)


@pytest.mark.parametrize(
    ("line", "expected"),
    [
        ("- Overall result: **PASS (partial coverage)**。", "PARTIAL"),
        ("* **Overall result**：**PASS**", "PASS"),
        ("+ **Overall result:** **FAIL**", "FAIL"),
        ("  - Overall Result：***BLOCKED***", "BLOCKED"),
    ],
)
def test_extract_result_supports_overall_result_variants(
    tmp_path: Path,
    line: str,
    expected: str,
) -> None:
    comparison = tmp_path / "comparison.md"
    comparison.write_text(f"# Comparison\n\n{line}\n", encoding="utf-8")

    assert summarizer.extract_result(comparison) == expected


def test_extract_result_prefers_overall_result(tmp_path: Path) -> None:
    comparison = tmp_path / "comparison.md"
    comparison.write_text(
        "- Latest result: PASS\n- Overall result: **FAIL**\n",
        encoding="utf-8",
    )

    assert summarizer.extract_result(comparison) == "FAIL"


@pytest.mark.parametrize(
    ("content", "expected"),
    [
        ("- Latest result: PASS\n", "PASS"),
        ("## Latest Result\n\nThe latest validation is PARTIAL.\n", "PARTIAL"),
    ],
)
def test_extract_result_keeps_legacy_latest_result_fallback(
    tmp_path: Path,
    content: str,
    expected: str,
) -> None:
    comparison = tmp_path / "comparison.md"
    comparison.write_text(content, encoding="utf-8")

    assert summarizer.extract_result(comparison) == expected


def test_main_reports_fail_bucket(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    evals_dir = tmp_path / "agents/example/test/sample/evals"
    workspace_dir = evals_dir / "workspace/eval-001"
    workspace_dir.mkdir(parents=True)
    (evals_dir / "evals.json").write_text(
        """
{
  "evals": [
    {
      "id": "eval-001-failure",
      "workspace": "workspace/eval-001"
    }
  ]
}
""".strip(),
        encoding="utf-8",
    )
    (workspace_dir / "comparison.md").write_text(
        "- Overall result: FAIL\n",
        encoding="utf-8",
    )

    original_root = summarizer.ROOT
    summarizer.ROOT = str(tmp_path)
    try:
        summarizer.main()
    finally:
        summarizer.ROOT = original_root

    output = capsys.readouterr().out
    assert "| example | `sample` | 1 | 1 FAIL |" in output
    assert "1 FAIL" in output
