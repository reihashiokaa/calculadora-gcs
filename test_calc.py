#test_calc.py
#Testes da Calculadora GCS

import unittest

from calc_conversao import celsius_para_fahrenheit, km_para_milhas

class TestCalcConversao(unittest.TestCase):
    def test_celsius_para_fahrenheit(self):
        self.assertEqual(celsius_para_fahrenheit(0), 32)
        self.assertEqual(celsius_para_fahrenheit(30), 86)
        self.assertEqual(celsius_para_fahrenheit(45), 113)

    def test_km_para_milhas(self):
        self.assertEqual(km_para_milhas(0), 0)
        self.assertEqual(km_para_milhas(5), 3.10)
        self.assertEqual(km_para_milhas(10), 6.21)

if __name__ == '__main__':
    unittest.main()
