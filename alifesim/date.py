##
##  Copyright (C) 2017 caryoscelus
##
##  This program is free software: you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation, either version 3 of the License, or
##  (at your option) any later version.
##
##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.
##
##  You should have received a copy of the GNU General Public License
##  along with this program.  If not, see <http://www.gnu.org/licenses/>.
##

"""Date"""

import datetime

from . import day

DAY_SLOTS = 2

class WeekTime(object):
    def __init__(self, weekday=0, slot=0):
        self.weekday = weekday
        self.slot = slot
    def __eq__(self, other):
        return self.weekday == other.weekday and self.slot == other.slot
    def __hash__(self):
        return hash(self.weekday*256+self.slot)

class RealTime(object):
    def __init__(self, date, slot=0):
        self.date = date
        self.slot = slot
    def tick(self):
        self.slot += 1
        if self.slot >= DAY_SLOTS:
            self.slot = 0
            self.date += datetime.timedelta(1)
            return True
        return False

def to_week_time(time):
    if isinstance(time, WeekTime):
        return time
    return WeekTime(time.date.weekday(), time.slot)

today = RealTime(datetime.date.today())

@day.on_time_tick
def update_time(event):
    if today.tick():
        day.next_day()
