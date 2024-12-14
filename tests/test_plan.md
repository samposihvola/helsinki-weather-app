# Test Plan

## API (Robot Framework)

- [x] Yr.no API returns status code 200
- [ ] OpenWeatherMap API returns status code 200

## E2E (Robot Framework)

- [ ] Add prompting to both tests
- [x] Code has access to API and returns correct data
- [x] App gives data for today & the following three days
- [x] Printed data is in correct form: {dd.mm.yyyy}, {hh.mm}
- [x] Prints times {09.00}, {12.00}, {18.00}, {00.00} tomorrow & day after
- [x] Prints degrees in Celcius and weather details (sunny, rainy, cloudy etc.)

## Unit tests (Pytest)

#### get_location

- [ ] Test prompting with three different locations around the world
- [ ] Test prompting with empty answers for both 'city' and 'country'
- [ ] Test prompting with empty answer for 'city' and a legit 'country' 
- [ ] Test prompting with a legit 'city' and an empty 'country'
- [ ] openweather.txt can be accessed
- [ ] Access 'failed to fetch content...' branch

#### location_weather
- [x] Access 'failed to fetch content...' branch

### weather_printer

#### format_data
- [x] If {symbol_code} is {next_1_hours}, adds correct detail 
- [x] If {symbol_code} is {next_6_hours}, adds correct detail 
- [x] Test {symbol_code} that is something else than mentioned above
- [x] Test time other than {09.00}, {12.00}, {18.00} or {00.00}
- [x] Should break the for-loop with a date bigger than {day_after_tomorrow}
- [x] Should not break the for-loop with a date smaller than or equal to {day_after_tomorrow}
  - This is verified in the previous unit tests

#### print_data
- [x] Prints the data in correct form and prints dates when it should