import unittest
from main import Validate

class TestCodes(unittest.TestCase):

    def test_right_codes(self):
        self.assertTrue('523563')
        self.assertTrue('112233')

    def test_false_codes(self):
        self.assertFalse('121426')
        self.assertFalse('552523')

if __name__ == '__main__':
    unittest.main()
