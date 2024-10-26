*** Settings ***
Library    utils.py
Library    RequestsLibrary

*** Test Cases ***
API Returns Status Code 200
    # could you get user-agent & url variables from the code?
    ${header}    Create Dictionary    user-agent=https://github.com/samposihvola/helsinki-weather-app/tree/main
    ${response}    GET    url=https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=60.192059&lon=24.945831    headers=${header}
    Status Should Be    200

