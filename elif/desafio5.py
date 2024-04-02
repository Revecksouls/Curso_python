reta_A = int(input("digite o tamanho da reta A: "))  
reta_B = int(input("digite o tamanho da reta B: "))
reta_C = int(input("digite o tamanho da reta C: "))

soma_AB = reta_A + reta_B
soma_AC = reta_A + reta_C
soma_BC = reta_B + reta_C

if soma_AB > reta_C and soma_AC > reta_B and soma_BC > reta_A:
    if reta_A == reta_B == reta_C:
        print("O triangulo formado foi o Equilatero")
        
    elif reta_A != reta_B != reta_C != reta_A:
        print("o triangulo formado foi o escaleno")
        
    else:
        print("O triangulo formado foi o isosceles")
        
else:
    print("nao foi possivel forma um triangulo")