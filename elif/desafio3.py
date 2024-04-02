nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a primeira nota: "))
media_final = (nota1 + nota2) / 2

if nota1 >= 0 and nota1 <= 10 and nota2 >= 0 and nota2 <=10:
    print("Pfvr nos informe uma nota valida")

    if media_final >= 7:
        print(f"Parabens voce foi aprovado, sua nota foi {media_final}.")
    elif media_final >= 5 <= 6.9:
        print(f"Voce esta em recuperação sua nota foi {media_final}")
    else:
        print(f"Desculpe, voce foi reprovado, sua nota foi {media_final}")