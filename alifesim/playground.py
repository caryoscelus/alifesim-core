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
from .socialize import Socialize
from .event import event_tags, event_handler
from . import job
from . import ui_helpers
from . import entity
from random import random

@entity.component('satiation')
class satiation(float):
    pass
Person.components.add('satiation')

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

@event_tags('eat_cake')
class EatCake(Socialize):
    name = "Eat Cake"
    people_min = 1
    people_max = 3

@event_handler('eat_cake')
def eat_cake_screen(event):
    ui_helpers.show_screen('cake')

@event_handler('eat_cake')
def eat_cake_special(event):
    print(event.people)
    if random() < 0.5:
        ui_helpers.show_screen('cake_special', event.people[0])

@event_handler('eat_cake')
def eat_cake_satiation(event):
    for person in event.people:
        person.satiation += 1


def get_a_job(person):
    ajob = job.normal_job('A boring job')
    person.job = ajob.name
