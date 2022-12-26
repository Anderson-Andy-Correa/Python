#!/usr/bin/env python
# coding: utf-8

# In[12]:


def metade(n=0, show=False):
    if show == False:
        return n / 2
    else:
        return estrutura(n / 2)


def dobro(n=0, show=False):
    if show == False:
        return n * 2
    else:
        return estrutura(n * 2)
    

def aumentar(n=0, more=0, show=False):
    if show == False:
        return n * (more / 100 + 1)
    else:
        return estrutura(n * (more / 100 + 1))
    

def diminuir(n=0, minus=0, show=False):
    if show == False:
        return n * (1 - minus / 100)
    else:
        return estrutura(n * (1 - minus / 100))
    

def estrutura(n=0, moeda='R$'):
    return f"{moeda}{n:.2f}".replace('.',',')


def resumo(n, aumento, redução):
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

