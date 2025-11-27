"""Post generation hooks."""

from pathlib import Path

WORKFLOW_PATH = Path("./.github/workflows")


def remove_files_and_dirs(is_deployed_to_pypi: bool, is_deployed_to_gh: bool) -> None:
    """Remove files and directories."""
    files_and_dirs_to_remove: list[Path] = []

    if is_deployed_to_pypi is False:
        files_and_dirs_to_remove.append(WORKFLOW_PATH / "release_to_pypi.yml")

    if is_deployed_to_gh is False:
        files_and_dirs_to_remove.append(WORKFLOW_PATH / "release_to_gh.yml")

    for obj in files_and_dirs_to_remove:
        if obj.is_dir():
            obj.rmdir()
        else:
            obj.unlink()


if __name__ == "__main__":
    IS_DEPLOYED_TO_PYPI = True if "{{ cookiecutter.deploy_to_pypi }}" == "True" else False
    IS_DEPLOYED_TO_GH = True if "{{ cookiecutter.deploy_to_gh }}" == "True" else False
    remove_files_and_dirs(
        is_deployed_to_pypi=IS_DEPLOYED_TO_PYPI, is_deployed_to_gh=IS_DEPLOYED_TO_GH
    )
