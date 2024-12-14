import datetime
from utils.location_weather import LocationWeather 

# responsible for tidying up the json data

class FormatData:
  def __init__(self):
    self.weather_data = LocationWeather().get_weather()
    self.times = ['09:00:00', '12:00:00', '18:00:00', '00:00:00']

  def format_weather_data(self):
    weather_data_next_3_days = []
    day_after_tomorrow = datetime.date.today() + datetime.timedelta(2)

    for data in self.weather_data['properties']['timeseries']:
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
      if time in self.times:
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