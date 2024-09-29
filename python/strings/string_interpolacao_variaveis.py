# Old Style PLaceholders, %S para valores do tipo string // %d para valores tipo inteiros // %f para valores float

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
profissao = input("Digite a sua profissao: ")
linguagem = input("Digite a sua linguagem preferida: ")

print("Olá eu me chamo %s. Eu tenho %d anos, minha profissão é %s e a linguagem que eu gosto de trabalhar é %s" % (nome, idade, profissao, linguagem)) 

# Metodo Format 

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
profissao = input("Digite a sua profissao: ")
linguagem = input("Digite a sua linguagem preferida: ")

print("Olá eu me chamo {}. Eu tenho {} anos, minha profissão é {} e a linguagem que eu gosto de trabalhar é {}" .format(nome, idade, profissao, linguagem))


# Metodo f-string

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
profissao = input("Digite a sua profissao: ")
linguagem = input("Digite a sua linguagem preferida: ")

print(f"Olá eu me chamo {nome}. Eu tenho {idade} anos, minha profissão é {profissao} e a linguagem que eu gosto de trabalhar é {linguagem}")

# Formatar strings com f-string

PI = 3.14159

print(f"Valor de PI: {PI: .2f}")
# Valor de PI: 3.14

print(f"Valor de PI: {PI:10.2f}")
# Valor de PI:         3.14