# Automation Testing Framework

This automation testing framework uses:
 - Python,
 - Selenium WebDriver,
 - Pytest,
 - Cucumber (pytest-bdd),
 - pytest-html,
 - tox.
 The framework implements the Screenplay pattern to improve test maintainability and readability.

# Screenplay pattern
The Screenplay Pattern is an advanced and extensible design pattern for writing maintainable and scalable automated test suites. It provides a clear structure and promotes separation of concerns, making it easier to understand and maintain the test code. Screenplay Pattern is an alternative to the Page Object Model (POM) pattern and was formerly known as the Journey Pattern.
<details>
<summary>read more...</summary>
  The Screenplay Pattern consists of the following key components:
  - Actors: An actor represents the user role in the test scenario. They can perform tasks, interact with the system, and ask questions about the system's state. Actors are not aware of the underlying implementation details, which helps to keep the tests focused on user interactions.
  - Abilities: Abilities are the skills that an actor possesses. Abilities define how an actor can interact with the system, such as browsing the web, using an API, or accessing a database. Abilities are implemented as separate classes, allowing for easy extensibility and reuse.
  - Tasks: Tasks are high-level actions performed by actors. Tasks are focused on user goals and are usually composed of multiple interactions with the system. They are designed to be reusable and are independent of the underlying UI or system structure. Tasks are written at a high level of abstraction, making them easy to read and understand.
  - Actions: Actions are low-level interactions with the system, such as clicking buttons, entering text, or selecting options from a dropdown menu. Actions are the building blocks for tasks and are usually tied to a specific ability. Like tasks, actions are also reusable and independent of the underlying UI or system structure.
  - Questions: Questions are used to query the state of the system or verify if certain conditions are met. Actors ask questions to gather information about the system and check if the expected outcome of a task has been achieved. Questions are designed to be reusable and independent of the underlying UI or system structure.
  - Outcomes: Outcomes represent the expected results or assertions that verify whether a test has passed or failed. Outcomes are usually based on the answers provided by questions.
  The Screenplay Pattern encourages writing tests that are focused on user interactions and goals. By separating concerns and promoting re-usability, the Screenplay Pattern makes it easier to write and maintain complex test suites. It also makes the tests more resilient to changes in the application's UI or system structure, reducing the need for frequent updates to the test code.
</details>

## Project Structure

<details>
<summary>The project is organized as follows, click to expand</summary>
  
  ```commandline
    webdriver_screenplay_cucumber/
    ├── venv/
    ├── ...
    ├── features/
    │   └── login.feature
    ├── step_definitions/
    │   ├── init.py
    │   └── test_login.py
    ├── abilities/
    │   ├── init.py
    │   └── browse_the_web.py
    ├── actors/
    │   ├── init.py
    │   └── actor.py
    ├── questions/
    │   ├── init.py
    │   └── is_user_logged_in.py
    ├── tasks/
    │   ├── init.py
    │   ├── login.py
    │   └── navigate_to_login.py
    ├── conftest.py
    ├── tox.ini
    └── requirements.txt
  ```
</details>

- `venv/`: Contains the virtual environment files.
- `features/`: Contains the feature files written in Gherkin syntax.
- `step_definitions/`: Contains the step definition files that implement the scenarios in the feature files.
- `abilities/`: Contains the ability classes for the Screenplay pattern.
- `actors/`: Contains the actor classes for the Screenplay pattern.
- `questions/`: Contains the question classes for the Screenplay pattern.
- `tasks/`: Contains the task classes for the Screenplay pattern.
- `conftest.py`: Contains Pytest configurations and fixtures.
- `tox.ini`: Contains the Tox configuration for running tests in multiple environments.
- `requirements.txt`: Lists the project's dependencies.

## Getting Started

1. Clone the repository.

2. Create and activate a virtual environment:
```commandline
  python -m venv venv
  source venv/bin/activate
```

3. Install the required packages:

```commandline
    pip install -r requirements.txt
```

```commandline
    tox -- --browser=firefox
    allure serve allure-results
```

4. Run tests using Tox:

```commandline
    tox
```


This will generate an HTML report named `report.html` in the root directory.

## Adding New Tests

1. Create a new feature file in the `features` directory using Gherkin syntax.

2. Implement the step definitions in the `step_definitions` directory.

3. If needed, create new ability, task, and question classes in the corresponding directories.

4. Run tests using Tox to ensure everything works as expected.

