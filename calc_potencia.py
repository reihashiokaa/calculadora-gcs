# calc_potencia.py
# Módulo B — Potência
# Autor: Luciana
# Branch: feature/modulo-potencia

import math


def potencia(base, expoente):
    return base ** expoente


def raiz_quadrada(valor):
    if valor < 0:
        raise ValueError("Não existe raiz quadrada real de número negativo.")
    return math.sqrt(valor)

def raiz_cubica(valor):
    if valor < 0:
        return -((-valor) ** (1/3))
    return valor ** (1/3)