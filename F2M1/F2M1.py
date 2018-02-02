print ("=== Bem vindo a fase 2 do mundo 1 ===\n"
       "=== Os desafios dessa fase são ===\n"
       "1. Desafio 3\n"
       "2. Desafio 4\n"
       "Qual desafio você escolhe?(digite 1 ou 2)")
num = int(input())
if num == 1:
       from F2M1 import D3F2M1
elif num == 2:
    from F2M1 import D4F2M1
else:
       print("Inválido")