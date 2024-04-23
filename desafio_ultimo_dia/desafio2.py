try: 
    with open("dados.txt","r") as arquivo:
        conteudo = arquivo.read()
except FileExistsError:
    print("SEU ARQUIVO NAO EXISTE")
else:
    print(conteudo)