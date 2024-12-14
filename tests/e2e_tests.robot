*** Settings ***
Library    DateTime
Library    OperatingSystem
Library    .venv/lib/python3.12/site-packages/robot/libraries/Collections.py
Library    ../.venv/lib/python3.12/site-packages/robot/libraries/Process.py

*** Variables ***
@{TIMES}    09.00    12.00    18.00    00.00
${CITY}    Helsinki
${COUNTRY}    Finland

*** Test Cases ***
App Gives Correct Data For Today & The Following 3 Days In Correct Form
    ${handle}=    Start Process    python3    app.py    stdin=${CITY}    stdin=${COUNTRY}
    ${result}=    Wait For Process    ${handle}
    ${output}=    Get Process Result    ${result}
    Log    ${output}
    ${today}=    Get Current Date    result_format=%d.%m.%Y
    ${tomorrow}=    Get Current Date    result_format=%d.%m.%Y    increment=1 day
    ${day_after_tomorrow}=    Get Current Date    result_format=%d.%m.%Y    increment=2 days
    ${day_four}=    Get Current Date    result_format=%d.%m.%Y    increment=3 days

    FOR    ${item}    IN    @{result}
        ${date}    Get From Dictionary    ${item}    date
        ${time}    Get From Dictionary    ${item}    time
        Should Contain Any    ${date}    ${today}    ${tomorrow}    ${day_after_tomorrow}    ${day_four}
        Should Contain Any    ${time}    @{TIMES}
        Should Contain    ${item}    temperature    °C
        Should Contain    ${item}    details
    END