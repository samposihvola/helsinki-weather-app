import pytest
import sys
import os
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import get_helsinki_weather, get_weather_data

class TestUtils:
  # initialize mock data
  @classmethod
  def setup_class(cls):
     # construct the path to 'mock_data.json' relative to this file’s location
    file_path = os.path.join(os.path.dirname(__file__), 'mock_data.json')
    with open(file_path, 'r') as file:
      cls.mock_data = json.load(file)

  def test_get_helsinki_weather_error_branch(self, mocker):
    # create a mock response object with a 404 status code to simulate an error from the API
    mock_response = mocker.Mock()
    mock_response.status_code = 404
    # return the mock response instead of an actual HTTP request
    mocker.patch('requests.get', return_value=mock_response)

    # expect an exception due to the 404 response
    with pytest.raises(Exception) as excinfo:
      get_helsinki_weather()
    
    assert 'failed to fetch content, response code 404' in str(excinfo.value)

  def test_get_weather_data_details_branches(self, mocker):
    # create mock data for get_helsinki_weather function to return
    mocker.patch('utils.get_helsinki_weather', return_value=self.mock_data)
    result = get_weather_data()

    # test all the possible branches
    expected_result_30102024 = 'fair_day'
    expected_result_31102024 = 'rainy'
    expected_result_01112024 = 'sunny'
    expected_result_02112024 = 'weather details not found from the data'

    assert result[0]['details'] == expected_result_30102024
    assert result[1]['details'] == expected_result_31102024
    assert result[2]['details'] == expected_result_01112024
    assert result[3]['details'] == expected_result_02112024

  def test_get_weather_data_time_branches(self, mocker):
    mocker.patch('utils.get_helsinki_weather', return_value=self.mock_data)
    result = get_weather_data()

    # test all the possible branches
    expected_result_30102024 = '09.00'
    expected_result_31102024 = '12.00'
    expected_result_01112024 = '18.00'
    expected_result_02112024 = '00.00'
    expected_result_03112024 = '01.00'

    assert result[0]['time'] == expected_result_30102024
    assert result[1]['time'] == expected_result_31102024
    assert result[2]['time'] == expected_result_01112024
    assert result[3]['time'] == expected_result_02112024

    # assert that '01.00' is not found in any 'time' field in result
    assert all(entry['time'] != expected_result_03112024 for entry in result)