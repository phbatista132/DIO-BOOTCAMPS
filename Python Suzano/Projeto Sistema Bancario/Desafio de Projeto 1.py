menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("Informe o valor do deposito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R${valor:.2f}\n"
        else: 
            print("Valor invalido, insira um valor valido para a operação")
        
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Valor do saque excede o valor do saldo")
        
        elif excedeu_limite:
            print("Valor excede o valor limite do saque")
        
        elif excedeu_saques:
            print("Quantidade maxima de saque atingida")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1
            
        else:
            print("Falha na operação, insira um valor valido")
    
    elif opcao == "3":
        print("###### EXTRATO ######")
        print("Sem transações realizadas." if not extrato else extrato)
        print(f"\n Saldo:  R${saldo:.2f}")
        print("#####################")
    elif opcao == "0":
        break
    
    else: 
        print("Operação invalida, por favor, selecione novamente a operação desejada.") 