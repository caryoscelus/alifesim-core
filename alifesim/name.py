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

from . import entity

class Name(str):
    pass

entity.register_component('name', Name)

def get_by_name(name):
    named = entity.entity_filter('name')(lambda x: x.name == name)()
    if len(named) > 1:
        raise NameLookupError('More than one entity named "{}"'.format(name))
    if len(named) == 0:
        raise NameLookupError('No entity named "{}"'.format(name))
    return named[0]

class NameLookupError(RuntimeError):
    pass
