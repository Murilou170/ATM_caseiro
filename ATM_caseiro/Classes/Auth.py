import json

class User():
    def __init__(self, nome, cpf, endereco, senha):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.credito = 0
        self.endereco = endereco
        self.senha = senha
        self.historico = []


class Autentication():

    def __init__(self):
        self.cpf = ""
        self.senha = ""
        self.usuarioAutenticado = False
        self.gerenteAutenticado =  False

    def fazer_login(self):
        foundClient = False
        gerente = False
        
        with open("ATM_caseiro/users.json", "r") as arquivo:
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
