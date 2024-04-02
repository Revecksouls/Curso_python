casa = float(input("Qual o valor da casa?: "))
salario = float(input("Qual o seu salario: "))
anos = int(input("Em quantos anos pretende pagar: ")) 

percetual_salario = salario * 0.3
meses = anos * 12 
prestacao_mensal = casa / meses 

if prestacao_mensal > percetual_salario:
    print("emprestimo negado")

else:
    print(f"Parabens, voce teve o emprestimo aprovado")

    