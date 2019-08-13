import unittest
from main import Validate

class TestCodes(unittest.TestCase):

    def test_right_codes(self):
        self.assertTrue(Validate('523563'))
        self.assertTrue(Validate('112233'))

    def test_false_codes(self):
        self.assertFalse(Validate('121426'))
        self.assertFalse(Validate('552523'))

    def test_invalid_size(self):
        self.assertRaises(Exception, Validate, '')
        self.assertRaises(Exception, Validate, '123')
        self.assertRaises(Exception, Validate, '12345')
        self.assertRaises(Exception, Validate, '1234567')

    def test_range(self):
        self.assertRaises(Exception, Validate, '100000')
        self.assertRaises(Exception, Validate, '999999')

if __name__ == '__main__':
    unittest.main()
