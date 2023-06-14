from ATM_caseiro.ATM import Autentication,MenuCliente,MenuGerente


def workspace():

    login = Autentication()

    login.fazer_login()

    
    if login.gerenteAutenticado:
        menuGerente = MenuGerente()
        menuGerente.loop()

    elif login.usuarioAutenticado:
        menuCliente = MenuCliente()
        menuCliente.loop()

workspace()