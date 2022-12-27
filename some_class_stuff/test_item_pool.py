"""TESTINT item pool and drop chance
"""
import item
import unittest

class Testing(unittest.TestCase):
    def test_count(self):
        item.item_pool_init()
        count = len(item.pool)
        self.assertGreater(count, 0, print('items in pool =', count))
        
    def test_drop(self):
        self.assertLess(item.Drop_factor(), 51, print('possible chance for an item to drop =', item.Drop_factor()))