from ATM_caseiro.Classes.BancoDeDados import Banco

class MenuCliente():
    def __init__(self):
        pass


    def exibir_menu(self):
        print("\n===== ATM CASEIRO =====")
        print("1. Extrato\n")
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
        bc = Banco()

        if opcao == "1":
            cpf = input("\nPor favor, confirme seu CPF:\t")
            bc.extrato(cpf)
        elif opcao == "2":
            cpf = input("\nPor favor, confirme seu CPF:\t")
            valor = input("\nValor desejado do saque R$:\t")
            bc.saque(cpf, int(valor))
        elif opcao == "3":
            cpf = input("Por favor, confirme seu CPF:\t")
            valor = input("Valor desejado do depósito R$:\t")
            bc.deposito(cpf, int(valor))
        elif opcao == "4":
            fromcpf = input("\nPor favor, confirme seu CPF:\t")
            tocpf = input("\nPor favor, confirme o CPF da conta onde o pagamento será depositado:\t")
            valor = input("\nRealizar Pagamento de R$:\t")
            bc.pagamento(int(valor), fromcpf, tocpf)
        elif opcao == "5":
            cpf = input("Por favor, confirme seu CPF:\t")
            valor = input("Valor desejado do crédito R$:\t")
            bc.pedirCredito(cpf, int(valor))
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