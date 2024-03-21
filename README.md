### Installation
Converted to Pipenv to remove the dependency on virtualenv and pip. Simply install pipenv (`pip install pipenv`), then run `pipenv --python 3.9`. This will build a new virtual environment. Run `pipenv run shell` to activate the environment. Finally, run `pipenv install` to install all dependencies.

Go to Project Settings ->  Settings -> Project -> Python Interpreter -> Add Interpreter -> Add Local Interpreter -> Pipenv Environment



### Running Tests
Run the following commands:

- `pytest` - To run all tests
- `pytest -m {mark}` To run all tests for a certain mark (located in the pyproject.toml file)
- `pytest --headful` To run all tests in a headful state
- `pytest --browser {browser_choice}` To run all tests in a specific browser (chromium, webkit, or firefox)

Each command can be combined such as `pytest -m elements --headful --browser chromium`
