
#And para ser true tudo precisa ser true
print(True and True)
print(True and False)
print(False and False)

#Or para ser true apenas 1 true é necessario. 
print(True or True)
print(True or False)
print(False or False)

saldo = 1000
saque = 250
limite = 200
conta_especial = True

expressao = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(expressao)

expressao_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(expressao_2)
