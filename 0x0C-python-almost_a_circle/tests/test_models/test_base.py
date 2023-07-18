#!/usr/bin/python3
"""Unittest for Base
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_base_1(self):
        b1 = Base()
        self.assertEqual(b1.id, 1, "Id is not 1")

    def test_base_2(self):
        b2 = Base()
        self.assertEqual(b2.id, 2, "Id is not 2")

    def test_base_3(self):
        b = Base(12)
        self.assertEqual(b.id, 12, "Id is not 12")
