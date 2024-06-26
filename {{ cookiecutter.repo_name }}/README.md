# {{ cookiecutter.project_name }}

A project package generated using the [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) library and the https://github.com/banditkings/ds_cookie template.

# Usage: with`poetry` + `pyenv`

## Set local `pyenv` environment

Let's say you want to create an environment using python version {{ cookiecutter.python_version }} (default: 3.10.6)

```bash
pyenv install {{ cookiecutter.python_version }}
```
Then navigate to the root directory and make it your local version:

```bash
pyenv local {{ cookiecutter.python_version }}
```

This creates a `.python-version` file. During cookie creation this should have prompted you for this for convenience

## Install dependencies and create the virtual env in `poetry`

```bash
# Install with optional dev and plotly dependencies
poetry install --with dev,plotly
```

This will install the required dependencies and the {{ cookiecutter.package_name }} package and create a virtual environment and virtual shell. You can exit the virtual shell with crtl+d or `exit` in terminal.

## Resuming work

Next time you enter into the directory, `pyenv` will detect and activate local python version and then you can restart the shell:

```bash
poetry shell
```
# Testing

To use `pytest` to run all tests in the `src\tests\` folder:


```bash
poetry run pytest
```

This will use `pytest` to search for files that start with test_*.py or *_test.py,
and within those files run `test` prefixed functions and methods. 

* See [pytest docs](https://docs.pytest.org/en/7.2.x/explanation/goodpractices.html)


# Git

See this [gist](https://gist.github.com/mindplace/b4b094157d7a3be6afd2c96370d39fad) for a reminder on the steps to initialize this as a git repo and push to a remote, empty repo.