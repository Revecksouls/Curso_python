try: 
    nome = input("digite o seu nome: ")
    idade = int(input("digite sua idade: "))
except ValueError:
    print("digite a sua idade com valor numerico")
    
else: 
    print("cadastro concluido!")