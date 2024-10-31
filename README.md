# Weather App

Python app that retrieves weather data for prompted location from the yr.no API and displays it in a simple format.

![Screencap from the app at work](/resources/commandline-screencap.png)

Command line, Python & Robot Framework nerdery! The next step is to fix all my tests after adding the possibility to prompt a location. Check my [test plan](/tests/test_plan.md) for details. I am also considering expanding this into a web application, probably with React so that it would render automatically.

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