import unittest
import pumpkin
import pumpkin.bar


class TestBar(unittest.TestCase):
    def test_bar(self):
        self.assertEqual(pumpkin.bar.bar(), 'bar')
