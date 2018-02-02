print ("=== Bem vindo a Fase 4 do Mundo 1 ===\n"
       "=== Os desafios dessa fase são ===\n"
       "1. Desafio 16\n"
       "2. Desafio 17\n"
       "3. Desafio 18\n"
       "4. Desafio 19\n"
       "5. Desafio 20\n"
       "6. Desafio 21"
       "Qual desafio você escolhe?(digite um número de 1 a 6)")
num = int(input())

if num == 1:
    from F4M1 import D16F4M1
elif num == 2:
    from F4M1 import D17F4M1
elif num == 3:
    from F4M1 import D18F4M1
elif num == 4:
    from F4M1 import D19F4M1
elif num == 5:
    from F4M1 import D20F4M1
elif num == 6:
    from F4M1 import D21F4M1
else:
    print("Inválido")