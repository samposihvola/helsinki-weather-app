*** Settings ***
Library    utils.py
Library    RequestsLibrary

*** Test Cases ***
API Returns Status Code 200
    ${header}    Create Dictionary    user-agent=https://github.com/samposihvola/helsinki-weather-app/tree/main
    ${response}    GET    url=https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=60.192059&lon=24.945831    headers=${header}
    Status Should Be    200


Get Access To The API
    [Documentation]    Test that the weather API returns a status code of 200.
    #                  (This test definitely needs to be improved)
    ${weather_data}=    Get Helsinki Weather
    Should Not Be Empty    ${weather_data}