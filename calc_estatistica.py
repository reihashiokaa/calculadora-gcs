# calc_estatistica.py
# Módulo D - Estatística
# Responsável: Isabela
# Branch: feature/modulo-estatistica

import math

def media(valores):
    """Retorna a média dos valores informados."""

    if len(valores) == 0:
        raise ValueError("A lista de valores não pode estar vazia.")
    return sum(valores) / len(valores)
