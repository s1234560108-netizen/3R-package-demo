# 3R-package-demo

A Python application created for Session 1 of the
Repeatability, Reproducibility, and Replicability (3R) course.

Author: Shao Chien Chang

## Requirements

- Python 3.12 (tested with Python 3.12.10)
- Git
- pip

## Installation

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip install -e ".[test]"
```

## Usage

```bash
three_r_package --message="Hello 3R"
```

Expected result:

```text
Hello world!: Hello 3R
```

## Testing

```bash
python -m pytest
```

## Code Quality

```bash
make test-isort
make test-black
make test-flake8
make test-pylint
make test-pytest
```

## Project Structure

- `src/`: Python package and command-line interface
- `tests/unit/`: Unit tests
- `tests/integration/`: Integration tests
- `setup.cfg`: Package configuration
- `pyproject.toml`: Build configuration
- `requirements.txt`: Runtime dependencies
- `Makefile`: Development commands
- `.github/workflows/`: Continuous integration
- `Dockerfile`: Container configuration

## Template

Generated using the application template from the
course repository:

https://github.com/drweihungpan-lab/devops-python-package-template

Minor configuration and formatting changes were made
for Python 3.12 compatibility.

Cloud release and Docker linting in CI are disabled
until the required infrastructure is configured.

Template source commit:
13120a294e5b724956d57eecd7df2bdbe32f9c8a
