


from datetime import * 

anoatual = date.today().year

dc= {
    
    "nome" : str(input("digite seu nome: ")),
    "ano de nascimento" : int(input("digite o ano do nascimento: ")),
    "carteira de trabalho" : int(input("carteira de tabalho : (0 se nao tem)"))
    
    
}

idade = anoatual - dc["ano de nascimento"]
del dc ["ano de nascimento"]
dc["idade"] = idade
print(dc)

if dc ["carteira de trabalho"] == 0:
    for k, v in dc.items():
        print(f" {k} = {v}")
        