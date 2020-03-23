from math import pi
import sys


def circulo(raio):
    return pi * raio**2


def help():
    nomeScript = sys.argv[0]
    print('É necessario informar o raio do círculo.')
    print(f'Sintaxe: {nomeScript} <raio>')


if __name__ == '__main__':

    if (len(sys.argv) < 2):
        help()
        sys.exit(1)
    elif not sys.argv[1].isnumeric():
        help()
        print(" O raio deve ser um valor númerico")
        sys.exit(1)
    else:
        raio = float(sys.argv[1])
        area = circulo(raio)
        print('Area: ', area)
