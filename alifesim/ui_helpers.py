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

selection = None
selection_processor = None

def new_selection(min_, max_):
    global selection
    selection = Selection(min_, max_)
    return selection

def can_select():
    return selection is not None

def select(what):
    if what not in selection:
        selection.append(what)

def deselect(what):
    if what in selection:
        selection.remove(what)

def set_selection_processor(f):
    global selection_processor
    selection_processor = f
    # return ??

def process_selection():
    selection_processor(*selection)

def show_screen(name, *args, **kwargs):
    """Show given screen with args.

    Currently this function has to be explicitly overridden by UI implementation.
    """
    raise RuntimeError('Show screen not provided')
