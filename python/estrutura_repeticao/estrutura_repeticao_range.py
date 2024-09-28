# Exemplo utilizando iteravel 
texto = input("Digite uma palavra: ")
VOGAIS = "AEIOU"


for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()


# Exemplo com a funcao bult-in de range, o primeiro numero start, segundo finish, terceiro o step.

for numero in range(0, 51, 5):
    print(numero, end=" ")


