*** Settings ***
Library    weather.py

*** Test Cases ***
Get Access To The API
    [Documentation]    Test that the weather API returns a status code of 200.
    ${weather_data}=    Get Helsinki Weather
    Should Not Be Empty    ${weather_data}