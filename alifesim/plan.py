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

from . import entity, relations, date

@entity.component('weekly')
class Weekly(set):
    pass

def get_all_weekly_on(person, time):
    wtime = date.to_week_time(time)
    return entity.entity_filter('weekly')(lambda x: relations.related(person, x, 'plan') and wtime in x.weekly)()

def get_plan(person, time):
    return get_all_weekly_on(person, time)
