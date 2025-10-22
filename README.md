# cookiecutter-python-uv

![CI](https://github.com/slangenbach/cookiecutter-python-uv/actions/workflows/ci.yml/badge.svg)

[Cookiecutter][1] template for Python projects using [uv][2] featuring:

- Flexible project structure using the [src layout][3]
- Python version and Python dependency management with [uv][2]
- Code linting and formatting with [ruff][4]
- Type checking using [ty][8]
- Testing with [pytest][5]
- Automated quality assurance with [pre-commit][6]
- CICD with [GitHub Actions][7]
- Task management using [Task][9]

## Prerequisites

- [uv][2]
- [Task][9]

## Installation

Install [cruft][10] via uv: `uv tool install cruft`

## Usage

Generate the project structure via `uv tool run cruft create https://github.com/slangenbach/cookiecutter-python-uv`

```
|- .devcontainer/                   <- devcontainer configuration
|- .github/                         <- GitHub Actions workflows
|- .vscode/                         <- VSCode configuration
|- data/                            <- Data for debugging and testing
|- infra/                           <- Infrastructure-as-Code
|- notebooks/                       <- Jupyter notebooks
|- src/                             <- Source code
|- tests/                           <- Tests
|- .gitignore                       <- Files ignored by git
|- .pre-commit-config.yaml          <- pre-commit configuration
|- .env                             <- Actual .env file
|- .env.example                     <- Dummy .env file
|- .python-version                  <- Python version used by package
|- pyproject.toml                   <- Package and tooling configuration
|- README.md                        <- Top-level README
|- taskfile.yml                     <- Taskfile
|- uv.lock                          <- uv lock file
```

## Contributing

1. Create a dedicated branch
1. Add your contribution
1. Run linters: `task lint`
1. Run tests: `task test`
1. Commit, push and create a merge request


[1]: https://github.com/cookiecutter/cookiecutter
[2]: https://docs.astral.sh/uv/
[3]: https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/
[4]: https://docs.astral.sh/ruff/
[5]: https://docs.pytest.org/en/stable/
[6]: https://pre-commit.com/
[7]: https://docs.github.com/en/actions
[8]: https://github.com/astral-sh/ty
[9]: https://taskfile.dev/
[10]: https://cruft.github.io/cruft/
