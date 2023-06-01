import json

class Autentication():
    
    def __init__(self, cpf, senha):

        self.cpf = cpf
        self.senha = senha

def fazer_login():
    with open('users.json', 'r') as arquivo:
        dados = json.load(arquivo)
    
    cpf = input=("CPF: ")
    senha = input("Senha: ")

    for usuario in dados: 
        if usuario['cpf'] == cpf and usuario['senha'] == senha:
            print('Login bem-sucedido!')
            return
        print("Credenciais inválidas")

class Menu():
    
    

    def exibir_menu():
        print("\n===== ATM CASEIRO =====")
        print("1. Extrato\n")
        print("2. Saque\n")
        print("3. Depósito\n")
        print("4. Realizar Pagamento\n")
        print("5. Solicitar Crédito\n")
        print("0. Sair\n")
        print("================")

    def obter_opcao():
        opcao = input("Digite o número da opção desejada: ")
        return opcao
    
    def executar_opcao(opcao):
        if opcao == "1":
            print("O seu extrato: ")
        elif opcao == "2":
            print("Valor desejado do saque R$: ")
        elif opcao == "3":
            print("Valor desejado para depósito R$: ")
        elif opcao == "4":
            print("Realizar Pagamento de R$: ")
        elif opcao == "5":
            print("Qual valor você quer de crédito R$: ")
        elif opcao == "0":
            print("Adeus")
            exit()
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
    
    while True:
        exibir_menu()
        opcao = obter_opcao()
        executar_opcao(opcao)