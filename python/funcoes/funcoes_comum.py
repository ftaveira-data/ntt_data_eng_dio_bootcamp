#Exemplo de funcao comum

def exibir_mensagem():
    print("Olá Mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome= "Chico"):
    print(f"Seja bem vindo {nome}")


exibir_mensagem()
exibir_mensagem_2(nome="Francisco") #preciso declarar a variavel em algum momento.
exibir_mensagem_3()
exibir_mensagem_3(nome="kid")