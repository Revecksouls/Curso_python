# Crie um programa onde 4 jogadores joguem um dado e
# tenham resultado aleatórios. Guarde esses resultados em um
# dicionário . No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior numero no dado.

from random import  *
from operator import *
j1 = randint (1,10)
j2 = randint (1,10)
j3 = randint (1,10)
j4 = randint (1,10)

dc = {
    
    "jogador 1°" : j1,
    "jogador 2°" : j2,
    "jogador 3°" : j3,
    "jogador 4°" : j4
    
}
print(dc)
vencedor = max(j1,j2,j3,j4)

for k, v in dc.items():
    print(f"{k} tirou {v} no dado")
print("maior pontuação",vencedor)

ganhador = sorted(dc.items(),key  = itemgetter(1),reverse = True)

print(ganhador)
print(ganhador[0])


# jogador = (k)
    
# ganhou = max(j1,j2,j3,j4)
# print(f"{jogador} ganhou por {ganhou}")