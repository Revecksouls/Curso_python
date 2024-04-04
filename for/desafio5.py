

# for n1 in range(1,7):
#     n2 = int(input("pfvr digite um numero: "))

#     n2 = n1 % 2
#     n1 == 0
#     print(n2)


soma = 0 

for elemento in range (1,7):
    numero = int(input("digite um valor: "))
    
    resto = numero % 2
    if resto == 0:
        soma = soma + numero
else:
    print(f"A soma dos valores pares digitados foi igual a {soma}")