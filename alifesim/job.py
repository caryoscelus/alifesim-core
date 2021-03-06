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

from . import entity, event, relations
from . import name, plan, day
from .entity import Entity
from .event import Event
from .date import WeekTime

@entity.component('payment')
class Payment(float):
    pass

class Job(Entity):
    components = {
        'payment',
        'name',
        'weekly',
        'event',
    }

@entity.entity_filter('payment')
def all_jobs(_):
    return True

@event.tags('job', 'tick')
class JobEvent(Event):
    def __init__(self, job):
        self.job = job

def normal_job(name):
    job = Job()
    job.name = name
    job.weekly = {
        WeekTime(d, 0) for d in range(5)
    }
    job.event = JobEvent(job)
    return job

@entity.component('job')
class HasJob(str):
    pass

@relations.processor('plan')
def job_related(person, job):
    return person.job == job.name
