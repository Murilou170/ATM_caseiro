import json
from Auth import User


class BancoDeDados():
    def __init__(self):
        pass

    

    def addUser(self):
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
    


    def deleteUser(self):
        wh = "Projeto4/ATM_caseiro/users.json"

        with  open(wh) as js:
            usersList = json.load(js)

        aDeletar = input("Qual seria o nome do usuario a ser deletado?  ->\t")

        for i in range(len(usersList)):
            print(len(usersList))
            if usersList[i]['nome'] == aDeletar and usersList[i]['saldo'] == 0:
                
                usersList.pop(i)
                print("\n\nMenos uma conta pra vc gerenciar!!\n\n")

            elif usersList[i]['nome'] == aDeletar and usersList[i]['saldo'] != 0:
                    
                    print("\n\nNão foi possível deletar o usuário...saldo diferente de 0\n\n")

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
        

        print("\n\n1. Atualizar Nome\n")
        print("2. Atualizar CPF\n")
        print("3. Atualizar Endereço\n")
        print("4. Atualizar Senha\n")


        opcao = input("\nDigite o número da opção desejada: ")


        
        if opcao == "1":

            Antigo = input("Digite nome atual do cliente: ")
            Novo = input("Digite o novo nome do cliente: ")

            wrapperUpdate('nome',Antigo,Novo)

            
        elif opcao == "2":

            Antigo = input("Digite cpf atual do cliente: ")
            Novo = input("Digite o novo cpf do cliente: ")

            wrapperUpdate('cpf',Antigo,Novo)

        elif opcao == "3":

            Antigo = input("Digite endereço atual do cliente: ")
            Novo = input("Digite o novo endereço do cliente: ")

            wrapperUpdate('endereco',Antigo,Novo)

        elif opcao == "4":

            Antigo = input("Digite senha atual do cliente: ")
            Novo = input("Digite a nova senha do cliente: ")

            wrapperUpdate('senha',Antigo,Novo)



        with open(wh, "w") as js:
            json.dump(usersList, js, indent=4)
            print("\n\nDados atualizados com Sucesso!\n\n")



    def visualizarUsuario(self):
        wh = "Projeto4/ATM_caseiro/users.json"

        with  open(wh) as js:
            usersList = json.load(js)

        aProcurar = input("Qual seria o nome do usuario a ser buscado?  ->\t")

        for i in range(len(usersList)):
            if usersList[i]['nome'] == aProcurar:
                print(usersList[i])