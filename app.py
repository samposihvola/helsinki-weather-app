import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'utils/')))
from weather_printer import WeatherPrinter

if __name__ == '__main__':
  weather_printer = WeatherPrinter()
  weather_printer.print_data()