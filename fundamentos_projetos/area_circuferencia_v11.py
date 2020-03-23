from math import pi
import sys


def circulo(raio):
    return pi * raio**2


if __name__ == '__main__':
    
    if (len(sys.argv)<2):
        nomeScript = sys.argv[0]
        print('É necessario informar o raio do círculo.')
        print(f'Sintaxe: {nomeScript} <raio>')
    else:
        raio = float(sys.argv[1])
        area = circulo(raio)
        print('Area: ', area)
