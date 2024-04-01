prova = float(input("Digite a nota na prova do aluno 0 a 70: "))
atividade = float(input("digite a media das notas das atividades 0 a 30: "))

#NOTA PROVA = 70%
#nota atividades = 30% da media final

media_final = prova + atividade /2
print(media_final)

if media_final >= 50:
    print("Voce foi aprovado")
    print(media_final)
elif media_final >= 40:
    print("Recupercao")
    print(media_final)
else:
    ("voce foi reprovado")