"""
Unittests in Python.
"""

import unittest
from unittest.mock import MagicMock


class Cool:
    def add(self, x, y, z=1):
        return x + y - z


class CoolTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual(1, 1)

    def test_two(self):
        self.assertNotEqual(1, 2)

    def test_three(self):
        self.assertIsInstance(MagicMock(spec=Cool), Cool)


if __name__ == "__main__":
    unittest.main()
