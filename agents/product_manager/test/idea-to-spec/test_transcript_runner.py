import importlib.util
import json
import os
import tempfile
import unittest
from pathlib import Path


RUNNER_PATH = (
    Path(__file__).resolve().parent / "transcript_runner.py"
)


def load_runner_module():
    spec = importlib.util.spec_from_file_location(
        "idea_to_spec_transcript_runner",
        RUNNER_PATH,
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class TranscriptRunnerTests(unittest.TestCase):
    def test_build_codex_command_uses_mandated_model_and_effort(self):
        runner = load_runner_module()

        command = runner.build_codex_command(
            "我想做一个 AI 对话助手",
            cwd=Path("/tmp/ws"),
            output_path=Path("/tmp/ws/result.txt"),
        )

        self.assertIn("-m", command)
        self.assertEqual(command[command.index("-m") + 1], "gpt-5.6-luna")
        self.assertIn('model_reasoning_effort="medium"', command)
        self.assertIn("-o", command)
        self.assertEqual(command[command.index("-o") + 1], "/tmp/ws/result.txt")
        self.assertEqual(command[-1], "我想做一个 AI 对话助手")

    def test_prepare_execution_workspace_removes_reserved_and_custom_outputs(self):
        runner = load_runner_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            eval_root = Path(temp_dir) / "eval"
            exec_root = Path(temp_dir) / "exec"

            (eval_root / "with_skill/outputs").mkdir(parents=True)
            (eval_root / "without_skill/outputs").mkdir(parents=True)
            (eval_root / "docs/input").mkdir(parents=True)
            (eval_root / "with_skill/outputs/transcript.md").write_text("old")
            (eval_root / "without_skill/outputs/transcript.md").write_text("old")
            (eval_root / "comparison.auto.md").write_text("stale")
            (eval_root / "PRD.md").write_text("stale-prd")
            (eval_root / "docs/input/fixture.md").write_text("fixture")
            (eval_root / "README.md").write_text("readme")
            (eval_root / "eval_metadata.json").write_text("{}")

            runner.prepare_execution_workspace(
                eval_root,
                exec_root,
                cleanup_paths=["PRD.md"],
            )

            self.assertFalse((exec_root / "README.md").exists())
            self.assertFalse((exec_root / "eval_metadata.json").exists())
            self.assertTrue((exec_root / "docs/input/fixture.md").exists())
            self.assertFalse((exec_root / "with_skill").exists())
            self.assertFalse((exec_root / "without_skill").exists())
            self.assertFalse((exec_root / "comparison.auto.md").exists())
            self.assertFalse((exec_root / "PRD.md").exists())

    def test_read_result_file_reads_codex_output(self):
        runner = load_runner_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            result_path = Path(temp_dir) / "result.txt"
            result_path.write_text("structured transcript")

            self.assertEqual(
                runner.read_result_file(result_path),
                "structured transcript",
            )

            missing_path = Path(temp_dir) / "missing.txt"
            with self.assertRaises(ValueError):
                runner.read_result_file(missing_path)

    def test_sync_declared_outputs_copies_existing_candidates(self):
        runner = load_runner_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            exec_root = Path(temp_dir) / "exec"
            eval_root = Path(temp_dir) / "eval"

            (exec_root / "with_skill/outputs").mkdir(parents=True)
            (exec_root / "docs/pm/feature").mkdir(parents=True)
            (eval_root / "with_skill/outputs").mkdir(parents=True)
            (eval_root / "docs/pm/feature").mkdir(parents=True)

            (exec_root / "with_skill/outputs/transcript.md").write_text("fresh")
            (exec_root / "docs/pm/feature/PRD.md").write_text("prd")

            runner.sync_declared_outputs(
                exec_root,
                eval_root,
                [
                    "with_skill/outputs/transcript.md",
                    ["docs/pm/feature/design.md", "docs/pm/feature/PRD.md"],
                ],
            )

            self.assertEqual(
                (eval_root / "with_skill/outputs/transcript.md").read_text(),
                "fresh",
            )
            self.assertEqual(
                (eval_root / "docs/pm/feature/PRD.md").read_text(),
                "prd",
            )
            self.assertFalse((eval_root / "docs/pm/feature/design.md").exists())

    def test_generate_eval_outputs_copies_transcripts_as_runtime_diagnostics(self):
        runner = load_runner_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            eval_root = temp_root / "eval"
            eval_root.mkdir()
            metadata = eval_root / "eval_metadata.json"
            metadata.write_text(
                json.dumps(
                    {
                        "eval_id": "eval-001-runtime-transcript",
                        "eval_name": "runtime-transcript",
                        "prompt": "Check transcript diagnostics.",
                    }
                )
            )

            def fake_run_codex(command, cwd, timeout_seconds):
                output_path = Path(command[command.index("-o") + 1])
                label = "with_skill" if "with_skill" in str(output_path) else "without_skill"
                output_path.parent.mkdir(parents=True, exist_ok=True)
                transcript = f"{label} transcript"
                output_path.write_text(transcript)
                return transcript, {
                    "command": command,
                    "cwd": str(cwd),
                    "timeout": False,
                    "returncode": 0,
                    "stdout_length": len(transcript),
                    "stderr": "",
                    "duration_ms": 1,
                    "result_length": len(transcript),
                }

            old_run_codex = runner.run_codex
            old_output_dir = os.environ.get("EVAL_RUN_OUTPUT_DIR")
            runner.run_codex = fake_run_codex
            os.environ["EVAL_RUN_OUTPUT_DIR"] = str(temp_root / "runs")
            try:
                runner.generate_eval_outputs(metadata)
            finally:
                runner.run_codex = old_run_codex
                if old_output_dir is None:
                    os.environ.pop("EVAL_RUN_OUTPUT_DIR", None)
                else:
                    os.environ["EVAL_RUN_OUTPUT_DIR"] = old_output_dir

            runtime_root = temp_root / "runs/product_manager/eval"
            self.assertEqual(
                (runtime_root / "with_skill/outputs/transcript.md").read_text(),
                "with_skill transcript",
            )
            self.assertEqual(
                (runtime_root / "without_skill/outputs/transcript.md").read_text(),
                "without_skill transcript",
            )


if __name__ == "__main__":
    unittest.main()
