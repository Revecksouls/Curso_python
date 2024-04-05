rodadas = 0
rodadas1 = 1
numeros1 = 0 

while True:
    numeros = float(input("pfvr digite os numeros desejados: "))
    continuar = input("deseja continuar [S/N]: ").upper()
    numeros1 = numeros1 + numeros
    rodadas = rodadas + rodadas1 
    
    if continuar == "S":
        media = (numeros1) / (rodadas)
        
    elif continuar == "N":
        print("FIM DO PROGRAMA")
        print(media)
        break