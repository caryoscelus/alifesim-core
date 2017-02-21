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

"""Playground - test-related code
"""

from .person import Person
from .friends import make_friends
from . import ui_helpers

def setup_friends(player):
    player.name = 'Mee Mines'
    friend_names = [
        'Frie Ends',
        'Clou Sefri',
    ]
    for name in friend_names:
        friend = Person()
        friend.name = name
        make_friends(player, friend)

class EatCake(object):
    name = "Eat Cake"
    people_min = 1
    people_max = 3
    @classmethod
    def make_and_run(cls, *people):
        self = cls(people)
        self.proceed()

    def __init__(self, *people):
        self.people = people

    def proceed(self):
        ## event?
        ui_helpers.show_screen('cake')
