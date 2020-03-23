from math import pi

def circulo(raio):
    return pi * raio**2
    


if(__name__ == '__main__'):
    raio = float(input('Digite o Raio: '))
    area = circulo(raio)
    print('Area: ',area)
     