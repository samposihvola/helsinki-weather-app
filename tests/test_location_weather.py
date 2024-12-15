import pytest
from unittest.mock import patch
from utils.location_weather import LocationWeather

def test_get_weather_error_branch(mocker):
  with patch('utils.location_weather.GetLocation.get_location', return_value={'latitude': 0, 'longitude': 0}):
    # create a mock response object with a 404 status code to simulate an error from the API
    mock_response = mocker.Mock()
    mock_response.status_code = 404
    # return the mock response instead of an actual HTTP request
    mocker.patch('requests.get', return_value=mock_response)

    # expect an exception due to the 404 response
    with pytest.raises(Exception) as excinfo:
      LocationWeather().location_weather()
    
    assert 'failed to fetch content, response code 404' in str(excinfo.value)