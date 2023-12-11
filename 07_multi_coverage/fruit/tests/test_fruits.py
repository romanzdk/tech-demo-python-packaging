import unittest
import cherry


class TestJustTrue(unittest.TestCase):
    def test_true(self):
        self.assertTrue(cherry.just_return_true())


class TestTrueOrFalse(unittest.TestCase):
    def test_true(self):
        self.assertEqual(cherry.true_or_false(True), 'TRUE')

    def test_error(self):
        self.assertEqual(cherry.true_or_false(7), 'ERROR')
