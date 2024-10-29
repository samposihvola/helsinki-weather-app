import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import get_helsinki_weather

def test_api_with_wrong_credentials(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 404
    
    mocker.patch('requests.get', return_value=mock_response)
    result = get_helsinki_weather()
    print(result)

    assert result == 'Exception: failed to fetch content, response code: 404'