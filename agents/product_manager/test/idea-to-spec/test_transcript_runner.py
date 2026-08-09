import importlib.util
from pathlib import Path


RUNNER = Path(__file__).with_name("transcript_runner.py")


def load_runner():
    spec = importlib.util.spec_from_file_location("pm_transcript_runner", RUNNER)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_generate_outputs_delegates_one_metadata_eval(monkeypatch, tmp_path: Path) -> None:
    runner = load_runner()
    definition = type(
        "Definition",
        (),
        {
            "repository_root": tmp_path,
            "agent": "product_manager",
            "skill": "idea-to-spec",
            "eval_id": "eval-001-user-request",
        },
    )()
    calls = []
    monkeypatch.setattr(runner, "definition_from_metadata", lambda path: definition)
    monkeypatch.setattr(
        runner,
        "run_selected_eval",
        lambda **kwargs: calls.append(kwargs) or {"overall_result": "PASS"},
    )

    assert runner.generate_eval_outputs(tmp_path / "eval_metadata.json") == [
        {"overall_result": "PASS"}
    ]
    assert calls == [
        {
            "repository_root": tmp_path,
            "agent": "product_manager",
            "skill": "idea-to-spec",
            "eval_id": "eval-001-user-request",
            "timeout_seconds": runner.DEFAULT_TIMEOUT_SECONDS,
        }
    ]


def test_transcript_runner_has_no_mirror_or_shared_home_logic() -> None:
    source = RUNNER.read_text(encoding="utf-8")
    assert "mirror_dependency_documents" not in source
    assert "install_entry_skill" not in source
    assert "build_isolated_env" not in source
    assert "shutil.copytree" not in source
