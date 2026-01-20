---
applyTo: "**/*.py"
---
# Python Conventions

## Tooling & Tasks
This project uses uv (package manager), ruff (linting/formatting), ty (type checking), pytest (testing) and taskfile (task runner).

- task setup - Setup dev environment  
- task lint - Run ruff and other linters via pre-commit
- task test - Run pytest via uv

## Project Structure
- data/ - Data files
- infra/ - Infrastructure
- notebooks/ - Jupyter notebooks
- src/ - Source code
- tests/ - Test files

## Core Modules
- config.py - Pydantic Settings with .env, access via get_config()
- constants.py - ROOT_PATH, DATA_PATH, and project constants
- errors.py - Custom exceptions inheriting from CustomError
- logger.py - Use get_logger(__name__) for logging

## Environment Variables
Settings use Pydantic Settings loaded from .env. When adding a new setting:
1. Add to config.py as a class attribute
2. Add to .env with the value
3. Add to .env.example (omit value if secret)
4. Add to the configuration table in README.md

## Testing
- Use pytest-mock (not unittest.mock)
- Use built-in pytest fixtures when possible
- Shared fixtures go in conftest.py

## Rules
- Use get_config() for configuration, not os.getenv()
- Use get_logger(__name__) for logging, not print()
- Define custom exceptions in errors.py, not inline
- Add constants to constants.py, not scattered in modules
