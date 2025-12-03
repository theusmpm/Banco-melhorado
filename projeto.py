from datetime import date
from getpass import getpass

# ================== CADASTRO DE USUÁRIO ==================

def cadastrar_usuario(usuarios):
    print("\n===== CADASTRO DE NOVO CLIENTE =====")
    cpf = input("CPF (somente números): ")

    if cpf in usuarios:
        print("Já existe um usuário cadastrado com esse CPF.")
        return usuarios

    nome = input("Nome : ")
    sobrenome = input("Sobrenome: ")
    cidade = input("Cidade: ")
    estado = input("Estado (UF): ")
    celular = input("Celular: ")
    email = input("Digite seu email: ")
    senha = getpass("Crie uma senha: ")
    

    usuarios[cpf] = {
        "nome": nome,
        "sobrenome": sobrenome,
        "cidade": cidade,
        "estado": estado,
        "celular": celular,
        "email": email,
        "senha": senha,
        "saldo": 0,
        "extrato": []
    }

    print(f"\nUsuário {nome} cadastrado com sucesso!")
    return usuarios


# ================== LOGIN ==================

def login_usuario(usuarios):
    print("\n===== LOGIN =====")
    cpf = input("CPF: ")

    if cpf not in usuarios:
        print("CPF não encontrado! Faça o cadastro primeiro.")

        
        return None

    senha = getpass("Senha: ")

    if senha == usuarios[cpf]["senha"]:
        print(f"\nBem-vindo, {usuarios[cpf]['nome']}!")
        return cpf
    else:
        print("Senha incorreta!")
        return None


# ================== MENU ==================

def mostrar_menu():
    print("""
================ MENU ================
1 - Depósito
2 - Saque
3 - Extrato
4 - Voltar ao Menu
======================================
    """)

# ================== OPERAÇÕES ==================

def depositar(usuario):
    print("\nDEPÓSITO")
    valor = float(input("Valor do depósito: R$ "))

    if valor <= 0:
        print("Valor inválido!")
        return

    usuario["saldo"] += valor
    usuario["extrato"].append(f"Depósito: +R$ {valor:.2f}")
    print("Depósito realizado com sucesso!")


def sacar(usuario, limite=500):
    print("\nSAQUE")
    valor = float(input("Valor do saque: R$ "))

    if valor <= 0:
        print("Valor inválido!")
    elif valor > limite:
        print("Limite máximo por saque é R$ 500!")
    elif valor > usuario["saldo"]:
        print("Saldo insuficiente!")
    else:
        usuario["saldo"] -= valor
        usuario["extrato"].append(f"Saque: -R$ {valor:.2f}")
        print("Saque realizado com sucesso!")


def mostrar_extrato(usuario):
    print("\n========== EXTRATO ==========")
    if not usuario["extrato"]:
        print("Nenhuma movimentação registrada.")
    else:
        for item in usuario["extrato"]:
            print(item)
    print(f"\nSaldo atual: R$ {usuario['saldo']:.2f}")
    print("==============================\n")


# ================== MAIN ==================

def main():
    usuarios = {}  # Banco de dados de clientes

    print("Bem-vindo ao Banco DIO.me")

    while True:
        print("""
==== MENU INICIAL ====
1 - Cadastrar novo cliente
2 - Fazer login
3 - Sair
        """)

        opcao = input("Escolha: ")

        if opcao == "1":
            usuarios = cadastrar_usuario(usuarios)

        elif opcao == "2":
            cpf = login_usuario(usuarios)
            if cpf:
                sistema_bancario(usuarios[cpf])

        elif opcao == "3":
            print("Saindo... Obrigado por escolher a DIO.me !")
            break

        else:
            print("Opção inválida!")


# ================== SISTEMA BANCÁRIO ==================

def sistema_bancario(usuario):
    hoje = date.today().strftime("%d/%m/%Y")

    while True:
        print(f"\nOperações bancárias - {usuario['nome']} - {hoje}")
        mostrar_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            depositar(usuario)
        elif opcao == "2":
            sacar(usuario)
        elif opcao == "3":
            mostrar_extrato(usuario)
        elif opcao == "4":
            print("Voltando ao menu inicial...")
            break
        else:
            print("Opção inválida!")


main()
