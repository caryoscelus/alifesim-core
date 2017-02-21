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

"""Events & event hadlners
"""

import copy

class EventHandler(object):
    def __init__(self, f, tags):
        self.f = f
        self.tags = set(tags)
    def process(self, entity):
        if entity.tags >= self.tags:
            self.f(entity)

event_handlers = []

def register_event_handler(f, *tags):
    event_handlers.append(EventHandler(f, tags))

def event_handler(*tags):
    """Decorator, which registers event handler"""
    def wrapper(f):
        register_event_handler(f, *tags)
        return f
    return wrapper

class Event(object):
    tags = set()
    """Event, which processes attached reactors"""
    def proceed(self):
        for handler in event_handlers:
            handler.process(self)

def event_tags(*tags):
    def wrapper(cls):
        cls.tags = copy.copy(cls.tags)
        cls.tags.update(tags)
        return cls
    return wrapper
