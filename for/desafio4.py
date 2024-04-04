import time
numero = int(input("digite o numero desejado: "))


print(f"a tabuada desejada foi a {numero}")
for tabuada in range(0,11,1):
    multi = numero * tabuada 
    print(f"{numero} x {tabuada} = {multi}")
    time.sleep(0.5)