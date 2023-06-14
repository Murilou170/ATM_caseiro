from BancoDeDados import BancoDeDados

class MenuCliente():
    def __init__(self):
        pass


    def exibir_menu(self):
        print("\n===== ATM CASEIRO =====")
        print("1. hyhyhy\n")
        print("2. Saque\n")
        print("3. Depósito\n")
        print("4. Realizar Pagamento\n")
        print("5. Solicitar Crédito\n")
        print("0. Sair\n")
        print("================")

    def obter_opcao(self):
        opcao = input("Digite o número da opção desejada: ")
        return opcao
    
    def executar_opcao(self, opcao):
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