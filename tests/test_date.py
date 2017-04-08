"""Date tests"""

from alifesim.day import next_day
from alifesim import date
import datetime

def test_newday():
    today = datetime.date.today()
    date.today = today
    next_day()
    assert date.today == today+datetime.timedelta(1)
