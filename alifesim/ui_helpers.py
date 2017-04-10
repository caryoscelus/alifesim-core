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

"""Ui helpers
"""

class Selection(list):
    def __init__(self, min_, max_):
        super(Selection, self).__init__()
        self.min = min_
        self.max = max_
    def append(self, element):
        if len(self) >= self.max:
            return
        super(Selection, self).append(element)
    def ready(self):
        return self.min <= len(self) <= self.max

class SelectionManager(object):
    def __init__(self):
        self.selection = None
        self.selection_processor = None
    def new(self, min, max):
        self.selection = Selection(min, max)
        return self.selection
    def can_select(self):
        return self.selection is not None and self.selection_processor
    def select(self, what):
        if what not in self.selection:
            self.selection.append(what)
        print(self.selection)
    def deselect(self, what):
        if what in self.selection:
            self.selection.remove(what)
    def set_processor(self, f):
        self.selection_processor = f
        # return ??
    def process(self):
        self.selection_processor(*self.selection)

selection_manager = SelectionManager()

def show_screen(name, *args, **kwargs):
    """Show given screen with args.

    Currently this function has to be explicitly overridden by UI implementation.
    """
    raise RuntimeError('Show screen not provided')
