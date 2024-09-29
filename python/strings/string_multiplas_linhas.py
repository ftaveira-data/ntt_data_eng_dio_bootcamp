# Strings de multiplas linhas sao definidas informando 3 aspas simples ou duplas durante a atribuicao. Elas podem ocupar varias linhas do codigo, e todos os espacos em branco sao incluidos na string final.


nome = "Francisco"

mensagem_1 = f"""
Ola meu nome é {nome}, e estou
fazendo o bootcamp
da NTT DATA"""

print(mensagem_1)

mensagem_2 = f'''
Ola agora estou testando com aspas
simples,
meu nome é {nome}
'''

print(mensagem_2)


