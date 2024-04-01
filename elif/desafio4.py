ano_nacimento = int(input("Qual o ano de nascimento: "))
ano_atual = int(input("ano atual: "))
idade = ano_atual - ano_nacimento
print(idade)
if idade <= 9:
    print("Voce e da classe mirim")
elif idade >= 10 and idade <= 14:
    print("Voce é da classe infantil")
elif idade >= 15 <= 19:
    print("voce e da classe junior")
elif idade >= 20 <= 24:
    print("voce e da classe senior")
else:
    print("voce e da classe master")
