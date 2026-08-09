import importlib.util
from pathlib import Path


RUNNER = Path(__file__).with_name("run_eval.py")


def load_runner():
    spec = importlib.util.spec_from_file_location("devops_run_eval", RUNNER)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_runner_delegates_to_shared_executor() -> None:
    runner = load_runner()
    calls = []
    runner.compatibility_main = lambda agent: calls.append(agent) or 0

    assert runner.main() == 0
    assert calls == ["devops"]


def test_runner_contains_no_candidate_or_fixture_logic() -> None:
    source = RUNNER.read_text(encoding="utf-8")
    assert "Expected output" not in source
    assert "copy_fixture" not in source
    assert "build_candidate_prompt" not in source
    assert "subprocess.run" not in source
