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

"""Day cycle
"""

from . import event

@event.tags('day_end')
class DayEnd(event.Event):
    pass

@event.tags('time')
class TimeTick(event.Event):
    pass

def next_day():
    DayEnd().proceed()

def tick():
    TimeTick().proceed()

on_day_end = event.handler('day_end')
on_time_tick = event.handler('time')
