n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

if n1 > n2:
    print(f"o valor {n1} é o maior")
elif n2 > n1:
    print(f"o valor {n2} é o maior")
else:
    print("os dois valores sao iguais")