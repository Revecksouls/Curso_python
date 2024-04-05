from random import*


escolha = randint(1,10)
print(escolha)

palpite = 0
palpite1 = 1
while True:
    escolha_usuario = int(input("Pfvr escolha um numero de 0 a 10: "))
    if escolha_usuario == escolha:
        print("usuario acertou")
        break
    else:
        print("usuario errou, pfvr tente novamente")
    palpite = palpite + palpite1
print(f"qunatidade de palpites: {palpite}")
