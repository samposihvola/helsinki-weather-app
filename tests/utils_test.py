import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tests.fixtures import *
from utils.format_data import FormatData
from utils.get_location import GetLocation
from utils.location_weather import LocationWeather


class TestUtils:
  def test_get_weather_error_branch(self, mocker):
    # create a mock response object with a 404 status code to simulate an error from the API
    mock_response = mocker.Mock()
    mock_response.status_code = 404
    # return the mock response instead of an actual HTTP request
    mocker.patch('requests.get', return_value=mock_response)

    # expect an exception due to the 404 response
    with pytest.raises(Exception) as excinfo:
      LocationWeather().location_weather()
    
    assert 'failed to fetch content, response code 404' in str(excinfo.value)

  def test_get_weather_data_details_branches(self, mock_data):
    # test all the possible branches
    expected_result_30102024 = 'fair_day'
    expected_result_31102024 = 'rainy'
    expected_result_01112024_1 = 'weather details not found from the data'
    expected_result_01112024_2 = 'sunny'
    expected_result_02112024 = 'weather details not found from the data'

    assert mock_data[0]['details'] == expected_result_30102024
    assert mock_data[1]['details'] == expected_result_31102024
    assert mock_data[2]['details'] == expected_result_01112024_1
    assert mock_data[3]['details'] == expected_result_01112024_2
    assert mock_data[4]['details'] == expected_result_02112024

  def test_get_weather_data_time_branches(self, mock_data):
    # test all the possible branches
    expected_result_30102024 = '09.00'
    expected_result_31102024 = '12.00'
    expected_result_01112024_1 = '09.00'
    expected_result_01112024_2 = '18.00'
    expected_result_02112024 = '00.00'
    expected_result_03112024 = '01.00'

    assert mock_data[0]['time'] == expected_result_30102024
    assert mock_data[1]['time'] == expected_result_31102024
    assert mock_data[2]['time'] == expected_result_01112024_1
    assert mock_data[3]['time'] == expected_result_01112024_2
    assert mock_data[4]['time'] == expected_result_02112024

    # assert that '01.00' is not found in any 'time' field in mock_data
    assert all(entry['time'] != expected_result_03112024 for entry in mock_data)

  def test_get_weather_data_for_loop(self, mock_data):
    assert len(mock_data) == 6
    # check that the date 4.11.2024 is ignored to prove that the for loop has stopped when it should
    assert not any(r['date'] == '4.11.2024' for r in mock_data)