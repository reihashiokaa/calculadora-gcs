#test_calc.py
#Testes da Calculadora GCS

import unittest

from calc_basico import somar, subtrair, multiplicar, dividir

class TestCalcBasico(unittest.TestCase):
    def test_somar(self):
        self.assertEqual(somar(2, 3), 5)
        self.assertEqual(somar(-2, 2), 0)

    def test_subtrair(self):
        self.assertEqual(subtrair(10, 4), 6)
        self.assertEqual(subtrair(3, 8), -5)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(5, 6), 30)
        self.assertEqual(multiplicar(7, 0), 0)

    def test_dividir(self):
        self.assertEqual(dividir(8, 2), 4)
        self.assertEqual(dividir(5, 2), 2.5)

    def test_dividir_por_zero(self):
        with self.assertRaises(ValueError):
            dividir(8, 0)

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


from calc_estatistica import media, mediana, desvio_padrao

class TestCalcEstatistica(unittest.TestCase):
    def test_media(self):
        self.assertEqual(media([10, 20, 30]), 20)
        self.assertEqual(media([5, 5, 5, 5]), 5)

    def test_media_lista_vazia(self):
        with self.assertRaises(ValueError):
            media([])

    def test_mediana_quantidade_impar(self):
        self.assertEqual(mediana([10, 20, 30]), 20)
        self.assertEqual(mediana([30, 10, 20]), 20)

    def test_mediana_quantidade_par(self):
        self.assertEqual(mediana([10, 20, 30, 40]), 25)

    def test_mediana_lista_vazia(self):
        with self.assertRaises(ValueError):
            mediana ([])

    def test_desvio_padrao(self):
        self.assertAlmostEqual(desvio_padrao([10, 20, 30]), 8.1649658093)
    
    def test_desvio_padrao_lista_vazia(self):
        with self.assertRaises(ValueError):
            desvio_padrao([])

if __name__ == '__main__':
    unittest.main()

    
