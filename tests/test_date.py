"""Date tests"""

from alifesim import day, date
import datetime

def test_newday():
    today = date.today.date
    day.tick()
    day.tick()
    assert date.today.date == today+datetime.timedelta(1)
