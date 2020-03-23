import math


def circulo(raio):
    result = math.pi * raio**2
    print(f'A área do círculo: {result}')


if(__name__ == '__main__'):
    raio = float(input('Digite o Raio: '))
    circulo(raio)