#!/usr/bin/env python
# coding: utf-8

# In[2]:


def leiaDinheiro(n):
    """
    →Analisa e valida se o valor informado pode ser lido como um valor flutuante.
    :param n: o valor a ser validado.
    :return: o valor já convertido no formato flutuante.
    """
    while True:
        n = input("Digite o preço: R$").strip()
        if n.find(",") > -1:
            n = n.replace(",", ".")
        if n.find(".") > -1 and int(n[:n.find(".")]) > 0:
            break
        elif n.isnumeric() == True and float(n) > 0:
            break
        else:
            print(f'\033[31mERRO! "{n}" é um preço inválido.\033[m')
    return float(n)


def leiaPorcentagem(n):
    """
    →Analisa e valida se o valor informado pode ser lido como um valor flutuante de porcertagem.
    :param n: o valor a ser validado.
    :return: o valor já convertido no formato flutuante.
    """
    msg = n
    while True:
        print(f"Digite a porcentagem de {msg}: ", end="")
        n = input("").strip()
        if n.find(",") > -1:
            n = n.replace(",", ".")
        if n.find(".") > -1 and int(n[:n.find(".")]) > 1:
            break
        elif n.isnumeric() == True and float(n) > -1:
            break
        else:
            print(f'\033[31mERRO! "{n}" é um valor inválido.\033[m')
    return float(n)

