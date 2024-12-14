import pytest
import json
import os

from utils.get_location import GetLocation
from utils.location_weather import LocationWeather

# initialize mock data
@pytest.fixture
def mock_data(mocker):
  file_path = os.path.join(os.path.dirname(__file__), 'mock_data.json')
  with open(file_path, 'r') as file:
    mock_data = json.load(file)

  # create mock data for location_weather
  mocker.patch('utils.location_weather.LocationWeather.location_weather', return_value=mock_data)
  # call get_weather_data after mocking
  return LocationWeather.location_weather()

@pytest.fixture
def mock_location(mocker):
  # create mock location info
  mocker.patch('utils.get_location.GetLocation.get_location', return_value={
    'latitude': '60.1674881',
    'longitude': '24.9427473'
  })

  return GetLocation.get_location()
