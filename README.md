# Weather App

Python app that retrieves weather data for prompted location from the yr.no API and displays it in a simple format. Location coordinates are fetched from the OpenWeatherMap API.

![Screencap from the app at work](/resources/commandline-screencap.png)

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