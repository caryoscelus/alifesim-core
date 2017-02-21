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

"""Test pickling/unpicklling
"""

import pickle

from alifesim.player import *
from alifesim import entity
from alifesim.name import get_by_name

def test_pickle_player():
    player = Player()
    player.name = 'Name'
    sp = pickle.dumps(player, protocol=pickle.HIGHEST_PROTOCOL)
    #entity.entities.clear()
    del entity.entities[:]
    player = pickle.loads(sp)
    assert player == get_by_name('Name')
