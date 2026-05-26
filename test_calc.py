#test_calc.py
#Testes da Calculadora GCS

import unittest

from calc_basico import somar

class TestCalcBasico(unittest.TestCase):
    def test_somar(self):
        self.assertEqual(somar(2, 3), 5)
        self.assertEqual(somar(-2, 2), 0)

from calc_conversao import celsius_para_fahrenheit, km_para_milhas, kg_para_libras

class TestCalcConversao(unittest.TestCase):
    def test_celsius_para_fahrenheit(self):
        self.assertEqual(celsius_para_fahrenheit(0), 32)
        self.assertEqual(celsius_para_fahrenheit(30), 86)
        self.assertEqual(celsius_para_fahrenheit(45), 113)

    def test_km_para_milhas(self):
        self.assertEqual(km_para_milhas(0), 0)
        self.assertEqual(km_para_milhas(5), 3.10)
        self.assertEqual(km_para_milhas(10), 6.21)

    def test_kg_para_libras(self):
        self.assertEqual(kg_para_libras(0), 0)
        self.assertEqual(kg_para_libras(5), 11.02)
        self.assertEqual(kg_para_libras(10), 22.04)

if __name__ == '__main__':
    unittest.main()
