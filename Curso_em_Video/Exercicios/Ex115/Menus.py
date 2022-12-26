#!/usr/bin/env python
# coding: utf-8

# In[4]:


def mainMenu():
    titulo("MENU PRINCIPAL")
    print("\033[33m1 - \033[34mVer pessoas cadastradas\033[m")
    print("\033[33m2 - \033[34mCadastrar nova Pessoa\033[m")
    print("\033[33m3 - \033[34mSair do Sistema\033[m")
    print('-'*50)
    resp = verificarMenu()
    return resp


def verificarMenu():
    while True:
        try:
            resp = int(input("\033[33mSua Opção: \033[m"))
            if 0 < resp < 4:
                break
            else:
                print("\033[31mERRO! Use apensa números entre 1 a 3.\033[m")
        except:
            print("\033[31mERRO! Use apensa números!\033[m")
    return resp

def titulo(txt):
    print('-'*50)
    print("{:^50}".format(txt))
    print('-'*50)


# In[ ]:


mainMenu()


# In[ ]:




