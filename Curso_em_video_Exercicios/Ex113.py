#coding: latin-1

def leiaInt():
    while True:
        try:
            n = int(input("Digite um valor inteiro: "))
            break
        except KeyboardInterrupt:
            print("\033[31mO usuário preferiu não digitar esse número.\033[m")
            n = 0
            break
        except:
            print("\033[31mErro: por favor, digite um valor inteiro válido!\033[m")
    return n

def leiaFloat():
    while True:
        try:
            n = float(input("Digite um valor real: "))
            break
        except KeyboardInterrupt:
            print("\033[31mO usuário preferiu não digitar esse número.\033[m")
            n = 0
            break
        except:
            print("\033[31mErro: por favor, digite um valor inteiro válido!\033[m")
    return n


try:
    inteiro = leiaInt()
    real = leiaFloat()
finally:
    print(f"O valor inteiro digitado foi {inteiro} e o real foi {real:.2f}")

