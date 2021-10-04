import main2
import unittest
from fractions import Fraction
import cmath


class Test_TestSum(unittest.TestCase):
    def test_sum_integer_integer(self):
        self.assertEqual(main2.sum(2, 2), 4)

    def test_sum_integer_float(self):
        self.assertEqual(main2.sum(2, 1.5), 3.5)

    def test_sum_integer_string(self):
        self.assertEqual(main2.sum(2, '2'), 4)

    def test_sum_string_string(self):
        self.assertEqual(main2.sum('2.1', '2.pyt0'), 4.1)
    
    def test_sum_integer_wrong_number_in_string(self):
        with self.assertRaises(Exception):
            main2.sum(2, "Ala ma kota123")
    
    def test_sum_fraction(self):
        self.assertEqual(main2.sum(Fraction(2, 3), Fraction(4, 3)), Fraction(2, 1))
    
    def test_sum_fraction_float_string(self):
        self.assertEqual(main2.sum(Fraction(1, 3), Fraction(4, 3)), Fraction(5,3))

    def test_sum_complex_correct(self):
        self.assertEqual(main2.sum( complex(1, 2), complex(2, 10) ), complex(3, 12) )    

    def test_list_exeption(self):
        with self.assertRaises(Exception):
            main2.sum(1, [2, 3])
            
if __name__ == '__main__':
    unittest.main()