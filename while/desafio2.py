 
soma = 0

while True:
    numeros = int(input("pfvr digite os numeros desejados: "))
    
    if numeros == 999:
        break
    #atribuir numeros a soma contanto numero por numero digitado pelo usuario
    soma = numeros + soma
print(f"a soma dos numeros sao: {soma}")  