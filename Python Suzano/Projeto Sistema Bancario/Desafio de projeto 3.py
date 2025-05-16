import textwrap
from datetime import datetime
from abc import ABC, abstractmethod



class Cliente:

    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class Pessoafisica(Cliente):
    def __init__(self, nome, endereco, cpf, data_nascimento):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "13254"
        self._historico = Historico()
        self.cliente = cliente

    @classmethod
    def nova_conta(cls,numero, cliente):
        return cls(numero, cliente )

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self._saldo
        execedeu_saldo = valor > saldo

        if execedeu_saldo:
            print("**Valor do saldo excedido, gentileza verificar saldo**")

        elif valor > 0:
            self._saldo -= valor
            print("*Saque realizado*")
            return True

        else:
            print("**Operação invalida**")

        return False

    def depositar(self, valor):

        if valor > 0:
            self._saldo += valor
            print("*Deposito realizado com sucesso*")
            return True
        else:
            print("**Valor para deposito invalido, reiniciar operação**")
        return False


class ContaCorrente(Conta):
        def __init__(self, numero, cliente, limite=500, limite_saque=3):
            super().__init__(numero, cliente)
            self.limite = limite
            self.limite_saque = limite_saque

        def __str__(self):
            return f"Conta {self.numero} | Agência: {self.agencia} | Saldo: R${self.saldo:.2f} | Cliente: {self.cliente.nome}"


        def sacar(self, valor):
            numero_saques = len(
                [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
            )
            execedeu_limite = valor > self.limite
            execedeu_saque = numero_saques >= self.limite_saque

            if execedeu_limite:
                print("**Valor limite por saque atingido, verifique e tente novamente**")

            elif execedeu_saque:
                print("**Quantidade maxima de saques atingida**")

            else:
                return super().sacar(valor)

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def add_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M")
        })

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        operacao_realizada = conta.depositar(self.valor)

        if operacao_realizada:
            conta.historico.add_transacao(self)


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        operacao_realizada = conta.sacar(self.valor)

        if operacao_realizada:
            conta.historico.add_transacao(self)


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

def deposito(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtro_clientes(cpf, clientes)

    if not cliente:
        print("**Cliente não localizado, verifique o CPF e tente novamente**")
        return

    valor = float(input("Insira o valor para Deposito: R$ "))
    transacao = Deposito(valor)

    conta = recuperar_conta_clientes(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtro_clientes(cpf, clientes)

    if not cliente:
        print("**Cliente não localizado, verifique o CPF e tente novamente**")
        return

    valor = float(input("Insira o valor para saque: R$ "))
    transacao = Saque(valor)

    conta = recuperar_conta_clientes(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    cpf = input("Insira o CPF: ")
    clientes = filtro_clientes(cpf, clientes)

    if not clientes:
        print("**Cliente não localizado, verifique o CPF**")
        return

    conta = recuperar_conta_clientes(clientes)
    if not conta:
        return

    print("====== EXTRATO ======")

    transacoes = conta.historico.transacoes
    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas transações"
    else:
        for transacao in transacoes: extrato += f"\n{transacao['tipo']}: R${transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo: R${conta.saldo:.2f}")
    print('=' * 20)


def novo_cliente(clientes):
    cpf = input("Insira o CPF completo (Somente os numero)")
    cliente = filtro_clientes(cpf, clientes)

    if cliente:
        print("\n**Usario ja existente**\n")
        return

    nome = input("Insira o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("informe seu endereço (Rua, numero, cidade/UF):")

    cliente = Pessoafisica(nome=nome,cpf=cpf , data_nascimento=data_nascimento, endereco=endereco)
    clientes.append(cliente)

    print("Cliente cadastrado com sucesso")

def filtro_clientes(cpf, clientes):
    filtro = [cliente for cliente in clientes if cliente.cpf == cpf]
    return filtro[0] if filtro else None

def recuperar_conta_clientes(cliente):
    if not cliente.contas:
        print("\n**Cliente não possui conta**")
        return

    return cliente.contas[0]

def nova_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do titular: ")
    cliente = filtro_clientes(cpf, clientes)

    if not clientes:
        print("Usuário não encontrado! Crie um novo usuário antes de abrir uma conta.")
        return
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)
    print("\n*Conta criada com sucesso*")

def listar_contas(contas):
    if not contas:
        print("Nenhuma conta encontrada.")
        return

    for conta in contas:
        print("=" * 50)
        print(textwrap.dedent(str(conta)))

def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            deposito(clientes)

        elif opcao == "2":
             sacar(clientes)

        elif opcao == "3":
            exibir_extrato(clientes)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            nova_conta(numero_conta, clientes, contas)

        elif opcao == "5":
            novo_cliente(clientes)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            print("Obrigado por utilizar nossos serviços!")
            break

        else:
            print("Operação invalidada, tente novamente")



main()




