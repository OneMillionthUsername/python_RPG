"""TESTINT item pool and drop chance
"""

import item_pool
import unittest

class Testing(unittest.TestCase):
    def test_count(self):
        item_pool.item_pool_init()
        count = len(item_pool.pool)
        self.assertGreater(count, 0, print('items in pool =', count))
        
    def test_drop(self):
        self.assertLess(item_pool.Drop_factor(), 51, print('possible chance for an item to drop =', item_pool.Drop_factor()))