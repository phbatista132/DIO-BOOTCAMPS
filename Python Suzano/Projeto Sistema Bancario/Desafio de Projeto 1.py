#CONSTANTES
NUM_AGENCIA = "0001"
LIMITE_SAQUES = 1

def menu():
    menu_interativo = """\n
    [1] Deposito,
    [2] Saque,
    [3] Extrato,
    [4] Criar Conta,
    [5] Novo Usuario,
    [6] Listar contas
    [0] Sair,
    => """
    return input (menu_interativo)

def deposito(saldo, valor, extrato,/):

    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R${valor:.2f}\n"
    else:
        print("Insira um valido para o deposito!")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

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

    return saldo, extrato

def exibir_extrato(saldo,/,*, extrato):
    print("====== EXTRATO ======")
    print("Sem transações realizadas." if not extrato else extrato)
    print(f"\n Saldo:  R${saldo:.2f}")
    print("=====================")

def novo_usuarios(usuarios):
    cpf = input("Insira o CPF completo (Somente os numero)")
    usuarios = filtro_usuarios(cpf, usuarios )

    if usuarios:
        print("\nUsario ja existente!\n")

    nome = input("Insira o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("informe seu endereço (Rua, numero, cidade/UF):")

    usuarios.append({"cpf": cpf, "nome": nome, "data_nascimento:": data_nascimento, "endereço": endereco})

def filtro_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if ["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def nova_conta(agencia, num_conta, usuarios):
    cpf = input("Informe o CPF do titular: ")
    usuarios = filtro_usuarios(cpf, usuarios)

    if usuarios:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "num_conta": num_conta, "usuarios": usuarios}

    print("Conta ja existente para esse CPF, verifique o CPF e tente novamente")

def listar_contas(contas):
    for contas in contas:
        linha = f"""
            Agência:\t{contas["agencia"]},
            C/C:\t\t{contas["num_conta"]},
            Nome:\t\t{contas["usuario"]["nome"]}
        """
        print("=" * 50)
        print(linha)

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Insira o valor do deposito: R$ "))

            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == "2":
             valor = float(input("Insira o valor a ser sacado: R$"))

             saldo, extrato = sacar(saldo=saldo,
                                   valor=valor,
                                   extrato=extrato,
                                   limite=limite,
                                   numero_saques=numero_saques,
                                   limite_saques=LIMITE_SAQUES)

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = nova_conta(NUM_AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            novo_usuarios(usuarios)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            print("Obrigado por utilizar nossos serviços!")
            break

        else:
            print("Operação invalidada, tente novamente")



main()
