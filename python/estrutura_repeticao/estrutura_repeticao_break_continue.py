while True:
    numero = int(input("Digite um numero: "))

    if numero == 10:
        print("numero secreto digitado") 
        break
    

    print(numero)



# Break com Range

for numero in range(100):

    if numero == 22:
        break

    print(numero, end=" ")

print()


# Usando o exemplo do Continue, pois pode pular uma situacao especifica dentro do laco

for numero in range(10):

    if numero == 7:
        continue

    print(numero, end=" ")

