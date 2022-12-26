#!/usr/bin/env python
# coding: utf-8

# In[1]:


def metade(n = 0):
    return n / 2


def dobro(n = 0):
    return n * 2


def aumentar(n = 0):
    return n * 1.10


def diminuir(n = 0):
    return n * 0.87


def moeda(n = 0, moeda = 'R$'):
    return f"{moeda}{n:.2f}".replace('.',',')

