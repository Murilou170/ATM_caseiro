from ATM_caseiro.Classes.BancoDeDados import Banco

class MenuGerente():
    def __init__(self):
        pass


    def exibir_menu(self):
        print("\n===== ATM CASEIRO =====")
        print("1. Criar Conta\n")
        print("2. Remover Conta\n")
        print("3. Atualizar Conta\n")
        print("4. Visualizar Conta\n")
        print("0. Sair\n")
        print("================")

    def obter_opcao(self):
        opcao = input("Digite o número da opção desejada: ")
        return opcao
    
    def executar_opcao(self, opcao):
        bc = Banco()

        if opcao == "1":
            bc.addUser()
        
        elif opcao == "2":
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