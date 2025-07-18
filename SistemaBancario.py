menu = """

[d] Depositar
[s] sacar
[e] Extrato
[q] Sair 

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")

        deposito = float(input(" Qual valor será depositado?"))

        if deposito > 0:
            saldo += deposito
            extrato += f"Deposito: R$ {deposito:.2f}\n"
            print(f"O valor será depositado e seu saldo após o saque será de R${saldo:.2f}. Selecione uma das opções abaixo:")
        
        else:
            print("O valor informado não pode ser depositado por, por favor informe um opção válida.")

    elif opcao == "s":
        print("Sacar")

        if numero_saques >= LIMITE_SAQUES:
            print(f"Você já atingiu o limite de {LIMITE_SAQUES} saques diários. Por favor, selecione uma das opções abaixo:")

        else:
            saque = float(input("Qual valor deseja sacar? "))

            if saque > 0 and saque <= saldo and saque <= limite:
                saldo -= saque
                extrato += f"Saque: R$ {saque:.2f}\n"
                numero_saques += 1
                print(f"Saque realizado com sucesso, seu saldo atual é de R${saldo:.2f}. Selecione uma das opções abaixo:")

            else:
                print(f"O valor de seu saque deve ser igual ou inferior ao seu saldo, que atualmente é de R${saldo}, além disso deverá respeitar o limite de R${limite}. Selecione uma das opções abaixo:")

    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("=============================")

    elif opcao == "q":
        print("Obrigado por utilizar nossos serviços! Até breve!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")