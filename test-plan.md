E2E

- API returns status code 200
- App gives data for today, tomorrow & day after tomorrow
- Printed data is in correct form: {dd.mm.yyyy}, {hh.mm}
- Prints times {09.00}, {12.00}, {18.00}, {00.00} tomorrow & day after
- Prints degrees in Celcius and weather details (sunny, rainy, cloudy etc.)

Unit tests

[Branch coverage: 100%]

- API returns correct data in JSON
- Prints 'failed to fetch content...' with status code when API is accessed with wrong credentials
- Prints 'failed to fetch content...' with status code when accessing a wrong url