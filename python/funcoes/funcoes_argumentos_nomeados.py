#Exemplo com argumentos nomeados

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", 1999, "ABC-1243")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1243")
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1243"}) #**kwargs=valores vem em dicionario