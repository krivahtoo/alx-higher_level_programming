#!/usr/bin/python3
"""Unittest for Rectangle
"""
import unittest
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):

    def test_id(self):
        rec = Rectangle(4, 2)
        self.assertEqual(rec.id, 4, "Id is not 4")

    def test_str(self):
        rec = Rectangle(4, 4, 0, 1)
        self.assertEqual(str(rec), "[Rectangle] (9) 0/1 - 4/4")

    def test_str_with_id(self):
        rec = Rectangle(4, 4, 0, 1, 12)
        self.assertEqual(str(rec), "[Rectangle] (12) 0/1 - 4/4")

    def test_width(self):
        rec = Rectangle(12, 16)
        self.assertEqual(rec.width, 12, "width is not 12")

    def test_height(self):
        rec = Rectangle(12, 16)
        self.assertEqual(rec.height, 16, "height is not 16")

    def test_raises_typeerror_on_width(self):
        with self.assertRaises(TypeError) as cm:
            Rectangle("", 12)
        self.assertEqual(str(cm.exception), "width must be an integer")

    def test_raises_typeerror_on_height(self):
        with self.assertRaises(TypeError) as cm:
            Rectangle(12, "")
        self.assertEqual(str(cm.exception), "height must be an integer")

    def test_raises_typeerror_on_x(self):
        with self.assertRaises(TypeError) as cm:
            Rectangle(12, 16, [])
        self.assertEqual(str(cm.exception), "x must be an integer")

    def test_raises_typeerror_on_y(self):
        with self.assertRaises(TypeError) as cm:
            Rectangle(12, 16, 2, [])
        self.assertEqual(str(cm.exception), "y must be an integer")

    def test_update0(self):
        rec = Rectangle(12, 16)
        rec.update(17, 50)
        self.assertEqual(rec.id, 17)
        self.assertEqual(rec.width, 50)

    def test_update1(self):
        rec = Rectangle(12, 16)
        rec.update(x=17, id=50)
        self.assertEqual(rec.x, 17)
        self.assertEqual(rec.id, 50)
