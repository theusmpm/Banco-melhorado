from datetime import date
from getpass import getpass

# CLASSE CONTA BANCÁRIA
class ContaBancaria:
    def __init__(self, usuario):
        self.usuario = usuario
        self.saldo = 0
        self.extrato = []
        self.limite_saque = 500

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido! Tente novamente.")
            return

        self.saldo += valor
        self.extrato.append(f"Depósito: +R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido!")
            return
        if valor > self.saldo:
            print("Saldo insuficiente!")
            return
        if valor > self.limite_saque:
            print(f"Limite por saque é R$ {self.limite_saque:.2f}.")
            return

        self.saldo -= valor
        self.extrato.append(f"Saque: -R$ {valor:.2f}")
        print(f"Saque de R$ {valor:.2f} realizado!")

    def ver_extrato(self):
        print("\n===== EXTRATO =====")
        if not self.extrato:
            print("Nenhuma movimentação registrada.")
        else:
            for item in self.extrato:
                print(item)
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print("=====================\n")


# FUNÇÃO: CADASTRAR USUÁRIO
def cadastrar_usuario(usuarios):
    print("\n=== CADASTRO DE NOVO CLIENTE ===")
    
    cpf = input("CPF: ")
    if cpf in usuarios:
        print("Já existe um usuário com esse CPF!")
        return usuarios

    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    ano_nascimento = int(input("Ano de nascimento: "))
    cidade = input("Cidade: ")
    estado = input("UF: ")
    celular = input("Celular: ")
    email = input("Email: ")
    senha = getpass("Senha: ")

    usuarios[cpf] = {
        "nome": nome,
        "sobrenome": sobrenome,
        "ano_nascimento": ano_nascimento,
        "cidade": cidade,
        "estado": estado,
        "celular": celular,
        "email": email,
        "senha": senha,
        "conta": ContaBancaria(nome)
    }

    ano_atual = date.today().year
    age = ano_atual - ano_nascimento

    if age >= 18:
        print("CRÉDITO LIBERADO")
    elif 16 <= age <= 17:
        print("SOMENTE DÉBITO")
    else:
        print("IDADE IMPOSSIBILITA DE ABRIR CONTA NO BANCO DIO.me")
        return usuarios
    
    print(f"Usuário {nome} cadastrado com sucesso!")
    return usuarios 


# FUNÇÃO: LOGIN
def login_usuario(usuarios):
    print("\n=== LOGIN ===")

    cpf = input("CPF: ")

    if cpf not in usuarios:
        print("CPF não encontrado!")
        cadastrar = input("Deseja cadastrá-lo? (S/N): ").upper()
        if cadastrar == "S":
            cadastrar_usuario(usuarios)
            return None
        else:
            return None

    # Loop até senha correta
    for tentativa in range(3):
        senha = getpass("Senha: ")
        if senha == usuarios[cpf]["senha"]:
            print(f"\nBem-vindo, {usuarios[cpf]['nome']}!")
            return cpf
        else:
            print("Senha incorreta!")

    print("Muitas tentativas. Retornando ao menu.")
    return None


# SISTEMA BANCÁRIO
def sistema_bancario(conta):
    while True:
        hoje = date.today().strftime("%d/%m/%Y")
        print(f"\n=== BANCO DIO.me | {conta.usuario} | {hoje} ===")
        print("1 - Depósito")
        print("2 - Saque")
        print("3 - Extrato")
        print("4 - Voltar ao Menu")

        opcao = input("Escolha: ")

        if opcao == "1":
            valor = float(input("Valor para depósito: R$ "))
            conta.depositar(valor)

        elif opcao == "2":
            valor = float(input("Valor para saque: R$ "))
            conta.sacar(valor)

        elif opcao == "3":
            conta.ver_extrato()

        elif opcao == "4":
            print("Voltando ao menu inicial...")
            break

        else:
            print("Opção inválida!")


# MAIN
def main():
    usuarios = {}

    print("=== BEM-VINDO AO BANCO DIO.me ===")

    while True:
        print("""
        ===== MENU PRINCIPAL =====
        1 - Cadastrar novo usuário
        2 - Fazer login
        3 - Sair
        ==========================""")
        
        opcao = input("Escolha: ")

        if opcao == "1":
            usuarios = cadastrar_usuario(usuarios)

        elif opcao == "2":
            cpf = login_usuario(usuarios)
            if cpf:
                conta = usuarios[cpf]["conta"]
                sistema_bancario(conta)

        elif opcao == "3":
            print("Obrigado por usar o Banco DIO.me! Até logo.")
            break

        else:
            print("Opção inválida!")


main()
