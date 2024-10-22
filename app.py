import requests
import json
import datetime

def get_helsinki_weather():
    # store contact info into a variable
    sitename = 'https://github.com/samposihvola/helsinki-weather-app/tree/main'
    # endpoint with helsinki coordinates
    url = 'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=60.192059&lon=24.945831'
    # create useragent object to be used as credentials for the API
    useragent = {
        'User-Agent': sitename
    }
    response = requests.get(url, headers=useragent)
    if response.status_code == 200:
        data = response.json()
        # convert data to a JSON formatted string with 4 spaces of intendation
        data_str = json.dumps(data, indent=4)
        return data_str
    else:
        print('failed to fetch content, response code:', response.status_code)

def get_days():
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(1)
    day_after_tomorrow = today + datetime.timedelta(2)
    # convert datetime objects into strings
    days = [str(today), str(tomorrow), str(day_after_tomorrow)]
    return days

if __name__ == '__main__':
    #get_helsinki_weather()
    print(get_days())