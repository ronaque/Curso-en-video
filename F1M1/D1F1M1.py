nome = input('Qual é o seu nome? ')
print('Olá', nome, '! Prazer em te conhecer!')

cf = str(input("Você deseja ver o codigo fonte(sim ou não)"))
if cf == "sim":
    f = open('D1F1M1.txt','r')
    print(f.read())