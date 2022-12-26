#!/usr/bin/env python
# coding: utf-8

# In[1]:


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

