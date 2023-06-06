from ATM_caseiro.ATM import MenuClient, Autentication, fazer_login


def workspace():

    # fazer login
    login = Autentication()
    login.cpf()
    login.senha()

    # cliente = MenuClient()

    # cliente.exibir_menu()

    workspace()