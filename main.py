# main.py — importa módulos conforme são mergeados na main

def menu():
    print("=== Calculadora GCS ===\n")

    try:
        from calc_basico import somar, subtrair, multiplicar, dividir
        print("Módulo Básico carregado.")
        print("2 + 3 =", somar(2, 3))
        print("10 - 4 =", subtrair(10, 4))
        print("5 * 6 =", multiplicar(5, 6))
        print("8 / 2 =", dividir(8, 2))
    except ImportError:
        print("Módulo Básico ainda não disponível.")

    print()

    try:
        from calc_potencia import potencia, raiz_quadrada, raiz_cubica
        print("Módulo Potência carregado.")
        print("2^10 =", potencia(2, 10))
        print("Raiz quadrada de 25 =", raiz_quadrada(25))
        print("Raiz cúbica de 27 =", raiz_cubica(27))
    except ImportError:
        print("Módulo Potência ainda não disponível.")

    print()

    try:
        from calc_percentual import percentual, acrescimo, desconto
        print("Módulo Percentual carregado.")
        print("10% de 200 =", percentual(200, 10))
        print("200 com acréscimo de 10% =", acrescimo(200, 10))
        print("200 com desconto de 10% =", desconto(200, 10))
    except ImportError:
        print("Módulo Percentual ainda não disponível.")

    print()

    try:
        from calc_estatistica import media, mediana, desvio_padrao
        valores = [10, 20, 30, 40]
        print("Módulo Estatística carregado.")
        print("Média:", media(valores))
        print("Mediana:", mediana(valores))
        print("Desvio padrão:", desvio_padrao(valores))
    except ImportError:
        print("Módulo Estatística ainda não disponível.")

    print()

    try:
        from calc_conversao import celsius_para_fahrenheit, km_para_milhas, kg_para_libras
        print("Módulo Conversão carregado.")
        print("30°C em Fahrenheit =", celsius_para_fahrenheit(30))
        print("10 km em milhas =", km_para_milhas(10))
        print("5 kg em libras =", kg_para_libras(5))
    except ImportError:
        print("Módulo Conversão ainda não disponível.")


if __name__ == "__main__":
    menu()