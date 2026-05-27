# test_calc.py
# Testes da Calculadora GCS

import unittest

from calc_conversao import celsius_para_fahrenheit, km_para_milhas, kg_para_libras
from calc_potencia import potencia, raiz_quadrada, raiz_cubica


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


class TestCalcPotencia(unittest.TestCase):
    def test_potencia(self):
        self.assertEqual(potencia(2, 3), 8)
        self.assertEqual(potencia(5, 0), 1)
        self.assertEqual(potencia(3, 4), 81)

    def test_raiz_quadrada(self):
        self.assertEqual(raiz_quadrada(9), 3)
        self.assertEqual(raiz_quadrada(25), 5)
        self.assertEqual(raiz_quadrada(0), 0)

    def test_raiz_quadrada_negativa(self):
        with self.assertRaises(ValueError):
            raiz_quadrada(-4)

    def test_raiz_cubica(self):
        self.assertAlmostEqual(raiz_cubica(27), 3)
        self.assertAlmostEqual(raiz_cubica(8), 2)
        self.assertAlmostEqual(raiz_cubica(0), 0)
        self.assertAlmostEqual(raiz_cubica(-8), -2)


if __name__ == '__main__':
    unittest.main()