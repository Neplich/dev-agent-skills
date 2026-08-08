import importlib.util
import tempfile
from pathlib import Path


RUNNER = Path(__file__).with_name("run_eval.py")
RUN_ALL = Path(__file__).with_name("run_all_evals.py")


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_runner_delegates_to_shared_executor() -> None:
    runner = load(RUNNER, "docs_run_eval")
    calls = []
    runner.compatibility_main = lambda agent: calls.append(agent) or 0

    assert runner.main() == 0
    assert calls == ["docs"]


def test_run_all_discovers_every_metadata_file() -> None:
    run_all = load(RUN_ALL, "docs_run_all")
    with tempfile.TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        metadata = root / "sample/evals/workspace/eval-001/eval_metadata.json"
        metadata.parent.mkdir(parents=True)
        metadata.write_text("{}", encoding="utf-8")
        assert run_all.find_eval_metadata(root) == [metadata]


def test_runner_contains_no_candidate_or_fixture_logic() -> None:
    source = RUNNER.read_text(encoding="utf-8")
    assert "Expected output" not in source
    assert "copy_fixture" not in source
    assert "build_candidate_prompt" not in source
    assert "subprocess.run" not in source
