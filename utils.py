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
    # convert data to a JSON formatted string
    data_str = json.dumps(data)
    # convert data into a python dictionary
    weather_data = json.loads(data_str)
    return weather_data
  else:
    raise Exception(f'failed to fetch content, response code {response.status_code}')

def get_weather_data():
  all_weather_data = get_helsinki_weather()
  weather_data_next_3_days = []
  day_after_tomorrow = datetime.date.today() + datetime.timedelta(2)

  for data in all_weather_data['properties']['timeseries']:
    # divide date and time into different strings
    date = data['time'].split('T')[0]
    time = data['time'].split('T')[1].split('Z')[0]
    temperature = data['data']['instant']['details']['air_temperature']

    if 'next_1_hours' in data['data']:
      details = data['data']['next_1_hours']['summary']['symbol_code']
    elif 'next_6_hours' in data['data']:
      details = data['data']['next_6_hours']['summary']['symbol_code']
    elif 'next_12_hours' in data['data']:
      details = data['data']['next_12_hours']['summary']['symbol_code']
    else:
      details = 'weather details not found from the data'

    # add only the data containing these times to the list
    if time == '09:00:00' or time == '12:00:00' or time == '18:00:00' or time == '00:00:00':
      formatted_date = date.split('-')
      formatted_date.reverse()

      formatted_time = time.split(':')

      weather_data_next_3_days.append({
        'date': formatted_date[0] + '.' + formatted_date[1] + '.' + formatted_date[2],
        'time': formatted_time[0] + '.' + formatted_time[1],
        'temperature': temperature,
        'details': details
      })

    # convert the date string into a datetime object for comparison
    date_obj = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    if date_obj > day_after_tomorrow:
      break

  return weather_data_next_3_days

def print_data():
  weather_data = get_weather_data()
  # track the current date
  current_date = None
  
  for data in weather_data: 
    if data['date'] != current_date:
      print(data['date'])
      current_date = data['date']

    print(' ', data['time'])
    print(' ', data['temperature'], '°C', end='')
    print('', data['details'])
    print('')