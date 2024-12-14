import requests
import json
from utils.get_location import GetLocation

# this module gets the correct coordinates from get_location module
# sends them to yr.no API and saves the fetched data in JSON

class LocationWeather:
  def __init__(self):
    self.location = GetLocation().get_location
    self.sitename = 'https://github.com/samposihvola/helsinki-weather-app/tree/main'

  def get_weather(self):
    coordinates = self.location()
    latitude = coordinates['latitude']
    longitude = coordinates['longitude']

    # weather API url with coordinates
    url = f'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={latitude}&lon={longitude}'
    # create useragent object for the API credentials
    useragent = {
      'User-Agent': self.sitename
    }
    response = requests.get(url, headers=useragent)
    
    if response.status_code == 200:
      data = response.json()
      data_str = json.dumps(data)
      weather_data = json.loads(data_str)
      return weather_data
    else:
      raise Exception(f'failed to fetch content, response code {response.status_code}')