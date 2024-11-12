import unittest
from Exercise_6_2.points import Point
from Exercise_6_3.rectangles import Rectangle


class MyTestCase(unittest.TestCase):
    def test_init(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect.pt1, Point(1, 2))
        self.assertEqual(rect.pt2, Point(3, 4))

        rect_float = Rectangle(1.5, 2.5, 3.5, 4.5)
        self.assertEqual(rect_float.pt1, Point(1.5, 2.5))
        self.assertEqual(rect_float.pt2, Point(3.5, 4.5))

        with self.assertRaises(TypeError):
            Rectangle("a", 2, 3, 4)
            Rectangle(1, "a", 3, 4)
            Rectangle(1, 2, "a", 4)
            Rectangle(1, 2, 3, "a")

    def test_str(self):
        self.assertEqual(str(Rectangle(1, 2, 3, 4)), "[(1, 2), (3, 4)]")
        self.assertEqual(str(Rectangle(1.5, 2.5, 3.5, 4.5)), "[(1.5, 2.5), (3.5, 4.5)]")

    def test_repr(self):
        self.assertEqual(repr(Rectangle(1, 2, 3, 4)), "Rectangle(1, 2, 3, 4)")
        self.assertEqual(repr(Rectangle(1.5, 2.5, 3.5, 4.5)), "Rectangle(1.5, 2.5, 3.5, 4.5)")

    def test_eq(self):
        self.assertEqual(Rectangle(1, 2, 3, 4) == Rectangle(1, 2, 3, 4), True)
        self.assertEqual(Rectangle(1, 2, 3, 4) == Rectangle(1, 2, 3, 5), False)

    def test_ne(self):
        self.assertEqual(Rectangle(1, 2, 3, 4) != Rectangle(1, 2, 3, 4), False)
        self.assertEqual(Rectangle(1, 2, 3, 4) != Rectangle(1, 2, 3, 5), True)

    def test_center(self):
        self.assertEqual(Rectangle(1, 2, 3, 4).center(), Point(2, 3))
        self.assertEqual(Rectangle(1.5, 2.5, 3.5, 4.5).center(), Point(2.5, 3.5))

    def test_area(self):
        self.assertEqual(Rectangle(1, 2, 3, 4).area(), 4)
        self.assertEqual(Rectangle(1.5, 2.5, 3.5, 4.5).area(), 4)

    def test_move(self):
        self.assertEqual(Rectangle(1, 2, 3, 4).move(1, 1), Rectangle(2, 3, 4, 5))
        self.assertEqual(Rectangle(1.5, 2.5, 3.5, 4.5).move(1, 1), Rectangle(2.5, 3.5, 4.5, 5.5))


if __name__ == '__main__':
    unittest.main()
