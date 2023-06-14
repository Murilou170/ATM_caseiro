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
            dados = jimport json

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

        with open(wh) as js:
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
    
    def deleteUser():
        wh = "Projeto4/ATM_caseiro/users.json"

        with  open(wh) as js:
            usersList = json.load(js)

        aDeletar = input("Qual seria o nome do usuario a ser deletado?  ->\t")

        for i in range(len(usersList)):
            if usersList[i]['nome'] == aDeletar:
                usersList.pop(i)
                print("\n\nMenos uma conta pra vc gerenciar!!\n\n")

        with open(wh, "w") as js:
            json.dump(usersList, js, indent=4)

        



    



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


class MenuGerente():
    def __init__(self):
        pass


    def exibir_menu():
        print("\n===== ATM CASEIRO =====")
        print("1. Criar Conta\n")
        print("2. Remover Conta\n")
        print("3. Atualizar Conta\n")
        print("4. Visualizar Conta\n")
        print("0. Sair\n")
        print("================")

    def obter_opcao():
        opcao = input("Digite o número da opção desejada: ")
        return opcao
    
    def executar_opcao(opcao):import json

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

        with open(wh) as js:
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
    
    def deleteUser():
        wh = "Projeto4/ATM_caseiro/users.json"

        with  open(wh) as js:
            usersList = json.load(js)

        aDeletar = input("Qual seria o nome do usuario a ser deletado?  ->\t")

        for i in range(len(usersList)):
            if usersList[i]['nome'] == aDeletar and usersList[i]['saldo'] == 0:
                usersList.pop(i)
                print("\n\nMenos uma conta pra vc gerenciar!!\n\n")
            if usersList[i]['nome'] == aDeletar and usersList[i]['saldo'] != 0:
                    print("\n\nNão foi possível deletar o usuário...saldo diferente de 0\n\n")

        with open(wh, "w") as js:
            json.dump(usersList, js, indent=4)

        print("\n\nUsuário deletado com Sucesso!\n\n")

    def updateUser():
        wh = "Projeto4/ATM_caseiro/users.json"

        with  open(wh) as js:
            usersList = json.load(js)
        

        print("\n\n1. Atualizar Nome\n")
        print("2. Atualizar CPF\n")
        print("3. Atualizar Endereço\n")
        print("4. Atualizar Senha\n")


        opcao = input("\nDigite o número da opção desejada: ")


        if opcao == "1":

            nomeAntigo = input("Digite nome atual do cliente: ")
            nomeNovo = input("Digite o novo nome do cliente: ")
            for i in range(len(usersList)):
                if usersList[i]['nome'] == nomeAntigo:
                    usersList[i]['nome'] = nomeNovo
            
        elif opcao == "2":

            cpfAntigo = input("Digite cpf atual do cliente: ")
            cpfNovo = input("Digite o novo cpf do cliente: ")
            for i in range(len(usersList)):
                if usersList[i]['cpf'] == cpfAntigo:
                    usersList[i]['cpf'] = cpfNovo

        elif opcao == "3":

            Antigo = input("Digite endereço atual do cliente: ")
            Novo = input("Digite o novo endereço do cliente: ")
            for i in range(len(usersList)):
                if usersList[i]['endereco'] == Antigo:
                    usersList[i]['endereco'] = Novo

        elif opcao == "4":

            Antigo = input("Digite senha atual do cliente: ")
            Novo = input("Digite a nova senha do cliente: ")
            for i in range(len(usersList)):
                if usersList[i]['senha'] == Antigo:
                    usersList[i]['senha'] = Novo

        with open(wh, "w") as js:
            json.dump(usersList, js, indent=4)
        
        print("\n\nDados atualizados com Sucesso!\n\n")
        


        

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


class MenuGerente():
    def __init__(self):
        pass


    def exibir_menu():
        print("\n===== ATM CASEIRO =====")
        print("1. Criar Conta\n")
        print("2. Remover Conta\n")
        print("3. Atualizar Conta\n")
        print("4. Visualizar Conta\n")
        print("0. Sair\n")
        print("================")

    def obter_opcao():
        opcao = input("Digite o número da opção desejada: ")
        return opcao
    
    def executar_opcao(opcao):
        bc = BancoDeDados()import json

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
        foundClient = False
        gerente = False
        
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

        with open(wh) as js:
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
    
    def deleteUser():
        wh = "Projeto4/ATM_caseiro/users.json"

        with  open(wh) as js:
            usersList = json.load(js)

        aDeletar = input("Qual seria o nome do usuario a ser deletado?  ->\t")

        for i in range(len(usersList)):
            if usersList[i]['nome'] == aDeletar and usersList[i]['saldo'] == 0:
                usersList.pop(i)
                print("\n\nMenos uma conta pra vc gerenciar!!\n\n")
            if usersList[i]['nome'] == aDeletar and usersList[i]['saldo'] != 0:
                    print("\n\nNão foi possível deletar o usuário...saldo diferente de 0\n\n")

        with open(wh, "w") as js:
            json.dump(usersList, js, indent=4)

        print("\n\nUsuário deletado com Sucesso!\n\n")

    def updateUser():
        wh = "Projeto4/ATM_caseiro/users.json"

        with  open(wh) as js:
            usersList = json.load(js)
        

        print("\n\n1. Atualizar Nome\n")
        print("2. Atualizar CPF\n")
        print("3. Atualizar Endereço\n")
        print("4. Atualizar Senha\n")


        opcao = input("\nDigite o número da opção desejada: ")


        if opcao == "1":

            nomeAntigo = input("Digite nome atual do cliente: ")
            nomeNovo = input("Digite o novo nome do cliente: ")
            for i in range(len(usersList)):
                if usersList[i]['nome'] == nomeAntigo:
                    usersList[i]['nome'] = nomeNovo
            
        elif opcao == "2":

            cpfAntigo = input("Digite cpf atual do cliente: ")
            cpfNovo = input("Digite o novo cpf do cliente: ")
            for i in range(len(usersList)):
                if usersList[i]['cpf'] == cpfAntigo:
                    usersList[i]['cpf'] = cpfNovo

        elif opcao == "3":

            Antigo = input("Digite endereço atual do cliente: ")
            Novo = input("Digite o novo endereço do cliente: ")
            for i in range(len(usersList)):
                if usersList[i]['endereco'] == Antigo:
                    usersList[i]['endereco'] = Novo

        elif opcao == "4":

            Antigo = input("Digite senha atual do cliente: ")
            Novo = input("Digite a nova senha do cliente: ")
            for i in range(len(usersList)):
                if usersList[i]['senha'] == Antigo:
                    usersList[i]['senha'] = Novo

        with open(wh, "w") as js:
            json.dump(usersList, js, indent=4)
        
        print("\n\nDados atualizados com Sucesso!\n\n")

    def visualizarUsuario():
        wh = "Projeto4/ATM_caseiro/users.json"

        with  open(wh) as js:
            usersList = json.load(js)

        aProcurar = input("Qual seria o nome do usuario a ser buscado?  ->\t")

        for i in range(len(usersList)):
            if usersList[i]['nome'] == aProcurar:
                print(usersList[i])
        


        

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


class MenuGerente():
    def __init__(self):
        pass


    def exibir_menu():
        print("\n===== ATM CASEIRO =====")
        print("1. Criar Conta\n")
        print("2. Remover Conta\n")
        print("3. Atualizar Conta\n")
        print("4. Visualizar Conta\n")
        print("0. Sair\n")
        print("================")

    def obter_opcao():
        opcao = input("Digite o número da opção desejada: ")
        return opcao
    
    def executar_opcao(opcao):
        bc = BancoDeDados()

        if opcao == "1":
            print("Ok!\n\n")
            bc.addUser()
        
        elif opcao == "2":
            print("Vish!!Blz...\n\n")
            bc.deleteUser()
    
        elif opcao == "3":
            bc.updateUser()
        
        elif opcao == "4":
            bc.visualizarUsuario()

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

        if opcao == "1":
            print("Ok!\n\n")
            bc.addUser()
        
        elif opcao == "2":
            print("Vish!!Blz...\n\n")
            bc.deleteUser()
    
        elif opcao == "3":
            print("Valor desejado para depósito R$: ")
        elif opcao == "4":
            print("Realizar Pagamento de R$: ")
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
        bc = BancoDeDados()

        if opcao == "1":
            print("Ok!\n\n")
            bc.addUser()
        
        elif opcao == "2":
            print("Valor desejado do saque R$: ")
    
        elif opcao == "3":
            print("Valor desejado para depósito R$: ")
        elif opcao == "4":
            print("Realizar Pagamento de R$: ")
        elif opcao == "0":
            print("Adeus")
            exit()
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
    def loop(self):
        while True:
            self.exibir_menu()
            opcao = self.obter_opcao()
            self.executar_opcao(opcao)son.load(arquivo)
        
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
