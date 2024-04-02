from random import choice
lista = ['papel', "pedra" , "tesoura"]
escolha = choice(lista)
print (escolha)

usuario = input("informe sua escolha: ")

if usuario == escolha:
    print("Deu empate")
    
elif escolha == "pedra" and usuario == "papel":
    print("maquina perdeu")
elif escolha == "papel" and usuario == "tesoura":
    print("maquina perdeu")
elif escolha == "tesoura" and usuario == "pedra":
    print("maquina perdeu")
    
elif escolha == "pedra" and usuario == "tesoura":
    print("usuario perdeu")
elif escolha == "tesoura" and usuario == "papel":
    print("usuario perdeu")    
elif escolha == "papel" and usuario == "pedra":
    print("usuario perdeu")