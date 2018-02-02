n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
re = n1 + n2
print('A soma é', re)

cf = str(input("Você deseja ver o codigo fonte(sim ou não)"))
if cf == "sim":
    f = open('D3F1M1.txt','r')
    print(f.read())