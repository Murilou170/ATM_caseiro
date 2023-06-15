import datetime
import json
from ATM_caseiro.Classes.Auth import User


class Banco():
    def __init__(self):
        pass


    def saque(self,cpf,valor):
        wh = "ATM_caseiro/users.json"
        usersList = []

        with open(wh) as js:
            usersList = json.load(js)
        
        for i in range(len(usersList)):

            atualcpf = usersList[i][f'cpf']
            atualsaldo = usersList[i]['saldo']
            atualcredito = usersList[i]['credito']
            
            if atualcpf == cpf and valor <= atualsaldo + atualcredito:
                usersList[i]['saldo'] = atualsaldo - int(valor)
                

                if atualsaldo < 0:
                    usersList[i]['saldo'] += atualcredito
                    usersList[i]['credito'] = 0
                

                with open(wh,"w") as where:
                    json.dump(usersList,where,indent=4)
                
                print("\n\tSaque efetuado com Sucesso!\n")
                self.registrar_transacao(cpf, f"Saque de R${valor:.2f}")
                break
                
    
            elif usersList[i][f'cpf'] == cpf and valor > usersList[i]['saldo'] + usersList[i][f'credito']:
                print("\nNão há dinheiro o suficiente, o seu saldo não foi alterado.\n")
                break
        
        


    def deposito(self,cpf,valor):
            wh = "ATM_caseiro/users.json"
            usersList = []

            with open(wh) as js:
                usersList = json.load(js)
            
            for i in range(len(usersList)):
                if usersList[i][f'cpf'] == cpf:
                    usersList[i][f'saldo'] += valor
                    self.registrar_transacao(cpf, f"Depósito de R${valor:.2f}")
                    print("\n\tDepósito efetuado com Sucesso!\n")
            
            with open(wh,"w") as where:
                json.dump(usersList,where,indent=4)

    def pagamento(self,valor,fromcpf,tocpf):

        self.saque(fromcpf,valor)
        self.deposito(tocpf,valor)
        print("\n\tPagamento Realizado com sucesso!\n")
        self.registrar_transacao(fromcpf, f"Pagamento enviado de R${valor:.2f}")
        self.registrar_transacao(tocpf, f"Pagamento recebido de R${valor:.2f}")

    def pedirCredito(self,cpf,valor):
        wh = "ATM_caseiro/users.json"
        usersList = []

        with open(wh) as js:
            usersList = json.load(js)
        
        for i in range(len(usersList)):
            if usersList[i][f'cpf'] == cpf and valor <= usersList[i]['saldo'] and not bool(usersList[i][f'credito']):
                usersList[i][f'credito'] += valor
                self.registrar_transacao(cpf, f"Crédito aprovado de R${valor:.2f}")
                print("\n\tDepósito de crédito efetuado com Sucesso!\n")
            elif usersList[i][f'cpf'] == cpf and valor > usersList[i]['saldo']:
                print("\n\tO credito requisitado é maior do que o saldo atual. Credito não concedido.\n")

        with open(wh,"w") as where:
            json.dump(usersList,where,indent=4)

    def addUser(self):
        wh = "ATM_caseiro/users.json"
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
        wh = "ATM_caseiro/users.json"

        with  open(wh) as js:
            usersList = json.load(js)

        print("\n\t===== ATM CASEIRO =====")
        aDeletar = input("\tQual seria o nome do usuario a ser deletado?  ->\t")
        print("\t================")

        for i in range(len(usersList)):
            if usersList[i]['nome'] == aDeletar and usersList[i]['saldo'] == 0:
                
                usersList.pop(i)
                print("\n\nUsuário deletado com Sucesso!\n\n")
                break

            elif usersList[i]['nome'] == aDeletar and usersList[i]['saldo'] != 0:
                    
                print("\n\n\tNão foi possível deletar o usuário...saldo diferente de 0\n\n")
                break

        with open(wh, "w") as js:
            json.dump(usersList, js, indent=4)
            




    def updateUser(self):

        def wrapperUpdate(info,antigo,novo):
            for i in range(len(usersList)):
                if usersList[i][f'{info}'] == antigo:
                    usersList[i][f'{info}'] = novo

        wh = "ATM_caseiro/users.json"

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
        wh = "ATM_caseiro/users.json"

        with  open(wh) as js:
            usersList = json.load(js)
        print("\n\t===== ATM CASEIRO =====")
        aProcurar = input("\tQual seria o nome do usuario a ser buscado?  ->\t")
        print("\t================")

        for i in range(len(usersList)):
            if usersList[i]['nome'] == aProcurar:
                print(usersList[i])

    def extrato(self, cpf):
        wh = "ATM_caseiro/users.json"
        usersList = []

        with open(wh) as js:
            usersList = json.load(js)

        for user in usersList:
            if user['cpf'] == cpf:
                historico = user.get('historico', [])
                print("\n===== Extrato =====")
                print(f"CPF: {cpf}")
                print("Transações:")
                for transacao in historico:
                    print(f"\t- {transacao}")
                print("====================")
                break
        else:
            print("CPF não encontrado.")


    def registrar_transacao(self, cpf, transacao):
        wh = "ATM_caseiro/users.json"
        usersList = []

        with open(wh) as js:
            usersList = json.load(js)

        for user in usersList:
            if user['cpf'] == cpf:
                historico = user.get('historico', [])
                data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                historico.append(f"{data_hora}: {transacao}")
                user['historico'] = historico
                break

        with open(wh, "w") as js:
            json.dump(usersList, js, indent=4)