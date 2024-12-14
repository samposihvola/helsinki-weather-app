*** Settings ***
Library    RequestsLibrary
Library    OperatingSystem

*** Variables ***
${API_KEY_FILE}    utils/openweather.txt

*** Test Cases ***
OpenWeather API Returns Status Code 200
    ${OpenWeatherAPIKey}    Get File    ${API_KEY_FILE}
    ${response}    GET    url=http://api.openweathermap.org/geo/1.0/direct?q=helsinki,finland&appid=${OpenWeatherAPIKey}
    Status Should Be    200 

Yr.no API Returns Status Code 200
    ${header}    Create Dictionary    user-agent=https://github.com/samposihvola/helsinki-weather-app/tree/main
    ${response}    GET    url=https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=60.192059&lon=24.945831    headers=${header}
    Status Should Be    200