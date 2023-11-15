import unittest

# Be aware!
# No need to know where in the filesystem the py-files are located.
# This is because we can simply import the application package because
# it is installed (in Developmend Mode via --editable).
import helloworldint


class DummyTest(unittest.TestCase):
    def test_dummy(self):
        self.assertTrue(True)

    def test_import(self):
        self.assertTrue(helloworldint.just_return_true())
