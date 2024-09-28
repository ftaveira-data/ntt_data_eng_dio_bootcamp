#Exemplo 1 - tamanho das letras
nome = "Guilherme"

print(nome.upper())
print(nome.lower())
print(nome.title())


#Exemplo 2 - Espaços

texto = " Olá Mundo! "
print(texto + ".")
print(texto.strip() + ".")
print(texto.lstrip() + ".")
print(texto.rstrip() + ".")


#Exemplo 3 - Center
menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))
print(menu.center(8, "#"))
print(menu.center(20, "#"))

#Exemplo 4 - Join

print("P-y-t-h-o-n")
print("-".join(menu))