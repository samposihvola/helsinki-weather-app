# Helsinki Weather App

Python app that retrieves weather data for Helsinki from the yr.no API and displays it in a simple format.

![Screencap from the app](/commandline-screencap.png)

Command line, Python & Robot Framework nerdery! There are still things to be done with this project: the next step is to create more tests for the Python code with Robot Framework. After that I am thinking of expanding this app into a modern-day web application. Then this would be the backend of the project.

## Todo

- Tests with Robot Framework
- Okay okay, maybe there could be a web UI as well?
  - Weather statistics included?
- CI/CD??

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