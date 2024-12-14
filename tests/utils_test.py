import pytest
import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.format_data import *

# initialize mock data
@pytest.fixture
def mock_data(mocker):
  file_path = os.path.join(os.path.dirname(__file__), 'mock_data.json')
  with open(file_path, 'r') as file:
    mock_data = json.load(file)

  # create mock data for get_helsinki_weather function to return
  mocker.patch('utils.get_location_weather', return_value=mock_data)
  # call get_weather_data after mocking
  return format_weather_data()

def mock_location(mocker):
  # create mock location info
  mocker.patch('utils.get_location', return_value={
    'latitude': '60.1674881',
    'longitude': '24.9427473'
  })

  return get_location()

class TestUtils:
  def test_get_helsinki_weather_error_branch(self, mocker):#, mock_location):
    # create a mock response object with a 404 status code to simulate an error from the API
    mock_response = mocker.Mock()
    mock_response.status_code = 404
    # return the mock response instead of an actual HTTP request
    mocker.patch('requests.get', return_value=mock_response)

    # expect an exception due to the 404 response
    with pytest.raises(Exception) as excinfo:
      get_location_weather()
    
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

  def test_print_data(self, mock_data, mocker, capsys):
    mocker.patch('utils.print_data', return_value=mock_data)
    print_data()
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