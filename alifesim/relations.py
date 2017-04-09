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

"""Relations between entities"""

from . import entity

relation_processors = []

def generic_processor(f):
    relation_processors.append(f)
    return f

def processor(relation):
    def decorator(f):
        def wrap(a, b, rel):
            if rel != relation:
                return False
            return f(a, b)
        relation_processors.append(wrap)
        return wrap
    return decorator

def related(a, b, relation):
    for processor in relation_processors:
        if processor(a, b, relation):
            return True
    return False
