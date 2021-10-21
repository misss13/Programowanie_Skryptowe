from skrypt import wypisywanie
import unittest
import io
import sys

class Test_wypisywanie(unittest.TestCase):

    def test_1(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        wypisywanie('50coś50coś')
        self.assertEqual(capturedOutput.getvalue(), 'Liczba:  50 50\nWyraz:  coś coś\n')

    def test_2(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        wypisywanie('psów20')
        self.assertEqual(capturedOutput.getvalue(), 'Liczba:  20\nWyraz:  psów\n')

    def test_3(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        wypisywanie('zażółćgęśląjaźń1')
        self.assertEqual(capturedOutput.getvalue(), 'Liczba:  1\nWyraz:  zażółćgęśląjaźń\n')

    def test_4(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        wypisywanie('ala ma kota')
        self.assertEqual(capturedOutput.getvalue(), 'Wyraz:  ala ma kota\n')

    def test_5(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        wypisywanie('50 50')
        self.assertEqual(capturedOutput.getvalue(), 'Liczba:  50 50\n')


if __name__ == '__main__':
    unittest.main()