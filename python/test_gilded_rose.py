import unittest
from gilded_rose import GildedRose, Item

class GildedRoseTest(unittest.TestCase):

    def test_regular_item_before_sell_date(self):
        item = Item("Elixir of the Mongoose", sell_in=5, quality=10)
        GildedRose([item]).update_quality()
        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 9)

    def test_regular_item_after_sell_date(self):
        item = Item("Elixir of the Mongoose", sell_in=0, quality=10)
        GildedRose([item]).update_quality()
        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 8)

    def test_quality_never_negative(self):
        item = Item("Elixir of the Mongoose", sell_in=5, quality=0)
        GildedRose([item]).update_quality()
        self.assertEqual(item.quality, 0)

    def test_aged_brie_increases_quality(self):
        item = Item("Aged Brie", sell_in=2, quality=0)
        GildedRose([item]).update_quality()
        self.assertEqual(item.quality, 1)

    def test_aged_brie_doubles_quality_after_sell_date(self):
        item = Item("Aged Brie", sell_in=0, quality=0)
        GildedRose([item]).update_quality()
        self.assertEqual(item.quality, 2)

    def test_quality_never_exceeds_50(self):
        item = Item("Aged Brie", sell_in=2, quality=49)
        GildedRose([item]).update_quality()
        self.assertEqual(item.quality, 50)

    def test_sulfuras_never_changes(self):
        item = Item("Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)
        GildedRose([item]).update_quality()
        self.assertEqual(item.sell_in, 0)
        self.assertEqual(item.quality, 80)

    def test_backstage_passes_increase_by_1(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)
        GildedRose([item]).update_quality()
        self.assertEqual(item.quality, 21)

    def test_backstage_passes_increase_by_2(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=20)
        GildedRose([item]).update_quality()
        self.assertEqual(item.quality, 22)

    def test_backstage_passes_increase_by_3(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=20)
        GildedRose([item]).update_quality()
        self.assertEqual(item.quality, 23)

    def test_backstage_passes_drop_to_0_after_concert(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=20)
        GildedRose([item]).update_quality()
        self.assertEqual(item.quality, 0)

    def test_conjured_item_degrades_twice_as_fast(self):
        item = Item("Conjured Mana Cake", sell_in=3, quality=6)
        GildedRose([item]).update_quality()
        self.assertEqual(item.quality, 4)

    def test_conjured_item_degrades_even_faster_after_sell_date(self):
        item = Item("Conjured Mana Cake", sell_in=0, quality=6)
        GildedRose([item]).update_quality()
        self.assertEqual(item.quality, 2)

    def test_conjured_item_never_goes_below_zero(self):
        item = Item("Conjured Mana Cake", sell_in=0, quality=1)
        GildedRose([item]).update_quality()
        self.assertEqual(item.quality, 0)


if __name__ == '__main__':
    unittest.main()
