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

from . import entity, relations
from .plan import WeekTime

@entity.component('course_payment')
class CoursePayment(float):
    pass

class Course(entity.Entity):
    components = {
        'course_payment',
        'name',
        'weekly',
    }

def evening_course(name, day):
    course = Course()
    course.name = name
    course.weekly.add(WeekTime(day, 1))
    return course

@entity.entity_filter('course_payment')
def all(_):
    return True

@entity.component('courses')
class HasCourses(set):
    pass

@relations.processor('plan')
def course_related(person, course):
    if not person.has_components('courses'):
        return False
    return course.name in person.courses
