menu = """
	[1] - Deposito
	[2] - Saque
	[3] - Consultar Extrato
"""
MAX_SAQUE = 500
LIMITE_SAQUES = 3

saques = 0
saldo = 500
extrato = []
valor = 0


while True:
	opcao = input(menu)

	if opcao == "1":
		valor = float(input("Informe o valor do Deposito:"))

		if valor > 0:
			saldo += valor
			extrato.append(f"|Deposito realizado no valor de R${valor:.2f}\n|Saldo ---------> {saldo:.2f}|")
			print(f"Deposito no valor de R${valor:.2f} realizado com sucesso")
			valor = 0;

		else:
			print("Insira um valor maior do que 0(zero)")

	elif opcao == "2":
		valor = float(input("Informe o valor do Saque:"))

		if (valor > 0) and (saldo - valor) > 0:

			if valor <= MAX_SAQUE and saques <=2:
				saldo -= valor
				extrato.append(f"|Saque realizado no valor de R${valor:.2f}\n|Saldo --------> {saldo:.2f}|")
				print(f"Saque no valor de R${valor:.2f} realizado com sucesso")
				saques += 1
				valor = 0
			else:
				print(f"Você só pode sacar valor até R${MAX_SAQUE} e no máximo 3 saques")
		elif (saldo - valor) < 0:
			print(f"Você não tem R${valor:.2f} para sacar, seu saldo atual é de R${saldo:.2f}. Tente novamente")

		else:
			print("Insira um valor maior do que 0")

	elif opcao == "3":
		print("|-----------------------------------------|")
		print("|---------------EXTRATO-------------------|")
		for x in extrato:
			print(f"{x}\n")


