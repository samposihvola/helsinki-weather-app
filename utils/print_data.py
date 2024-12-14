from utils.format_data import FormatData

# as the name implies, this module prints the formatted data to the command line

class PrintData:
  def __init__(self):
    self.formatted_data = FormatData().format_weather_data

  def print_data(self):
    weather_data = self.formatted_data()
    if not weather_data:
      print('No weather data available.')
      return
    
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
