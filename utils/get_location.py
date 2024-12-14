import requests
import json
import os

# this module is responsible for prompting the user for wanted location
# and returning the coordinates for location_weather module to use

class GetLocation:
  def __init__(self):
    self.api_key = self._load_api_key()

  def _load_api_key(self):
    api_key_path = os.path.join(os.path.dirname(__file__), '../resources/openweather.txt')
    try:
      with open (api_key_path, 'r') as file:
        api_key = file.read()
      return api_key
    except FileNotFoundError:
      raise FileNotFoundError('API key not found')

  def get_location(self):
    # get location coordinates from the openweathermap geocoding API
    city = input('city: ')
    country = input('country: ')
      
    location_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city},{country}&appid={self.api_key}'
    response = requests.get(location_url)
    
    if response.status_code == 200:
      data = response.json()
      # convert data to a JSON formatted string
      data_str = json.dumps(data)
      # convert data into a python dictionary
      location_data = json.loads(data_str)
      coordinates = {
        'latitude': location_data[0]['lat'],
        'longitude': location_data[0]['lon']
      }
      if not coordinates['latitude'] or not coordinates['longitude']:
        raise ValueError('invalid coordinates received')
    else:
      raise Exception(f'failed to fetch content, response code {response.status_code}')
    
    return coordinates