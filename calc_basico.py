# calc_basico.py
# Módulo A - Operações Básicas
# Responsável: Beatriz
# Branch: feature/modulo-basico

def somar(a, b):
    """Retorna a soma de a e b."""
    return a + b

def subtrair(a, b):
    """Retorna a diferença entre a e b."""
    return a - b

def multiplicar(a, b):
    """Retorna o produto entre a e b."""
    return a * b

def dividir(a, b):
    """Retorna a divisão de a por b.
    
    Lança ValueError se b for igual a zero.
    """
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b