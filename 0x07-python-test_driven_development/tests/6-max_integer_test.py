#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittests for max_integer([..])."""

    def test_ordered(self):
        """Unittest for max_integer([..])"""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered(self):
        """Test an unordered list of integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        self.assertEqual(max_integer([5, 4, 3, 2]), 5)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        self.assertEqual(max_integer([98]), 98)

    def test_floats(self):
        """Test a list of floats."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        """Unittest for max_integer([..])"""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        """Test a string."""
        self.assertEqual(max_integer("Holberton"), "t")

    def test_list_of_strings(self):
        """Test a list of strings."""
        self.assertEqual(
                max_integer([["foo"], ["boo"], ["abc"], ["sic"], ["ric"]]),
                ["sic"])

    def test_empty_string(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
