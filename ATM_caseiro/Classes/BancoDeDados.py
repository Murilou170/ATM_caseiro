import json
from ATM_caseiro.Classes.Auth import User


class Banco():
    def __init__(self):
        pass


    def saque(self,cpf,valor):
        wh = "Projeto4/ATM_caseiro/users.json"
        usersList = []

        with open(wh) as js:
            usersList = json.load(js)
        
        for i in range(len(usersList)):

            atualcpf = usersList[i][f'cpf']
            atualsaldo = usersList[i]['saldo']
            atualcredito = usersList[i]['credito']
            
            if atualcpf == cpf and valor < atualsaldo + atualcredito:
                atualsaldo -= int(valor)

                if atualsaldo < 0:
                    atualsaldosaldo += atualcredito
                    atualcredito = 0
        
                print("\n\tSaque efetuado com Sucesso!\n")
    
            elif usersList[i][f'cpf'] == cpf and valor > usersList[i]['saldo'] + usersList[i][f'credito']:
                print("\nNão há dinheiro o suficiente, o seu saldo não foi alterado.\n")
        
        with open(wh,"w") as where:
            json.dump(usersList,where,indent=4)


    def deposito(self,cpf,valor):
            wh = "Projeto4/ATM_caseiro/users.json"
            usersList = []

            with open(wh) as js:
                usersList = json.load(js)
            
            for i in range(len(usersList)):
                if usersList[i][f'cpf'] == cpf:
                    usersList[i][f'saldo'] += valor
                    print("\n\tDepósito efetuado com Sucesso!\n")
            
            with open(wh,"w") as where:
                json.dump(usersList,where,indent=4)

    def pagamento(self,valor,fromcpf,tocpf):

        self.saque(fromcpf,valor)
        self.deposito(tocpf,valor)
        print("\n\tPagamento Realizado com sucesso!\n")

    def pedirCredito(self,cpf,valor):
        wh = "Projeto4/ATM_caseiro/users.json"
        usersList = []

        with open(wh) as js:
            usersList = json.load(js)
        
        for i in range(len(usersList)):
            if usersList[i][f'cpf'] == cpf and valor <= usersList[i]['saldo'] and not bool(usersList[i][f'credito']):
                usersList[i][f'credito'] += valor
                print("\n\tDepósito de crédito efetuado com Sucesso!\n")
            elif usersList[i][f'cpf'] == cpf and valor > usersList[i]['saldo']:
                print("\n\tO credito requisitado é maior do que o saldo atual. Credito não concedido.\n")

        with open(wh,"w") as where:
            json.dump(usersList,where,indent=4)

    def addUser(self):
        wh = "Projeto4/ATM_caseiro/users.json"
        usersList = []

        with open(wh) as js:
            usersList = json.load(js)

        print("\n\t===== ATM CASEIRO =====")
        nome = input("\n\tPor favor digite seu nome: ")
        cpf = input("\n\tPor favor digite seu CPF: ")
        endereco = input("\n\tPor favor digite seu endereco: ")
        senha = input("\n\tPor favor digite sua senha: ")
        print("\t================")

        newUser = User(nome,cpf,endereco,senha)
        convertUser = vars(newUser)


        usersList.append(convertUser)

        with open(wh,"w") as where:
            json.dump(usersList,where,indent=4)
        print("\n->\tUsuário Salvo!\n")
    


    def deleteUser(self):
        wh = "Projeto4/ATM_caseiro/users.json"

        with  open(wh) as js:
            usersList = json.load(js)

        print("\n\t===== ATM CASEIRO =====")
        aDeletar = input("\tQual seria o nome do usuario a ser deletado?  ->\t")
        print("\t================")

        for i in range(len(usersList)):
            print(len(usersList))
            if usersList[i]['nome'] == aDeletar and usersList[i]['saldo'] == 0:
                
                usersList.pop(i)
                print("\n\n\tMenos uma conta pra vc gerenciar!!\n\n")

            elif usersList[i]['nome'] == aDeletar and usersList[i]['saldo'] != 0:
                    
                    print("\n\n\tNão foi possível deletar o usuário...saldo diferente de 0\n\n")

        with open(wh, "w") as js:
            json.dump(usersList, js, indent=4)
            print("\n\nUsuário deletado com Sucesso!\n\n")




    def updateUser(self):

        def wrapperUpdate(info,antigo,novo):
            for i in range(len(usersList)):
                if usersList[i][f'{info}'] == antigo:
                    usersList[i][f'{info}'] = novo

        wh = "Projeto4/ATM_caseiro/users.json"

        with  open(wh) as js:
            usersList = json.load(js)
        
        print("\n\t===== ATM CASEIRO =====")
        print("\n\n\t1. Atualizar Nome\n")
        print("\t2. Atualizar CPF\n")
        print("\t3. Atualizar Endereço\n")
        print("\t4. Atualizar Senha\n")
        print("\t================")


        opcao = input("\nDigite o número da opção desejada: ")


        
        if opcao == "1":
            print("\n\t===== ATM CASEIRO =====")
            Antigo = input("\tDigite nome atual do cliente: ")
            Novo = input("\tDigite o novo nome do cliente: ")
            print("\t================")

            wrapperUpdate('nome',Antigo,Novo)

            
        elif opcao == "2":
            print("\n\t===== ATM CASEIRO =====")
            Antigo = input("\tDigite cpf atual do cliente: ")
            Novo = input("\tDigite o novo cpf do cliente: ")
            print("\t================")

            wrapperUpdate('cpf',Antigo,Novo)

        elif opcao == "3":
            print("\n\t===== ATM CASEIRO =====")
            Antigo = input("\tDigite endereço atual do cliente: ")
            Novo = input("\tDigite o novo endereço do cliente: ")
            print("\t================")

            wrapperUpdate('endereco',Antigo,Novo)

        elif opcao == "4":
            print("\n\t===== ATM CASEIRO =====")
            Antigo = input("\tDigite senha atual do cliente: ")
            Novo = input("\tDigite a nova senha do cliente: ")
            print("\t================")

            wrapperUpdate('senha',Antigo,Novo)



        with open(wh, "w") as js:
            json.dump(usersList, js, indent=4)
            print("\n\nDados atualizados com Sucesso!\n\n")



    def visualizarUsuario(self):
        wh = "Projeto4/ATM_caseiro/users.json"

        with  open(wh) as js:
            usersList = json.load(js)
        print("\n\t===== ATM CASEIRO =====")
        aProcurar = input("\tQual seria o nome do usuario a ser buscado?  ->\t")
        print("\t================")

        for i in range(len(usersList)):
            if usersList[i]['nome'] == aProcurar:
                print(usersList[i])