"""Very basic tests like creating Player instance
"""

from alifesim.player import *
from alifesim import name, money, basic_stats

def test_new_player():
    player = Player()

def test_player_stats():
    player = Player()
    assert player.money == 0
    assert player.name == ''
    assert player.iq == 0
