casa = float(input("Qual o valor da casa?: "))
salario = float(input("Qual o seu salario: "))
anos = int(input("Em quantos anos pretende pagar: "))
anual = anos / casa
meses = anual / 12 
percetual_salario = salario * 0.3
prestacao = meses / casa

if prestacao <= percetual_salario: 
    print("prestacao aprovada")
else:
    print("prestacao negada")
    