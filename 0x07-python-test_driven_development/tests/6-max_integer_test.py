#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_max(self):
        self.assertEqual(max_integer([2, 3, 10, 4]), 10)

    def test_none(self):
        self.assertIsNotNone(max_integer([4]))
