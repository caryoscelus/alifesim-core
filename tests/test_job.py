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

"""Test job
"""

from alifesim.job import normal_job
from alifesim.person import Person
from alifesim.relations import related

boring_job = normal_job('A boring job')
fun_job = normal_job('A fun job')

def test_job_related():
    person = Person()
    assert not related(person, boring_job, 'plan')
    person.job = boring_job.name
    assert related(person, boring_job, 'plan')
    assert not related(person, fun_job, 'plan')
    person.job = fun_job.name
    assert not related(person, boring_job, 'plan')
    assert related(person, fun_job, 'plan')
