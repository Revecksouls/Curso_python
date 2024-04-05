#fazendo o caminho do par 

from random import*

ponto = 0
ponto1 = 1
ganhando_par = 0

# escolha do usuario
while True:
    escolha_Usuario = str(input("escolha I/P: ")).upper()
    escolha_numero_par = int(input("Digite um numero: "))
    par = escolha_numero_par % 2
    if par == 0:
        print(escolha_numero_par)
    
    #maquina caminho impar 
    lista = randint(1,10)
    maquina = lista 
    impar = lista % 3
    print(lista)
    
    # ganhando da maquina
    ganhando_par = escolha_numero_par + lista 
    
    if ganhando_par:
         
         
    