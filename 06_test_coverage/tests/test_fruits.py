import unittest
import fruits


class TestJustTrue(unittest.TestCase):
    def test_true(self):
        self.assertTrue(fruits.just_return_true())


class TestTrueOrFalse(unittest.TestCase):
    def test_true(self):
        self.assertEqual(fruits.true_or_false(True), 'TRUE')

    def test_false(self):
        self.assertEqual(fruits.true_or_false(False), 'FALSE')

    def test_error(self):
        self.assertEqual(fruits.true_or_false(7), 'ERROR')
