from random import randint

maquina = usuario = 0

for elemento in range(1,10):
    
    escolha_maquina = randint (0,5)
    print(escolha_maquina)
    escolha_Usuario = int(input(f"{elemento}° rodada, digite um numero: "))
    
    if escolha_maquina == escolha_Usuario:
        usuario = usuario + 1 
        print("usuario venceu")
    else:
        maquina = maquina + 1
        print("maquina venceu")
else:
    print(f"voce acertou {usuario}")       