import unittest
import banana


class TestJustTrue(unittest.TestCase):
    def test_true(self):
        self.assertTrue(banana.just_return_true())


class TestTrueOrFalse(unittest.TestCase):
    def test_true(self):
        self.assertEqual(banana.true_or_false(True), 'TRUE')

    def test_false(self):
        self.assertEqual(banana.true_or_false(False), 'FALSE')

    def test_error(self):
        self.assertEqual(banana.true_or_false(7), 'ERROR')
