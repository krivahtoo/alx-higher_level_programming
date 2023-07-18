#!/usr/bin/python3
"""Unittest for Rectangle
"""
import unittest
from models.base import Base


class TestMaxInteger(unittest.TestCase):

    def test_base_1(self):
        b1 = Base()
        self.assertEqual(b1.id, 1, "Id is not 1")

    def test_base_2(self):
        b2 = Base()
        self.assertEqual(b2.id, 2, "Id is not 2")
