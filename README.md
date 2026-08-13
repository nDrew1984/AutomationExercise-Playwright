# AutomationExercise Playwright Tests

Automated test suite for [automationexercise.com](https://automationexercise.com) using Playwright and Python.

## Tech Stack
- Python 3.14
- Playwright 1.61
- pytest

## Project Structure
- `tests/` - test files
- `conftest.py` - fixtures (cookie handling, navigation)
- `page_selectors.py` - selectors
- `test_data.py` - test data

## Installation
pip install -r requirements.txt
playwright install

## Run Tests
pytest tests/ -v --headed