import pytest
import json
import os

from utils.get_location import GetLocation
from utils.location_weather import LocationWeather

@pytest.fixture
def mock_data():
  file_path = os.path.join(os.path.dirname(__file__), 'mock_data.json')
  with open(file_path, 'r') as file:
    mock_data = json.load(file)

  return mock_data

@pytest.fixture
def mock_location(mocker):
  mocker.patch('utils.get_location.GetLocation.get_location', return_value={
    'latitude': '60.1674881',
    'longitude': '24.9427473'
  })

  return GetLocation().get_location()

@pytest.fixture
def mock_formatted_data():
  return [
    {'date': '30.10.2024', 'time': '09.00', 'temperature': 8.4, 'details': 'fair_day'},
    {'date': '31.10.2024', 'time': '12.00', 'temperature': 8.4, 'details': 'rainy'},
    {'date': '01.11.2024', 'time': '09.00', 'temperature': 8.4, 'details': 'weather details not found from the data'},
    {'date': '01.11.2024', 'time': '18.00', 'temperature': 8.4, 'details': 'sunny'},
    {'date': '02.11.2024', 'time': '00.00', 'temperature': 8.4, 'details': 'weather details not found from the data'}
  ]

@pytest.fixture
def mock_api_key(mocker):
  # mock the API key to prevent reading from a file
  mocker.patch('utils.get_location.GetLocation._load_api_key', return_value='test_api_key')