# ano_nacimento = int(input("Qual o ano de nascimento: "))
# ano_atual = int(input("ano atual: "))
# idade = ano_atual - ano_nacimento
# print(idade)

from datetime import *

data_atual = date.today()
ano_atual = data_atual.year
ano_nascimento = int(input("Digite o ano do seu nascimento: "))
idade = ano_atual - ano_nascimento


if idade <= 9:
    print("Voce e da classe mirim")
elif idade <= 14:
    print("Voce é da classe infantil")
elif idade <= 19:
    print("voce e da classe junior")
elif idade <= 24:
    print("voce e da classe senior")
else:
    print("voce e da classe master")
