frase = "microsoft power BI"

#trocando uma palavra 

troca_palavra = frase.replace("power BI","AZ-900")

print(troca_palavra)

#deixa tudo em letra maiusculas
print(frase.upper())

#deixa tudo minusculo
print(frase.lower())

#deixa a primeira letra maiuscula 
print(frase.capitalize())

#deixa todas as frases com suas letras maiusculas 
print(frase.title())

#removendo espaços desnecessarios 
espaço = "escola        legal     demais    uau    ."

Sespaco = espaço.strip()
print(Sespaco)

Sespaco = espaço.rstrip()
print(Sespaco)

Sespaco = espaço.lstrip()
print(Sespaco)