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

"""Player character entity
"""

from . import entity
from .entity import Entity

@entity.component('player')
class PlayerComponent(object):
    pass

class Player(Entity):
    components = {
        'player',
        'name',

        'money',

        'iq',
        'energy',

        'job',
        'courses',
        'friends',
        'items',
    }

class PlayerError(RuntimeError):
    pass

def get():
    all = entity.entity_filter('player')()()
    if len(all) == 0:
        raise PlayerError('No player found')
    elif len(all) > 1:
        raise PlayerError('More than one player')
    return all[0]
