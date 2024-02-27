class ContaBancaria:
    def __init__(self, nome_cliente, cpf_cliente, saldo_inicial=0):
        self.nome_cliente = nome_cliente
        self.cpf_cliente = cpf_cliente
        self.saldo = saldo_inicial
        self.extrato = []

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.append(f"Depósito: +{valor}")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.extrato.append(f"Saque: -{valor}")
        else:
            print("Saldo insuficiente!")

    def transferir(self, outra_conta, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            outra_conta.depositar(valor)
            self.extrato.append(f"Transferência para {outra_conta.nome_cliente}: -{valor}")
        else:
            print("Saldo insuficiente para transferência!")

    def mostrar_extrato(self):
        print(f"Extrato de {self.nome_cliente} (CPF: {self.cpf_cliente}):")
        for operacao in self.extrato:
            print(operacao)
        print(f"Saldo atual: {self.saldo}")

    def excluir_conta(self):
        self.saldo = 0
        self.extrato = []
        print(f"Conta de {self.nome_cliente} excluída com sucesso!")

def criar_nova_conta():
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    saldo_inicial = float(input("Digite o saldo inicial: "))
    return ContaBancaria(nome, cpf, saldo_inicial)

def exibir_menu():
    print("\nMenu:")
    print("1. Criar Nova Conta")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Transferir")
    print("5. Mostrar Extrato")
    print("6. Excluir Conta")
    print("0. Sair")

# Lista para armazenar as contas criadas
contas = []

while True:
    exibir_menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nova_conta = criar_nova_conta()
        contas.append(nova_conta)
        print(f"Conta criada para {nova_conta.nome_cliente}.")
    elif opcao == 2:
        valor = float(input("Digite o valor para depósito: "))
        contas[-1].depositar(valor)  # Última conta criada
    elif opcao == 3:
        valor = float(input("Digite o valor para saque: "))
        contas[-1].sacar(valor)  # Última conta criada
    elif opcao == 4:
        valor = float(input("Digite o valor para transferência: "))
        outra_conta = int(input("Digite o índice da conta para transferir: "))
        contas[-1].transferir(contas[outra_conta], valor)  # Última conta criada
    elif opcao == 5:
        contas[-1].mostrar_extrato()  # Última conta criada
    elif opcao == 6:
        contas[-1].excluir_conta()  # Última conta criada
        break
    elif opcao == 0:
        break
    else:
        print("Opção inválida. Tente novamente.")
