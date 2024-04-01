km = float(input("digite a velocidade:"))
ultrapassagem = (km - 80)
valor_multa = ultrapassagem * 7
if km < 80:
   print("sem multa")
else: 
    print("voce foi multado")
    print("voce ultrapassou",ultrapassagem,"km")
    print("sua multa foi de",valor_multa,"reais")