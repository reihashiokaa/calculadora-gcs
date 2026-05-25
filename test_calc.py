#test_calc.py
#Testes da Calculadora GCS

import unittest

from calc_conversao import celsius_para_fahrenheit

class TestCalcConversao(unittest.TestCase):
    def test_celsius_para_fahrenheit(self):
        self.assertEqual(celsius_para_fahrenheit(0), 32)
        self.assertEqual(celsius_para_fahrenheit(30), 86)
        self.assertEqual(celsius_para_fahrenheit(45), 113)

if __name__ == '__main__':
    unittest.main()
