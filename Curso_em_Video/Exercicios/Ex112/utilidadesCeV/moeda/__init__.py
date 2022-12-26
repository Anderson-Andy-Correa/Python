#!/usr/bin/env python
# coding: utf-8

# In[12]:


def metade(n=0, show=False):
    """
    → Calcula a metade de um determindo preço, retornando o resultado com ou sem formatação.
    :param n: o preço base que se quer calcular.
    :param show: quer a saída formatada ou não?
    :return: a metade do preço base com ou sem formatação.
    """
    if show == False:
        return n / 2
    else:
        return estrutura(n / 2)


def dobro(n=0, show=False):
    """
    → Calcula o dobro de um determindo preço, retornando o resultado com ou sem formatação.
    :param n: o preço base que se quer calcular.
    :param show: quer a saída formatada ou não?
    :return: o dobro do preço base com ou sem formatação.
    """
    if show == False:
        return n * 2
    else:
        return estrutura(n * 2)
    

def aumentar(n=0, more=0, show=False):
    """
    → Calcula o aumento de um determindo preço, retornando o resultado com ou sem formatação.
    :param n: o preço base que se quer calcular.
    :param more: qual é a porcentagem do aumento?
    :param show: quer a saída formatada ou não?
    :return: o preço base reajustado com ou sem formatação.
    """
    if show == False:
        return n * (more / 100 + 1)
    else:
        return estrutura(n * (more / 100 + 1))
    

def diminuir(n=0, minus=0, show=False):
    """
    → Calcula uma redução de um determindo preço, retornando o resultado com ou sem formatação.
    :param n: o preço base que se quer calcular.
    :param minus: qual é a porcentagem da redução?
    :param show: quer a saída formatada ou não?
    :return: a redução do preço base com ou sem formatação.
    """
    if show == False:
        return n * (1 - minus / 100)
    else:
        return estrutura(n * (1 - minus / 100))
    

def estrutura(n=0, moeda='R$'):
    """
    → Converte o valor para um formato monetário com a respectiva representação da moeda.
    :param n: o valor base a ser formatado.
    :param moeda: qual o simbolo do sifrão da moeda?
    :return: o valor no formato monetário com o sifrão.
    """
    return f"{moeda}{n:.2f}".replace('.',',')


def resumo(n=0, aumento=0, redução=0):
    print('-'*30)
    print(f"{'RESUMO DO VALOR':^30}")
    print('-'*30)
    print(f"{'Preço analisado:':<19}", estrutura(n))
    print(f"{'Dobro do preço:':<19}", dobro(n, True))
    print(f"{'Metade do preço:':<19}", metade(n, True))
    if aumento > 0:
        print(f"{f'{aumento}% de aumento:':<19}", aumentar(n, aumento, True))
    if redução > 0:
        print(f"{f'{redução}% de redução:':<19}", diminuir(n, redução, True))
    print('-'*30)

