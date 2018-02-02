print ("=== Bem vindo a fase 3 do mundo 1 ===\n"
       "=== Os desafios dessa fase são ===\n"
       "1. Desafio 5\n"
       "2. Desafio 6\n"
       "3. Desafio 7\n"
       "4. Desafio 8\n"
       "5. Desafio 9\n"
       "6. Desafio 10\n"
       "7. Desafio 11\n"
       "8. Desafio 12\n"
       "9. Desafio 13\n"
       "10. Desafio 14\n"
       "11. Desafio 15\n"
       "Qual desafio você escolhe?(digite um número de 1 a 11)")
num = int(input())
if num == 1:
    from F3M1 import D5F3M1
elif num == 2:
    from F3M1 import D6F3M1
elif num == 3:
    from F3M1 import D7F3M1
elif num == 4:
    from F3M1 import D8F3M1
elif num == 5:
    from F3M1 import D9F3M1
elif num == 6:
    from F3M1 import D10F3M1
elif num == 7:
    from F3M1 import D11F3M1
elif num == 8:
    from F3M1 import D12F3M1
elif num == 9:
    from F3M1 import D13F3M1
elif num == 10:
    from F3M1 import D14F3M1
elif num == 11:
    from F3M1 import D15F3M1
else:
    print("Inválido")