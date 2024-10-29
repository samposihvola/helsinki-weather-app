# Helsinki Weather App

Python app that retrieves weather data for Helsinki from the yr.no API and displays it in a simple format.

![Screencap from the app at work](/resources/commandline-screencap.png)

Command line, Python & Robot Framework nerdery! The next step is to finish unit tests following my [test plan](/tests/test-plan.md). After that I am thinking 
of expanding this app into a modern-day web application. Then this would be the backend of the project.

## Todo

- E2E tests with Robot Framework
- Unit tests
- Prompt location -> search latitude & longitude -> insert to url as variables
- Web UI
  - Weather statistics for the location
- CI/CD

## Instructions

Run the app

```
python3 app.py
```

Install Robot Framework in a virtual environment

```
python3 -m venv .venv
source .venv/bin/activate
pip install robotframework
robot --version
```

If RequestsLibrary is not installed with the package, run

```
pip install robotframework-requests
```

Install pytest-mock

```
pip install pytest-mock
```

Install Coverage

```
source .venv/bin/activate
python3 -m pip install coverage
```
