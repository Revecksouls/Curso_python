#fazendo o caminho do par 

from random import*

ponto = 0
ponto1 = 1
ganhando_par = 0

# escolha do usuario
while True:
    escolha_Usuario = str(input("escolha I/P: ")).upper()
    escolha_numero_usuario = int(input("Digite um numero: "))
    
       # print(escolha_numero_usuario)
    
    #maquina caminho impar 
    lista = randint(1,10)
    maquina = lista 
    print(lista)
    
    # ganhando da maquina
    soma = escolha_numero_usuario + lista 
    resto = soma % 2
    
    if escolha_Usuario == "P" and resto == 0 : 

        print(soma, "resultado par, voce ganhou" )
    else:
        print(soma,"resultado impar , maquina ganhou")
        break
    
    if escolha_Usuario == "I" and resto == 1 : 
        print(soma, "resultado impar, voce ganhou" )
    else:
        print(soma,"resultado par , maquina ganhou")
        
        break
    
    
    
    # if  escolha_Usuario == "I":
    #     escolha_numero_usuario = ganhando_impar % 2
    #     ganhando_impar = escolha_numero_usuario + lista
        
    #     print(escolha_numero_usuario)
    #     ganhando_impar % 2 
    #     impar = 1
    #     print(ganhando_impar, "voce ganhou")
    # else:
    #     print("resultado par , maquina ganhou")
    #     break