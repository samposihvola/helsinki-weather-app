import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import utils

class GetHelsinkiWeather:
  def __init__(self):
     self.x = x
  def access_api_with_wrong_credentials(self):
    print(utils.get_helsinki_weather())

if __name__ == '__main__':
    GetHelsinkiWeather.access_api_with_wrong_credentials('x')