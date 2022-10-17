f = str(input('DIgite uma frase: ')).strip().upper().replace(' ','')
s = f[::-1]
#for letra in range(len(f)-1,-1,-1):
#    s = s + f[letra]
print(f'{f} e {s}')
if f == s:
    print('Sim')
else:
    print('Não')