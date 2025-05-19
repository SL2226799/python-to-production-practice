#!/bin/bash

set -e

EXIT_STATUS=0
# Check if the virtual environment is activated
black --config black.toml || ((EXIT_STATUS++))
isort --settings-path .isort.toml || ((EXIT_STATUS++))
flake8 --config .flake8 || ((EXIT_STATUS++))
mypy --config-file mypy.ini || ((EXIT_STATUS++))
pylint --rcfile .pylintrc || ((EXIT_STATUS++))
ruff --config .ruff.toml || ((EXIT_STATUS++))

echo "Exiting with status: $EXIT_STATUS"
exit $EXIT_STATUS
