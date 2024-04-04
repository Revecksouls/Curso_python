#importa a biblioteca de tempo 
#time.sleep() faz um codigo ter tempo de execucao como de 1 segundo
import time

inicio = 10
fim = -1
salto = -1
for elemento in range(inicio,fim,salto):
    print(elemento)
    time.sleep(1)
