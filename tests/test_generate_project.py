from pathlib import Path

from cookiecutter.main import cookiecutter

ROOT_PATH = Path(__file__).parent.parent
PROJECT_NAME = "Test Project"
PROJECT_SLUG = "test-project"


def test_generate_project(tmp_path: Path):
    cookiecutter(
        template=ROOT_PATH.as_posix(),
        no_input=True,
        extra_context={"project_name": PROJECT_NAME},
        output_dir=tmp_path.as_posix(),
    )

    assert tmp_path.joinpath(PROJECT_SLUG).exists()
    assert tmp_path.joinpath(f"{PROJECT_SLUG}/test_project").exists()
