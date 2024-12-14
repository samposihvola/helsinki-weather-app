*** Settings ***
Library    DateTime
Library    ../utils/location_weather.py    WITH NAME    LOCATION_WEATHER
Library    ../utils/weather_printer.py    WITH NAME    WEATHER_PRINTER
Library    .venv/lib/python3.12/site-packages/robot/libraries/Collections.py

*** Variables ***
@{TIMES}    09.00    12.00    18.00    00.00

*** Test Cases ***
Code Has Access To Both APIs And Returns Correct Data
    [Documentation]    Checks that the data is in dictionary form. 
    ...    If it's not, the code returns an error message and thus the test will fail.
    ${result}=   LOCATION_WEATHER.Get Weather    ${}
    Log    ${result}
    ${passed}=    Run Keyword And Return Status    Evaluate    type(${result})
    ${type}=      Run Keyword If     ${passed}    Evaluate    type(${result})


App Gives Correct Data For Today & The Following 3 Days In Correct Form
    ${result}=   WEATHER_PRINTER.Format Weather Data
    ${today}=    Get Current Date    result_format=%d.%m.%Y
    ${tomorrow}=    Get Current Date    result_format=%d.%m.%Y    increment=1 day
    ${day_after_tomorrow}=    Get Current Date    result_format=%d.%m.%Y    increment=2 days
    ${day_four}=    Get Current Date    result_format=%d.%m.%Y    increment=3 days

    FOR    ${item}    IN    @{result}
        ${date}=    Get From Dictionary    ${item}    date
        ${time}=    Get From Dictionary    ${item}    time
        Should Contain Any    ${date}    ${today}    ${tomorrow}    ${day_after_tomorrow}    ${day_four}
        Should Contain Any    ${time}    @{TIMES}
        Should Contain    ${item}    temperature    °C
        Should Contain    ${item}    details
    END