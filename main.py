from ATM_caseiro.Classes.Auth import Autentication
from ATM_caseiro.Classes.MenuCliente import MenuCliente
from ATM_caseiro.Classes.MenuGerente import MenuGerente

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