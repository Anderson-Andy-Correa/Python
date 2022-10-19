#coding: latin-1

import requests

def acessar(url):
    try:
        html = requests.get(url)
    except:
        print("\033[31mO site Pudim não está disponível no momento.\033[m")
    else:
        print("\033[33mConsegui acessar o site Pudim com sucesso!\033[m")
        

teste = acessar("http://www.pudim.com.br/")


