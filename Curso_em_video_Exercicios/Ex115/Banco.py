#coding: latin-1

def acessar():
    open("Banco_de_Dados.txt", "a")

def analisar():
    open("Banco_de_Dados.txt", "r")

def armazenar(nome, idade):
    arquivo = open("Banco_de_Dados.txt", "a")
    arquivo.write(f"{nome:<40} {idade} anos")
