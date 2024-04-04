litro = float(input("digite a quantidade de litros: "))
mililitro = float(input("digite a quantidade de mililitros: ")) 
centilitros = float(input("digite a quantidade de centilitros: "))

op1 = litro
op2 = mililitro
op3 = centilitros

opcao = str(input(f"pfvr escolha uma das opcoes  op1 , op2 , op3 : "))

if opcao == "op1":
    litro1 = litro / 1000
    print(litro1)
elif opcao == "op2":
    mililitro1 = litro * 1000
    print(mililitro1)
elif opcao == "op3":
    centilitros1 = litro * 100
    print(centilitros1)
else:
    print("opcao invalida")