import unittest
import helloworldpkg
import howareyoupkg


class Integration(unittest.TestCase):
    def test_import(self):
        self.assertTrue(helloworldpkg.just_return_true())
        self.assertTrue(howareyoupkg.just_return_true())
