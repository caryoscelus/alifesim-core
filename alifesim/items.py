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

"""Items & price"""

from . import entity
from . import relations
from . import name, plan
from .entity import Entity
from .plan import WeekTime

@entity.component('price')
class Price(float):
    pass

class Item(entity.Entity):
    components = {
        'name',
        'price',
    }

def make(name, price):
    item = Item()
    item.name = name
    item.price = price
    return item

@entity.entity_filter('price')
def all(_):
    return True
