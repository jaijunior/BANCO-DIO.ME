menu = """
	[1] - Deposito
	[2] - Saque
	[3] - Consultar Extrato
"""
SAQUE_MAXIMO 	= 500
LIMITE_SAQUES 	= 3

saques	= 0
saldo 	= 500
extrato	= []

def deposito(valor: float):
	if valor > 0:
		global saldo
		saldo += valor
		extrato.append(f"|Deposito realizado no valor de R${valor:.2f}\n|Saldo -------> R${saldo:.2f}|")
		return f"Deposito de R${valor:.2f} realizado com sucesso!"
	else:
		return "Insira um valor maior do que 0(Zero)"

def saque(valor: float):
	if valor <= 0:
		return "Insira um valor maior do que 0(Zero)"

	if valor > SAQUE_MAXIMO:
		return f"O límite por saque é igual a {SAQUE_MAXIMO}, tente novamente"

	global saques
	if saques > 2:
		return f"Você ja realizou {saques} saques que é o limite"

	global saldo
	if (saldo - valor) < 0:
		return f"Você não tem saldo suficiente para o saque"

	saldo -= valor
	extrato.append(f"|Saque realizado no valor de R${valor:.2f}\m|Saldo -------> R${saldo:.2f}|")
	saques += 1
	return f"Saque de R${valor:.2f} realizado com sucesso"

def mostraExtrato(extrato):
	print("|-----------------------------------------|")
	print("|---------------EXTRATO-------------------|")
	for x in extrato:
		print(f"{x}\n")


while True:
	opcao = input(menu)

	if opcao == "1":
		valor = float(input("Informe o valor do Deposito: "))
		print(deposito(valor))

	elif opcao == "2":
		valor = float(input("Informe o valor do Saque: "))
		print(saque(valor))

	elif opcao == "3":
		mostraExtrato(extrato)


