# funcoes de parametros especiais = positional only or hibryd

def criar_carros(modelo, ano, placa, / , marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carros("Palio", 1999, "ABC-1234", "Fiat", "2.0", "Gasolina")

# keyword only

def criar_carro_2(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro_2(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")