import unittest
import howareyoupkg


class HowAreYou(unittest.TestCase):
    def test_dummy(self):
        self.assertTrue(True)

    def test_import(self):
        self.assertTrue(howareyoupkg.just_return_true())
