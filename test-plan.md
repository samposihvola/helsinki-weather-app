# Test Plan

## E2E (Robot Framework)

- [x] API returns status code 200
- [ ] App gives data for today, tomorrow & day after tomorrow
- [ ] Printed data is in correct form: {dd.mm.yyyy}, {hh.mm}
- [ ] Prints times {09.00}, {12.00}, {18.00}, {00.00} tomorrow & day after
- [ ] Prints degrees in Celcius and weather details (sunny, rainy, cloudy etc.)

## Unit tests (Python)

### utils.py

- Measure the branch coverage with coverage.py?

#### get_helsinki_weather
- [ ] API returns correct data in JSON
- [ ] Prints 'failed to fetch content...' with status code when API is accessed with wrong credentials
- [ ] Prints 'failed to fetch content...' with status code when accessing a wrong url

#### get_weather_data
- [ ] If {symbol_code} is {next_1_hours}, adds correct detail 
- [ ] If {symbol_code} is {next_6_hours}, adds correct detail 
- [ ] Test {symbol_code} that is something else than mentioned above
- [ ] Test time other than {09.00}, {12.00}, {18.00} or {00.00}
- [ ] Should break the for-loop with a date bigger than {day_after_tomorrow}
- [ ] Should not break the for-loop with a date smaller than or equal to {day_after_tomorrow}

#### print_data
- [ ] Prints date when {data['time']} is {00.00}
- [ ] Does not print date when {data['time']} is something else
- [ ] Prints {time}, {temperature} and {details} when date is printed
- [ ] Prints {time}, {temperature} and {details} when date is not printed