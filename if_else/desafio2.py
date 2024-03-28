km = float(input("digite a velocidade:"))
multa = (km - 80)
valor_multa = multa * 7
if km < 80:
   print("sem multa")
else: 
    print("voce foi multado")
    print("voce ultrapassou",multa,"km")
    print("sua multa foi de",valor_multa,"reais")