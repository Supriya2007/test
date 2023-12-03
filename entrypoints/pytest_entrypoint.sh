#! /bin/sh
set -e
python -m pytest -v --cov=. --cov-report=xml:/output/coverage.xml
