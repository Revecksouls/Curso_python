from random import*
escolha_maquina = randint (0,5)


for elemento in range(1,10,1):
    escolha_Usuario = int(input(f"{elemento}° rodada, digite um numero: "))
    
    if escolha_Usuario == escolha_maquina:
        print("voce venceu")
        break
else:
    print("maquina venceu")
    