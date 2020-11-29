"""
Unittest test two.
"""

import unittest


class CoolTest(unittest.TestCase):
    def test_a(self):
        self.assertEqual(1, 1)

    def test_b(self):
        self.assertEqual(True, True, 'cool')

    def test_c(self):
        self.assertDictContainsSubset({'a': 1}, {'a': 1, 'b': 2}, 'nice!')
