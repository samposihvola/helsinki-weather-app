import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import get_helsinki_weather

def test_get_helsinki_weather_error_branch(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 404    
    mocker.patch('requests.get', return_value=mock_response)

    with pytest.raises(Exception) as excinfo:
      get_helsinki_weather()
    
    assert 'failed to fetch content, response code 404' in str(excinfo.value)

def test_get_weather_data_next_1_hours_branch(mocker):
  mock_data =  {
    "properties": {
      "timeseries": [{
        "time": "2024-10-30T07:00:00Z",
        "data": {
          "instant": {
            "details": {
              "air_temperature": 8.4,
            }
          },
          "next_1_hours": {
              "summary": {
              "symbol_code": "fair_day"
              },
              "details": {
              "precipitation_amount": 0
              }
          },
        }
      }]
    }
  }