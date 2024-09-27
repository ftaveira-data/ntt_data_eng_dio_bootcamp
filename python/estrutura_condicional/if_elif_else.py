#Exemplo 1

MAIOR_IDADE = 18
IDADE_ESPECIAL = 1717

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

if idade < MAIOR_IDADE:
    print("Não é maior de idade, não pode tirar")


#Exemplo 2 

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
else:
    print("Ainda não pode tirar a CNH.")


#Exemplo 3 

if idade >= MAIOR_IDADE:
    print("Maior de Idade, pode tirar a CNH")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Ainda não pode tirar a CNH")