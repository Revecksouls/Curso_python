#importa toda a biblioteca 
#import random
#renomear 
#import random as rd
#importa metodos especificos da biblioteca
from random import *

nota1 = randint(1,10)
nota2 = randint(1,10)

media = (nota1 + nota2) / 2 

if media >= 7 :
    print("aluno aprovado")
else:
    print("aluno reprovado")
print (media)