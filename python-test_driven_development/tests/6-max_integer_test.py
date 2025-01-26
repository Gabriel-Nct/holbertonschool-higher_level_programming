#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer function"""

    def test_ordered_list(self):
        """Test with an ordered list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list of integers"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_single_element_list(self):
        """Test with a list containing a single element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test with a list of negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test with a list of positive and negative numbers"""
        self.assertEqual(max_integer([-10, 5, 3, 0]), 5)

    def test_duplicates(self):
        """Test with a list containing duplicate values"""
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_floats(self):
        """Test with a list of floats"""
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 2.1]), 3.3)

    def test_mixed_types(self):
        """Test with a list of integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 3, 0.5]), 3)

    def test_string_list(self):
        """Test with a list of strings"""
        self.assertEqual(max_integer(["a", "b", "c", "d"]), "d")

    def test_single_string(self):
        """Test with a single string"""
        self.assertEqual(max_integer("abcd"), "d")

    def test_none_argument(self):
        """Test with None as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_no_argument(self):
        """Test with no argument"""
        self.assertIsNone(max_integer())

    def test_mixed_invalid(self):
        """Test with a list containing invalid types"""
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3])

if __name__ == "__main__":
    unittest.main()
