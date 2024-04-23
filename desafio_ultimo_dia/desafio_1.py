while True:
    try:
        n1 = int(input("digite um valor: "))
        n2 = int(input("digite um valor: "))
        
        divisao = n1/n2 
    except ZeroDivisionError:
        print("Nao existe divisao por zero")
        
    except ValueError:
        print("Digite um valor numerico")
    else:
        print(f"Valor da divisão foi {divisao}")
        break