# {{cookiecutter.project_name}}

![CI](https://github.com/slangenbach/{{cookiecutter.project_slug}}/actions/workflows/ci.yml/badge.svg)
{%- if cookiecutter.deploy_to_gh %}
![Github](https://github.com/slangenbach/{{cookiecutter.project_slug}}/actions/workflows/release_to_gh.yml/badge.svg)
{%- endif %}
{%- if cookiecutter.deploy_to_pypi %}
![PyPI](https://github.com/slangenbach/{{cookiecutter.project_slug}}/actions/workflows/release_to_pypi.yml/badge.svg)
{%- endif %}

{{cookiecutter.project_description}}

![Logo](assets/logo.png)

## About

tbd

## Prerequisites

- [uv][1]
- [Task][2]

## Installation

1. Make sure you meet the prerequisites
1. Setup the development environment: `task setup`

## Configuration

Edit the **.env** file in project root directory and set the following variables:

| Variable | Description | Note |
| --- | --- | --- |
| LOG_LEVEL | Set the logging level | Defaults to 'INFO'

## Usage

tbd

## Troubleshooting

tbd

## Contributing

Check out [Contributing](Contributing.md) for further information.


[1]: https://docs.astral.sh/uv/
[2]: https://taskfile.dev/
