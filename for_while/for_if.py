from random import randint

aleatorio = randint(0,5)
maquina = 0
usuario = 0 

for elemento in range (1,11):
    numero = int(input(f"{elemento} rodada, digite um numero: "))
    print("Voce acertou")
    usuario = usuario + 1
else:
    print("voce errou")
    maquina = maquina + 1