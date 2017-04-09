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

"""Day planning"""

import datetime

from . import entity
from . import relations

class WeekTime(object):
    def __init__(self, weekday=0, slot=0):
        self.weekday = weekday
        self.slot = slot

class RealTime(object):
    def __init__(self, date, slot=0):
        self.date = date
        self.slot = slot

def to_week_time(time):
    if isinstance(time, WeekTime):
        return time
    return WeekTime(time.date.weekday(), time.slot)

@entity.component('weekly')
class Weekly(set):
    pass

def get_all_weekly_on(person, time):
    wtime = to_week_time(time)
    return entity.entity_filter('weekly')(lambda x: relations.related(person, x) and wtime in x.weekly)

def get_plan(time):
    return get_all_weekly_on(time)
