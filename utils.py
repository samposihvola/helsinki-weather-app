import datetime
from weather import get_helsinki_weather

def get_days():
  today = datetime.date.today()
  tomorrow = today + datetime.timedelta(1)
  day_after_tomorrow = today + datetime.timedelta(2)
  # convert datetime objects into strings
  days = [str(today), str(tomorrow), str(day_after_tomorrow)]
  return days

def get_correct_data():
  days = get_days()
  all_weather_data = get_helsinki_weather()
  weather_data_next_3_days = []

  for info in all_weather_data['properties']['timeseries']:
    # divide date and time into different strings
    date = info['time'].split('T')[0]
    time = info['time'].split('T')[1].split('Z')[0]
    temperature = info['data']['instant']['details']['air_temperature']
    details = info['data']['next_1_hours']['summary']['symbol_code']

    if time == '09:00:00' or time == '15:00:00' or time == '21:00:00':
      weather_data_next_3_days.append({
        'date': date,
        'time': time,
        'temperature': temperature,
        'details': details
      })

    # 9pm day after tomorrow is the last info we need
    if date == days[2] and time == '21:00:00':
      break

  return weather_data_next_3_days

def format_data():
  weather_data = get_correct_data()
  print(weather_data)

if __name__ == '__main__':
  format_data()