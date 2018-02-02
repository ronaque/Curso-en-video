print ("=== Bem vindo a Fase 1 do Mundo 1 ===\n"
       "=== Os desafios dessa fase são ===\n"
       "1. Desafio 1\n"
       "2. Desafio 2\n"
       "3. Desafio 3\n"
       "Qual desafio você escolhe?(digite um número de 1 a 3)")
num = int(input())
if num == 1:
    from F1M1 import D1F1M1
elif num == 2:
    from F1M1 import D2F1M1
elif num == 3:
    from F1M1 import D3F1M1
else:
    print("Inválido")