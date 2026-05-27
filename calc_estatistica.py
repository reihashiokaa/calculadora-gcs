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

def mediana(valores):
    """Retorna a mediana dos valores informados."""
    if len(valores) == 0:
        raise ValueError("A lista de valores não pode estar vazia.")
    
    valores_ordenados = sorted(valores)
    tamanho = len(valores_ordenados)
    meio = tamanho // 2

    if tamanho % 2 == 1:
        return valores_ordenados[meio]
    
    return (valores_ordenados[meio - 1] + valores_ordenados[meio]) / 2