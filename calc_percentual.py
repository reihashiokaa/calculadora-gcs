#percentual
def percentual(valor, porcentagem):
    return valor * (porcentagem / 100)

def acrescimo(valor,  porcentagem):
    return valor + percentual(valor, porcentagem)

