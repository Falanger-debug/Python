import unittest
import fracs as f

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.frac_zero = [0, 1]
        self.frac_zero_minus = [-0, 2]
        self.frac1 = [1, 2]
        self.frac2 = [1, 3]
        self.frac3 = [23, 3]
        self.frac4 = [3, 23]
        self.frac_one = [1, 1]
        self.frac_one_reducible = [1, 1]
        self.frac_reducible_1 = [2, 4]
        self.frac_reducible_2 = [2, 6]
        self.frac_minus_at_first = [-2, 3]
        self.frac_minus_at_second = [2, -3]
        self.frac_minus_at_both = [-2, -3]
        self.frac_zero_denominator = [2, 0]
        self.frac_zero_numerator = [0, 2]
        self.frac_zero_numerator_1 = [0, 13]
        self.frac_zero_both = [0, 0]
        self.frac_with_NaN = ["m", 2]
        self.frac_with_float = [2.3, 2]

    def test_add_frac(self):
        self.assertEqual(f.add_frac(self.frac1, self.frac2), [5, 6])
        self.assertEqual(f.add_frac(self.frac3, self.frac4), [538, 69])
        self.assertEqual(f.add_frac(self.frac_zero, self.frac1), [1, 2])
        self.assertEqual(f.add_frac(self.frac1, self.frac_reducible_1), [1, 1])
        with self.assertRaises(ValueError):
            f.add_frac(self.frac1, self.frac_with_float)
        with self.assertRaises(ValueError):
            f.add_frac(self.frac1, self.frac_with_NaN)
        with self.assertRaises(ValueError):
            f.add_frac(self.frac1, self.frac_zero_denominator)

    def test_sub_frac(self):
        self.assertEqual(f.sub_frac(self.frac1, self.frac2), [1, 6])
        self.assertEqual(f.sub_frac(self.frac3, self.frac4), [520, 69])
        self.assertEqual(f.sub_frac(self.frac_zero, self.frac1), [-1, 2])
        self.assertEqual(f.sub_frac(self.frac1, self.frac_reducible_1), [0, 1])
        with self.assertRaises(ValueError):
            f.sub_frac(self.frac1, self.frac_with_float)
        with self.assertRaises(ValueError):
            f.sub_frac(self.frac1, self.frac_with_NaN)
        with self.assertRaises(ValueError):
            f.sub_frac(self.frac1, self.frac_zero_denominator)

    def test_mul_frac(self):
        self.assertEqual(f.mul_frac(self.frac1, self.frac2), [1, 6])
        self.assertEqual(f.mul_frac(self.frac3, self.frac4), [1, 1])
        self.assertEqual(f.mul_frac(self.frac_zero, self.frac1), [0, 1])
        self.assertEqual(f.mul_frac(self.frac_minus_at_first, self.frac_minus_at_second), [4, 9])
        with self.assertRaises(ValueError):
            f.mul_frac(self.frac1, self.frac_with_float)
        with self.assertRaises(ValueError):
            f.mul_frac(self.frac1, self.frac_with_NaN)
        with self.assertRaises(ValueError):
            f.mul_frac(self.frac1, self.frac_zero_denominator)

    def test_div_frac(self):
        self.assertEqual(f.div_frac(self.frac1, self.frac2), [3, 2])
        self.assertEqual(f.div_frac(self.frac3, self.frac4), [529, 9])
        self.assertEqual(f.div_frac(self.frac_one, self.frac_one_reducible), [1, 1])
        self.assertEqual(f.div_frac(self.frac_minus_at_first, self.frac_minus_at_both), [-1, 1])
        with self.assertRaises(ValueError):
            f.div_frac(self.frac1, self.frac_with_float)
        with self.assertRaises(ValueError):
            f.div_frac(self.frac1, self.frac_with_NaN)
        with self.assertRaises(ValueError):
            f.div_frac(self.frac1, self.frac_zero_denominator)
        with self.assertRaises(ValueError):
            f.div_frac(self.frac1, self.frac_zero_numerator)

    def test_is_positive(self):
        self.assertTrue(f.is_positive(self.frac1))
        self.assertTrue(f.is_positive(self.frac3))
        self.assertFalse(f.is_positive(self.frac_minus_at_first))
        self.assertFalse(f.is_positive(self.frac_minus_at_second))
        with self.assertRaises(ValueError):
            f.is_positive(self.frac_with_float)
        with self.assertRaises(ValueError):
            f.is_positive(self.frac_with_NaN)
        with self.assertRaises(ValueError):
            f.is_positive(self.frac_zero_denominator)

    def test_is_zero(self):
        self.assertTrue(f.is_zero(self.frac_zero))
        self.assertTrue(f.is_zero(self.frac_zero_numerator))
        self.assertFalse(f.is_zero(self.frac1))
        with self.assertRaises(ValueError):
            f.is_zero(self.frac_with_float)
        with self.assertRaises(ValueError):
            f.is_zero(self.frac_with_NaN)
        with self.assertRaises(ValueError):
            f.is_zero(self.frac_zero_denominator)

    def test_cmp_frac(self):
        self.assertEqual(f.cmp_frac(self.frac1, self.frac2), 1)
        self.assertEqual(f.cmp_frac(self.frac3, self.frac4), 1)
        self.assertEqual(f.cmp_frac(self.frac_zero, self.frac_zero_numerator), 0)
        self.assertEqual(f.cmp_frac(self.frac_minus_at_first, self.frac_minus_at_second), 0)
        with self.assertRaises(ValueError):
            f.cmp_frac(self.frac1, self.frac_with_float)
        with self.assertRaises(ValueError):
            f.cmp_frac(self.frac1, self.frac_with_NaN)
        with self.assertRaises(ValueError):
            f.cmp_frac(self.frac1, self.frac_zero_denominator)

    def test_frac2float(self):
        self.assertEqual(f.frac2float(self.frac1), 0.5)
        self.assertEqual(f.frac2float(self.frac2), 1/3)
        self.assertEqual(f.frac2float(self.frac_one), 1.0)
        self.assertEqual(f.frac2float(self.frac_minus_at_first), -2/3)
        with self.assertRaises(ValueError):
            f.frac2float(self.frac_with_float)
        with self.assertRaises(ValueError):
            f.frac2float(self.frac_with_NaN)
        with self.assertRaises(ValueError):
            f.frac2float(self.frac_zero_denominator)

if __name__ == '__main__':
    unittest.main()
