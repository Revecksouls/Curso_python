from random import choice
lista = ['papel', "pedra" , "tesoura"]

while True:
    escolha = choice(lista)
    print (escolha)

    usuario = input("informe sua escolha: ")

    if usuario == escolha:
        print("Deu empate")
        break
    elif escolha == "pedra" and usuario == "papel":
        print("maquina perdeu")
        break
    elif escolha == "papel" and usuario == "tesoura":
        print("maquina perdeu")
        break
    elif escolha == "tesoura" and usuario == "pedra":
        print("maquina perdeu")
        break
    elif escolha == "pedra" and usuario == "tesoura":
        print("usuario perdeu")
    elif escolha == "tesoura" and usuario == "papel":
        print("usuario perdeu")    
    elif escolha == "papel" and usuario == "pedra":
        print("usuario perdeu")