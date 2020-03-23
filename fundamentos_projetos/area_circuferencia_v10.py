from math import pi
import sys


def circulo(raio):
    return pi * raio**2


if(__name__ == '__main__'):

    raio = sys.argv[1]
    area = circulo(raio)
    print('Area: ', area)
