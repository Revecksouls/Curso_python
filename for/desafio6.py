primeiro_termo = int(input("digite um termo: "))
razao = int(input("digite a razao: "))

ultimo_termo = (primeiro_termo + (10 - 1) * razao) + razao

for elemento in range (primeiro_termo,ultimo_termo,razao):
    print(elemento, end="-> ")
    