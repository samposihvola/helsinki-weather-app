import datetime
import requests
import json

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
    # convert data into a python dictionary
    weather_data = json.loads(data_str)
    return weather_data
  else:
    print('failed to fetch content, response code:', response.status_code)

def get_weather_data():
  all_weather_data = get_helsinki_weather()
  weather_data_next_3_days = []
  day_after_tomorrow = datetime.date.today() + datetime.timedelta(2)

  for info in all_weather_data['properties']['timeseries']:
    # divide date and time into different strings
    date = info['time'].split('T')[0]
    time = info['time'].split('T')[1].split('Z')[0]
    temperature = info['data']['instant']['details']['air_temperature']

    if 'next_1_hours' in info['data']:
      details = info['data']['next_1_hours']['summary']['symbol_code']
    if 'next_6_hours' in info['data']:
      details = info['data']['next_6_hours']['summary']['symbol_code']

    if time == '09:00:00' or time == '15:00:00' or time == '21:00:00':
      date = date.split('-')
      date.reverse()
      weather_data_next_3_days.append({
        'date': date[0] + '.' + date[1] + '.' + date[2],
        'time': time,
        'temperature': temperature,
        'details': details
      })

    # 9pm day after tomorrow is the last info we need
    # convert datetime object into string
    if date == str(day_after_tomorrow) and time == '21:00:00':
      break

  return weather_data_next_3_days

def format_days():
  weather_data = get_weather_data()
  print(weather_data)

def print_data():
  weather_data = get_weather_data()
  
  for info in weather_data:
    print(info['date'], '', end='')
    print(info['time'])
    print(info['temperature'], '°C')
    print(info['details'])
    print('')

if __name__ == '__main__':
  format_days()