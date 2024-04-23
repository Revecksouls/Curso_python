from math import sqrt

try:
    valor = int(input("Digite um valor e descubra a sua  raiz quadrada: "))
    raiz_quadrada = sqrt(valor)
    
except ValueError:
    print("pfvr digite um valor numerico positivo")
else:
    print(raiz_quadrada)