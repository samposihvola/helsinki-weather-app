# Helsinki Weather App

Python app that retrieves weather data for Helsinki from the yr.no API and displays it in a clear, user-friendly format.

I want to develop a straightforward tool that allows me to check the weather directly from the command line. My primary motivation for this project is my obsession with the command line: it is by far my favourite UI and I want to create my own tools for it. Also a good chance for some Python & Robot Framework nerdery!

## Todo

- No need to append data from every hour into weather_data_next_3_days
  - {9am} {3pm} {9pm} is enough
- Tidy up the info in weather_data_next_3_days
- Format: 3x {date, time} {temperature} {rain/norain}
- Tests with Robot Framework
- CI/CD

## Instructions

Install Robot Framework in a virtual environment

```
python3 -m venv .venv
source .venv/bin/activate
pip install robotframework
robot --version
```