import pytest
import datetime
from unittest.mock import patch
from utils.format_data import FormatData
from utils.location_weather import LocationWeather
from tests.fixtures import mock_data

def test_format_data(mock_data):
  mock_today = datetime.date(2024, 10, 30)

  # send mock date to the module
  with patch('datetime.date', autospec=True) as mock_date:
    mock_date.today.return_value = mock_today
    with patch('utils.location_weather.LocationWeather.location_weather', return_value=mock_data):
      format_data = FormatData().format_data()
      print(format_data)

  expected_output = [
    {'date': '30.10.2024', 'time': '09.00', 'temperature': 8.4, 'details': 'fair_day'},
    {'date': '31.10.2024', 'time': '12.00', 'temperature': 8.4, 'details': 'rainy'},
    {'date': '01.11.2024', 'time': '09.00', 'temperature': 8.4, 'details': 'weather details not found from the data'},
    {'date': '01.11.2024', 'time': '18.00', 'temperature': 8.4, 'details': 'sunny'},
    {'date': '02.11.2024', 'time': '00.00', 'temperature': 8.4, 'details': 'weather details not found from the data'}
  ]

  assert format_data == expected_output
  # check that the date 3.11.2024 is ignored to prove that the for loop has stopped when it should
  assert not any(r['date'] == '3.11.2024' for r in format_data)