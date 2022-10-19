#coding: latin-1

# Menus principal
def mainMenu():
    print('-'*50)
    print("{:^50}".format("MENU PRINCIPAL"))
    print('-'*50)
    print("1 - Ver pessoas cadastradas")
    print("2 - Cadastrar nova Pessoa")
    print("3 - Sair do Sistema")
    print('-'*50)
    verificarMenu(resp)
    return resp


def verificarMenu(resp):
    while True:
        try:
            resp = int(input("Sua Opção"))

