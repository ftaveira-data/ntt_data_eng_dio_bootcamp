# Desafio do Sistema Bancário 

def depositar(saldo, extrato, valor):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor de depósito inválido.")
    return saldo, extrato

def sacar(saldo, extrato, numero_saques, valor, limite_saque, LIMITE_SAQUES_DIARIOS):
    if numero_saques >= LIMITE_SAQUES_DIARIOS:
        print("Limite de saques diários atingido.")
    elif valor > limite_saque:
        print("O valor do saque excede o limite permitido de R$ 500,00.")
    elif saldo < valor:
        print("Saldo insuficiente para realizar o saque.")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor de saque inválido.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    if len(extrato) == 0:
        print("Não foram realizadas movimentações.")
    else:
        print("\nExtrato:")
        for operacao in extrato:
            print(operacao)
    print(f"Saldo atual: R$ {saldo:.2f}")

def exibir_menu():
    print("\n===== Banco DIO =====")
    print("\n===== MENU =====")
    print("1. Depósito")
    print("2. Saque")
    print("3. Extrato")
    print("4. Sair")

# Loop principal do sistema bancário
def main():
    saldo = 0.0
    limite_saque = 500.0
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES_DIARIOS = 3

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor para depósito: "))
            saldo, extrato = depositar(saldo, extrato, valor)
        elif opcao == "2":
            valor = float(input("Digite o valor para saque: "))
            saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, valor, limite_saque, LIMITE_SAQUES_DIARIOS)
        elif opcao == "3":
            exibir_extrato(saldo, extrato)
        elif opcao == "4":
            print("Saindo do sistema. Obrigado por usar o Banco DIO!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o programa
if __name__ == "__main__":
    main()

