import datetime

def get_days():
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(1)
    day_after_tomorrow = today + datetime.timedelta(2)
    # convert datetime objects into strings
    days = [str(today), str(tomorrow), str(day_after_tomorrow)]
    return days