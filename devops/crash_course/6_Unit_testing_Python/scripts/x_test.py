'''
author: faraz mazhar
descri: Testing Simple arithmatic functions.
'''

import unittest
from a_sample import add, sub, mul, div

class Tests(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(5, 6), 11, msg='Addition.')
    
    def test_sub(self):
        self.assertEqual(sub(6, 3), 3, msg='Subtraction.')

    def test_mul(self):
        self.assertEqual(mul(3, 2), 6, msg='Multiplication.')
    
    def test_div(self):
        self.assertEqual(div(6, 3), 2, msg='Division.')

if __name__ == "__main__":
    unittest.main()