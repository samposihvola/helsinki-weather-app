import pytest
import sys
import os
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import get_helsinki_weather, get_weather_data

def test_get_helsinki_weather_error_branch(mocker):
  # create a mock response object with a 404 status code to simulate an error from the API
  mock_response = mocker.Mock()
  mock_response.status_code = 404
  # return the mock response instead of an actual HTTP request
  mocker.patch('requests.get', return_value=mock_response)

  # expect an exception due to the 404 response
  with pytest.raises(Exception) as excinfo:
    get_helsinki_weather()
  
  assert 'failed to fetch content, response code 404' in str(excinfo.value)

def test_get_weather_data_next_1_hours_branch(mocker):
  with open('mock_data.json', 'r') as file:
     mock_data = json.load(file)

  # create mock data for get_helsinki_weather function to return
  mocker.patch('utils.get_helsinki_weather', return_value=mock_data)

  result = get_weather_data()
  # expect the result to be the symbol_code in the mock_data.json file under 'next_1_hours'
  expected_result = 'fair_day'
  assert result[0]['details'] == expected_result