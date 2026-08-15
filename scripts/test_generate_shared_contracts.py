from pathlib import Path

import generate_shared_contracts as generator


def write_sources(root: Path) -> None:
    source = generator.source_root(root)
    source.mkdir(parents=True)
    for name in generator.CONTRACT_NAMES:
        (source / name).write_text(f"# {name}\n", encoding="utf-8")


def test_generate_creates_all_expected_files(tmp_path: Path) -> None:
    write_sources(tmp_path)

    generator.generate(tmp_path)

    assert len(generator.expected_files(tmp_path)) == 24
    assert generator.freshness_errors(tmp_path) == []


def test_freshness_reports_missing_stale_and_extra(tmp_path: Path) -> None:
    write_sources(tmp_path)
    generator.generate(tmp_path)
    paths = sorted(generator.expected_files(tmp_path))

    paths[0].unlink()
    paths[1].write_text("manual edit\n", encoding="utf-8")
    extra = paths[2].parent / "extra.md"
    extra.write_text("extra\n", encoding="utf-8")

    errors = generator.freshness_errors(tmp_path)

    assert any(error.startswith("missing generated contract:") for error in errors)
    assert any(error.startswith("stale generated contract:") for error in errors)
    assert any(error.startswith("extra generated contract:") for error in errors)


def test_generated_copy_declares_source(tmp_path: Path) -> None:
    write_sources(tmp_path)

    content = generator.generated_content("handoff-contract.md", tmp_path)

    assert content.startswith("<!-- GENERATED FILE: DO NOT EDIT.")
    assert "idea-to-spec/_internal/_shared/handoff-contract.md" in content
