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

"""Entity
"""

components = {}

def register_component(name, constructor):
    components[name] = constructor

entities = []

class Entity(object):
    def __new__(cls, *args, **kwargs):
        instance = super(Entity, cls).__new__(cls, *args, **kwargs)
        entities.append(instance)
        return instance

    def __getattr__(self, name):
        if name == '_components':
            self._components = {}
            return self._components
        if name in self.__class__.components:
            if name not in components:
                raise AttributeError('Component is not registered: {}'.format(name))
            if name not in self._components:
                self._components[name] = components[name]()
            return self._components[name]
        raise AttributeError('No such attribute or component: {}'.format(name))

    def __setattr__(self, name, value):
        if name in self.__class__.components:
            self._components[name] = components[name](value)
            return
        super(Entity, self).__setattr__(name, value)

    def has_components(self, *comps):
        for comp in comps:
            if comp not in self.__class__.components:
                return False
        return True

    @classmethod
    def add_components(cls, *comps):
        """Add components to this entity"""
        cls.components.update(comps)

def entity_processor(*req_comps):
    def wrapper(f):
        def _f():
            for entity in entities:
                if entity.has_components(*req_comps):
                    f(entity)
        return _f
    return wrapper

def entity_filter(*comps):
    def wrapper(f):
        def _f():
            return [
                entity
                    for entity in entities
                        if entity.has_components(*comps) and f(entity)
            ]
        return _f
    return wrapper

class ComponentNotFound(RuntimeError):
    pass
