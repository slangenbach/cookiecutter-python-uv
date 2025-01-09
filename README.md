# cookiecutter-python-uv

[Cookiecutter][1] template for Python projects using [uv][2] featuring:

- Flexible project structure using the [src layout][3]
- Python version and Python dependency management with [uv][2]
- Code linting and formatting with [ruff][4]
- Testing with [pytest][5]
- Automated quality assurance with [pre-commit][6]
- CICD with [GitHub Actions][7]

## Prerequisites

- Python 3.12+
- [uv][2]
- [Cookiecutter][1]

## Installation

Install [Cookiecutter][1] via uv: `uv tool install cookiecutter`

## Usage

Generate the project structure via `uv tool run cookiecutter https://github.com/slangenbach/cookiecutter-python-uv`

## Contributing

1. Run project setup: `uv sync` and `uv run pre-commit install`
1. Create a dedicated development branch: `git checkout -b YOUR-BRANCH-NAME`
1. Make changes
1. Run linters: `uv run pre-commit run all-files`
1. Run tests: `uv run pytest`
1. Commit changes and create a pull request


[1]: https://github.com/cookiecutter/cookiecutter
[2]: https://docs.astral.sh/uv/
[3]: https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/
[4]: https://docs.astral.sh/ruff/
[5]: https://docs.pytest.org/en/stable/
[6]: https://pre-commit.com/
[7]: https://docs.github.com/en/actions
