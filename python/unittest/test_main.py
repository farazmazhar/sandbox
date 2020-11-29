"""
Unittest test three.
"""

import unittest
from test_two import two
from test_one import test_one

if __name__ == "__main__":
    unittest.main(two)
    unittest.main(test_one)

