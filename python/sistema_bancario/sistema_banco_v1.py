# Desafio do Sistema Bancário 
conta_corrente = True
conta_poupanca = False
saldo = 5000


menu = "Banco DIO" 

print(menu.rjust(30).center(50, "-"))
print()


operacao = input("Escolha uma opção: ")

# saque = float(input"Valor do Saque: ")

# print()
# print()
# print(menu.center(14))
# print(menu.center(14, "#"))
# print(menu.center(8, "#"))
# print(menu.center(20, "#"))

# #Exemplo com *args=valores vem em tupla e **kwargs=valores vem em dicionario

# def exibir_poema(data_extenso, *args, **kwargs):
#     texto = "\n".join(args)
#     meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
#     mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
#     print(mensagem)


# exibir_poema("Domingo 30 de Setembro de 2024", "Zen of Python", "Beautiful is better than ugly.", autor="Tim Peters", ano=1990)


# nome = input("informe seu nome: ")
# idade = input("Informe sua idade: ")

# print(f"Seu nome é {nome}")
# print(nome, idade, end="...\n")
# print(nome, idade, sep="#")
# print(nome, idade)


# conta_normal = True
# conta_universitaria = False

# saldo = 2000
# saque = float(input("Informe o valor do saque: "))
# cheque_especial = 450

# if conta_normal:
#     if saldo >= saque:
#         print("Saque realizado com sucesso")
#     elif saque <= (saldo + cheque_especial):
#         print("Saque realizado com o uso do cheque especial!")
#     else: 
#         print("Saque não permitido, saldo insuficiente")
# elif conta_universitaria:
#     if saldo >= saque:
#         print("Saque realizado com sucesso")