import pytest
from unittest.mock import patch
from utils.print_data import PrintData
from utils.format_data import FormatData
from tests.fixtures import mock_formatted_data

def test_print_data(mock_formatted_data, capsys):
  # mock FormatData.format_data to return mock data
  with patch.object(FormatData, 'format_data', return_value=mock_formatted_data):
      # mock LocationWeather to avoid calling GetLocation
      with patch('utils.format_data.LocationWeather.location_weather', return_value=None):
          # mock GetLocation to prevent user input
          with patch('utils.location_weather.GetLocation.get_location', return_value={'latitude': 0, 'longitude': 0}):
              # run the function
              PrintData().print_data()

  # capture the printed output
  captured = capsys.readouterr()
  
  expected_lines = [
    '30.10.2024',
    '  09.00',
    '  8.4 °C fair_day',
    '',
    '31.10.2024',
    '  12.00',
    '  8.4 °C rainy',
    '',
    '01.11.2024',
    '  09.00',
    '  8.4 °C weather details not found from the data',
    '',
    '  18.00',
    '  8.4 °C sunny',
    '',
    '02.11.2024',
    '  00.00',
    '  8.4 °C weather details not found from the data',
    '',
  ]

  # check that each expected line is included in the output
  for line in expected_lines:
    assert line in captured.out