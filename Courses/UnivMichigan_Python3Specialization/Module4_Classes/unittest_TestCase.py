import unittest

class GovindUnitTest(unittest.TestCase):
    ''' This class inherits from unittest.TestCase and defines 3 finctions that 
    test equality, Truth and False
    '''  
    def test_is_equal(self):
        fn = lambda x : x **4
        self.assertEqual(fn(2), 16)

    def test_is_true(self):
        self.assertTrue(1)

    def test_is_false(self):
        self.assertFalse(0)    

if __name__ == '__main__':
    unittest.main()