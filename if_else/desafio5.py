reta_A = int(input("digite o tamanho da reta A: "))  
reta_B = int(input("digite o tamanho da reta B: "))
reta_C = int(input("digite o tamanho da reta C: "))

soma_AB = reta_A + reta_B
soma_AC = reta_A + reta_C
soma_BC = reta_B + reta_C

if soma_AB > reta_C and soma_AC > reta_B and soma_BC > reta_A:
    print(" foi possivel forma um triangulo")
else:
    print("nao formado")