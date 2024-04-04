soma = 0

for maquina in range(0,501,1):
    maquina1 = maquina % 3
    impar = maquina % 2
    if maquina1 == 0 and impar == 1  :
        soma = soma + maquina
        print(maquina)
print(soma)