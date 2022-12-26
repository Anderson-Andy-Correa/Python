#!/usr/bin/env python
# coding: utf-8

# In[55]:


# Vamos ver como fazer acesso a arquivos usando o Python.

from Menus import *

def acessar():
    open("Banco_de_Dados.txt", "a")

def mostrar():
    titulo("PESSOAS CADASTRADAS")
    try:
        arquivo = open("Banco_de_Dados.txt", "r")
        linha = arquivo.readlines()
        for i in linha:
            nome = i.find(";")
            print(f"{i[:nome]:<40} {i[nome+2:-1]:>3} anos")
    except:
        print('Não há registros, por favor, adicione um novo cadastro.')

def armazenar():
    titulo("NOVO CADASTRO")
    nome = input("Nome: ")
    while True:
        try:
            idade = int(input("Idade: "))
        except:
            print("\033[31mIdade inválida, tente novamente colocando um número inteiro válido.\033[m")
        else:
            print(f"Registro de {nome} adicionado.")
            break
    arquivo = open("Banco_de_Dados.txt", "a")
    arquivo.write(f"{nome}; {idade}\n")
    


# In[56]:


mostrar()


# In[ ]:




