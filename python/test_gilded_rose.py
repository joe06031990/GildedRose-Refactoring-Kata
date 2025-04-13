# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        # Arrange: Create one item
        items = [Item("foo", 10, 20)]
        gilded_rose = GildedRose(items)

        # Act: Update quality
        gilded_rose.update_quality()

        # Assert: Name remains the same, quality and sell_in should be decreased by 1
        self.assertEqual("foo", items[0].name)         # Name should not change
        self.assertEqual(9, items[0].sell_in)          # sell_in decreases by 1
        self.assertEqual(19, items[0].quality)         # quality decreases by 1

        
if __name__ == '__main__':
    unittest.main()
