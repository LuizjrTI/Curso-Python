

def calcconceito(nota):
    if(nota > 10 or nota < 0):
        print("Nota invalida")
    else:
        if(nota <= 10 and nota >= 9.1):
            print("A")
        elif(nota <= 9 and nota >= 8.1):
            print("A-")
        elif(nota <= 8 and nota >= 7.1):
            print("B")
        elif(nota <= 7 and nota >= 6.1):
            print("B-")
        elif(nota <= 6 and nota >= 5.1):
            print("C")
        elif(nota <= 5 and nota >= 4.1):
            print("C-")
        elif(nota <= 4 and nota >= 3.1):
            print("D")
        elif(nota <= 3 and nota >= 2.1):
            print("D-")
        elif(nota <= 2 and nota >= 1.1):
            print("E")
        elif(nota <= 1 and nota >= 0):
            print("E-")


if __name__ == '__main__':

    nota_conceito = float(input("Digite uma nota: "))
    calcconceito(nota_conceito)
