import unittest
import helloworldpkg


class HelloWorld(unittest.TestCase):
    def test_dummy(self):
        self.assertTrue(True)

    def test_import(self):
        self.assertTrue(helloworldpkg.just_return_true())
