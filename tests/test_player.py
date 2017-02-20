"""Very basic tests like creating Player instance
"""

import pytest

from alifesim.player import *
from alifesim import name, money, basic_stats

def test_new_player():
    player = Player()

def test_player_stats():
    player = Player()
    assert player.money == 0
    assert player.name == ''
    assert player.iq == 0

def test_list_stats():
    ## TODO: move to stat tests
    from alifesim.stat import get_stats
    player = Player()
    player_stats = get_stats(player)
    assert player_stats.keys() == { 'iq', 'energy' }

def test_set_stat():
    from alifesim.money import Money
    player = Player()
    player.money = 10
    assert isinstance(player.money, Money)

def test_extend():
    from alifesim import entity
    player = Player()
    with pytest.raises(AttributeError):
        player.foo
    Player.add_components('foo')
    with pytest.raises(AttributeError):
        player.foo
    entity.register_component('foo', str)
    assert player.foo == ''
