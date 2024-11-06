import unittest

import points as p


class MyTestCase(unittest.TestCase):
    def test_init(self):
        self.assertEqual(p.Point(1, 2).x, 1)
        self.assertEqual(p.Point(1, 2).y, 2)
        self.assertEqual(p.Point(1.5, 2.5).x, 1.5)
        with self.assertRaises(TypeError):
            p.Point("a", 2)

    def test_str(self):
        self.assertEqual(str(p.Point(1, 2)), "(1, 2)")
        self.assertEqual(str(p.Point(1.5, 2.5)), "(1.5, 2.5)")
        with self.assertRaises(TypeError):
            str(p.Point("a", 2))

    def test_repr(self):
        self.assertEqual(repr(p.Point(1, 2)), "Point(1, 2)")
        self.assertEqual(repr(p.Point(1.5, 2.5)), "Point(1.5, 2.5)")

    def test_eq(self):
        self.assertEqual(p.Point(1, 2) == p.Point(1, 2), True)
        self.assertEqual(p.Point(1, 2) == p.Point(1, 3), False)
        self.assertEqual(p.Point(1, 2) == p.Point(2, 2), False)
        self.assertEqual(p.Point(1, 2) == p.Point(2, 3), False)
        self.assertEqual(p.Point(1, 2) == p.Point(1.0, 2.0), True)
        self.assertEqual(p.Point(1, 2) == p.Point(1.0, 2.5), False)

    def test_ne(self):
        self.assertEqual(p.Point(1, 2) != p.Point(1, 2), False)
        self.assertEqual(p.Point(1, 2) != p.Point(1, 3), True)
        self.assertEqual(p.Point(1, 2) != p.Point(2, 2), True)
        self.assertEqual(p.Point(1, 2) != p.Point(2, 3), True)
        self.assertEqual(p.Point(1, 2) != p.Point(1.0, 2.0), False)
        self.assertEqual(p.Point(1, 2) != p.Point(1.0, 2.5), True)

    def test_add(self):
        self.assertEqual(p.Point(1, 2) + p.Point(1, 2), p.Point(2, 4))
        self.assertEqual(p.Point(1, 2) + p.Point(1, 3), p.Point(2, 5))
        self.assertEqual(p.Point(1, 2) + p.Point(2, 2), p.Point(3, 4))
        self.assertEqual(p.Point(1, 2) + p.Point(2, 3), p.Point(3, 5))

    def test_sub(self):
        self.assertEqual(p.Point(1, 2) - p.Point(1, 2), p.Point(0, 0))
        self.assertEqual(p.Point(1, 2) - p.Point(1, 3), p.Point(0, -1))
        self.assertEqual(p.Point(1, 2) - p.Point(2, 2), p.Point(-1, 0))
        self.assertEqual(p.Point(1, 2) - p.Point(2, 3), p.Point(-1, -1))

    def test_mul(self):
        self.assertEqual(p.Point(1, 2) * p.Point(1, 2), 5)
        self.assertEqual(p.Point(1, 2) * p.Point(1, 3), 7)
        self.assertEqual(p.Point(1, 2) * p.Point(2, 2), 6)
        self.assertEqual(p.Point(1, 2) * p.Point(2, 3), 8)

    def test_cross(self):
        self.assertEqual(p.Point(1, 2).cross(p.Point(1, 2)), 0)
        self.assertEqual(p.Point(1, 2).cross(p.Point(1, 3)), 1)
        self.assertEqual(p.Point(1, 2).cross(p.Point(2, 2)), -2)
        self.assertEqual(p.Point(1, -2).cross(p.Point(-2, 3)), -1)

    def test_length(self):
        self.assertEqual(p.Point(3, 4).length(), 5)
        self.assertEqual(p.Point(1, 1).length(), 2 ** 0.5)
        self.assertEqual(p.Point(1, 0).length(), 1)
        self.assertEqual(p.Point(0, 1).length(), 1)

    def test_hash(self):
        self.assertEqual(hash(p.Point(1, 2)), hash((1, 2)))
        self.assertEqual(hash(p.Point(1.5, 2.5)), hash((1.5, 2.5)))







if __name__ == '__main__':
    unittest.main()
