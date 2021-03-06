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

"""Friends component
"""

from . import entity

class Friends(list):
    pass

entity.register_component('friends', Friends)

def make_friends(a, b):
    if b.name not in a.friends:
        a.friends.append(b.name)
    if a.name not in b.friends:
        b.friends.append(a.name)

def remove_friends(a, b):
    if b.name in a.friends:
        a.friends.remove(b.name)
    if a.name in b.friends:
        b.friends.remove(a.name)
