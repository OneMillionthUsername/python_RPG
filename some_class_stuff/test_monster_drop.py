"""TEST monster health reset
"""

import unittest
from monster import Monster
from player import player

class Testing(unittest.TestCase):
    def test_health_reset_monster(self):
        enemy = Monster("Dean", "bird", 5)
        print('default health =', enemy.Health)
        enemy.Health -= 100
        print('-100 = ', enemy.Health)
        enemy.health_reset()
        self.assertEqual(enemy.Health, enemy.Health_default, print('result = ', enemy.Health))
    
    def test_health_reset_player(self):
        test_Player = player("Dean")
        print('default health =', test_Player.Health)
        test_Player.Health -= 100
        print('-100 = ', test_Player.Health)
        test_Player.health_reset()
        self.assertEqual(test_Player.Health, test_Player.Health_default, print(test_Player.Health))