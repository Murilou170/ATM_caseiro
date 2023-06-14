import json

class User():
    def __init__(self, nome, cpf, endereco, senha):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.senha = senha


class Autentication():

    def __init__(self):
        self.cpf = ""
        self.senha = ""
        self.usuarioAutenticado = False
        self.gerenteAutenticado =  False

    def fazer_login(self):
        foundClient, gerente = False
        with open("Projeto4/ATM_caseiro/users.json", "r") as arquivo:
            dados = json.load(arquivo)
        
        self.cpf = str(input("CPF: "))
        self.senha = str(input("Senha: "))


        for usuario in dados:
            if usuario['cpf'] == self.cpf and usuario['senha'] == self.senha:

                if usuario['cpf'] == '00':
                    gerente = True
                    foundClient = True
                    break

                foundClient = True
                break

        if foundClient and not gerente:
            self.usuarioAutenticado = True
            print('Login bem-sucedido!')

        elif gerente:
            self.gerenteAutenticado = True
            print('Sudo Su bem-sucedido!')

        else:
            print("Credenciais inválidas")




class BancoDeDados():
    def __init__(self):
        pass

    def addUser():
        wh = "Projeto4/ATM_caseiro/users.json"
        usersList = []

        with open("Projeto4/ATM_caseiro/users.json") as js:
            usersList = json.load(js)

        nome = input("\nPor favor digite seu nome: ")
        cpf = input("\nPor favor digite seu CPF: ")
        endereco = input("\nPor favor digite seu endereco: ")
        senha = input("\nPor favor digite sua senha: ")

        newUser = User(nome,cpf,endereco,senha)
        convertUser = vars(newUser)


        usersList.append(convertUser)

        with open(wh,"w") as where:
            json.dump(usersList,where,indent=4)
        print("\n->\tUsuário Salvo!\n")

    



class MenuCliente():
    def __init__(self):
        pass


    def exibir_menu():
        print("\n===== ATM CASEIRO =====")
        print("1. hyhyhy\n")
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
    def loop(self):
        while True:
            self.exibir_menu()
            opcao = self.obter_opcao()
            self.executar_opcao(opcao)
