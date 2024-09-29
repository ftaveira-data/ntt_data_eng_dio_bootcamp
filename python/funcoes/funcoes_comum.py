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


#Exemplo de funcao com return 

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero -1 
    sucessor = numero + 1

    return antecessor, sucessor

print(calcular_total([10,20,34])) #64
print(retorna_antecessor_e_sucessor(10)) #9 e 11 *args=valores vem em tupl



#Exemplo com *args=valores vem em tupla e **kwargs=valores vem em dicionario

def exibir_poema(data_extenso, *args, **kwargs):
    






