# Em python tudo é objeto, dessa forma funções tambem são objetos o que as tornam objetos de primeira classe.
# Com isso podemos atribuir funçoes a variaveis, passa-las como parametro para funções, usá-las como valores em estruturas de dados(listas, tuplas, dicionariso)
# e usar como valor de retorno para uma função (closures). 

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")

exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subtrair)
exibir_resultado(10, 10, multiplicar)
exibir_resultado(10, 10, dividir)
