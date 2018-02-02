dia = input('Dia em que nasceu = ')
mes = input('Mês = ')
ano = input('Ano = ')
print('Você nasceu no dia', dia, 'de', mes, 'de', ano, '. Correto?')

cf = str(input("Você deseja ver o codigo fonte(sim ou não)"))
if cf == "sim":
    f = open('D2F1M1.txt','r')
    print(f.read())