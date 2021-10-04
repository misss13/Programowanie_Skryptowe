import main
import unittest
from fractions import Fraction
import cmath


class Test_TestSum(unittest.TestCase):
    def test_sum_integer_integer(self):
        self.assertEqual(main.sum(2, 2), 4)

    def test_sum_integer_float(self):
        self.assertEqual(main.sum(2, 1.5), 3.5)

    def test_sum_integer_string(self):
        self.assertEqual(main.sum(2, '2'), 4)

    def test_sum_string_string(self):
        self.assertEqual(main.sum('2.1', '2.0'), 4.1)
    
    def test_sum_integer_wrong_number_in_string(self):
        self.assertEqual(main.sum(2, 'Ala ma kota123'), 2)

    
    def test_sum_fraction(self):
        self.assertEqual(main.sum(Fraction(2, 3), Fraction(4, 3)), Fraction(2, 1))
    
    def test_sum_fraction_float_string(self):
        self.assertEqual(main.sum(Fraction(1, 3), "2.0"), 2.3333333333333335)

    def test_sum_complex_correct(self):
        self.assertEqual( main.sum( complex(10, 4), complex(2, 11) ), complex(12, 15) )    

if __name__ == '__main__':
    unittest.main()