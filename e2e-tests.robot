*** Settings ***
Library    RequestsLibrary
Library    DateTime
Library    .venv/lib/python3.12/site-packages/robot/libraries/Process.py
Library    utils.py    WITH NAME    UTILS
Library    .venv/lib/python3.12/site-packages/robot/libraries/Collections.py

*** Variables ***
@{TIMES}    09.00    12.00    18.00    00.00

*** Test Cases ***
API Returns Status Code 200
    # could you get user-agent & url variables from the code?
    ${header}    Create Dictionary    user-agent=https://github.com/samposihvola/helsinki-weather-app/tree/main
    ${response}    GET    url=https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=60.192059&lon=24.945831    headers=${header}
    Status Should Be    200

App Gives Data For Today & The Following 3 Days In Correct Form
    ${result}=   UTILS.Get Weather Data
    ${today}=    Get Current Date    result_format=%d.%m.%Y
    ${tomorrow}=    Get Current Date    result_format=%d.%m.%Y    increment=1 day
    ${day_after_tomorrow}=    Get Current Date    result_format=%d.%m.%Y    increment=2 days
    ${day_four}=    Get Current Date    result_format=%d.%m.%Y    increment=3 days

    FOR    ${item}    IN    @{result}
        ${date}=    Get From Dictionary    ${item}    date
        ${time}=    Get From Dictionary    ${item}    time
        Should Contain Any    ${date}    ${today}    ${tomorrow}    ${day_after_tomorrow}    ${day_four}
        Should Contain Any    ${time}    @{TIMES}
    END
 
    