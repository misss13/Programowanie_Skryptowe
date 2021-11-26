from zadanie1 import Operacje
import unittest

class Test_Suma(unittest.TestCase):
    def test_suma_1(self):
        op = Operacje()
        self.assertEqual(op.suma(1), None)

    def test_suma_2(self):
        op = Operacje()
        self.assertEqual(op.suma(1, 2), 5)
        
    def test_suma_3(self):
        op = Operacje()
        self.assertEqual(op.suma(3, 3, 3), 4)

    def test_suma_TypeError(self):
        op = Operacje()
        with self.assertRaises(TypeError):
            op.suma()


class Test_Roznica(unittest.TestCase):
    def test_roznica_0(self):
        op = Operacje()
        self.assertEqual(op.roznica(), 6)    

    def test_roznica_1(self):
        op = Operacje()
        self.assertEqual(op.roznica(2), 5)

    def test_roznica_2(self):
        op = Operacje()
        self.assertEqual(op.roznica(2, 1), 4)


class Test_Zmiana(unittest.TestCase):
    def test_zmiana_s1(self):
        op = Operacje()
        op['suma'] = [1, 3]
        self.assertEqual(op.argumentySuma, [1, 3])
        self.assertEqual(op.suma(1, 2), 3) #3
        
    def test_zmiana_r1(self):
        op = Operacje()
        op['roznica'] = [4, 2, 3]
        self.assertEqual(op.argumentyRoznica, [4, 2, 3])
        self.assertEqual(op.roznica(2, 1), 4) #2
    

if __name__ == '__main__':
    unittest.main()
    #python3 test1.py -b