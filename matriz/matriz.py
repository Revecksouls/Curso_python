nome = input("pfvr digite o seu nome: ")
n1 = float(input("digite a primeira nota: "))
n2 = float(input("digite a segunda nota: "))
media = n1 + n2 / 2
 
situacao = media
if situacao >= 7:
    situacao = "aprovado"
else:
    situacao = "reprovado"
    
dc = [{
    
    "nome" : {nome},
    "media" : {media},
    "situação" : {situacao}
       
}]
print(dc)