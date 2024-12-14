*** Settings ***
Library    DateTime
Library    OperatingSystem
Library    .venv/lib/python3.12/site-packages/robot/libraries/Collections.py
Library    ../.venv/lib/python3.12/site-packages/robot/libraries/Process.py
Library    ../.venv/lib/python3.12/site-packages/robot/libraries/Telnet.py
Library    ../.venv/lib/python3.12/site-packages/robot/libraries/String.py

*** Variables ***
@{TIMES}    09.00    12.00    18.00    00.00
${CITY}    Helsinki
${COUNTRY}    Finland

*** Test Cases ***
Prompt Returns Correct Dates and Times
    # test that the prompt feature works
    ${inputs}=    Catenate    SEPARATOR=\n    ${CITY}    ${COUNTRY}
    ${result}=    Run Process    python3    app.py    stdin=${inputs}

    ${today}=    Get Current Date    result_format=%d.%m.%Y
    ${tomorrow}=    Get Current Date    result_format=%d.%m.%Y    increment=1 day
    ${day_after_tomorrow}=    Get Current Date    result_format=%d.%m.%Y    increment=2 days
    ${day_four}=    Get Current Date    result_format=%d.%m.%Y    increment=3 days

    Should Contain Any    ${result.stdout}    ${today}    ${tomorrow}    ${day_after_tomorrow}    ${day_four}
    Should Contain Any    ${result.stdout}    @{TIMES}