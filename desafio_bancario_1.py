extrato = ""
saldo = 0
limite_conta = 500
numero_saques = 0
MAXIMO_SAQUES_DIARIO = 3

selecao = """

[d] Deposito
[s] Saque
[e] Extrato
[q] Sair

* """

while True:

    opcao = input(selecao)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação não concluida! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite_conta

        excedeu_saques = numero_saques >= MAXIMO_SAQUES_DIARIO

        if excedeu_saldo:
            print("Operação não concluida! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação não concluida! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação não concluida! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação não concluida! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
