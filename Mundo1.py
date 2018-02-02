print("=== Bem Vindo ao Mundo 1 - Floresta ===\n"
      "=== As fases desse mundo são ===\n"
      "1. Primeiros Comandos em python\n"
      "2. Tipos Primitivos e Saída de Dados\n"
      "3. Operadores Aritméticos\n"
      "4. Utilizando Módulos\n"
      "5. Manipulando Strings\n"
      "6. Estrutura Condicional(Parte 1)\n"
      "7. Cores no terminal")
print("Qual fase você escolhe(número de 1 a 7)")
num = int(input())

if num == 1:
    from F1M1 import F1M1
elif num == 2:
    from F2M1 import F2M1
elif num == 3:
    from F3M1 import F3M1
elif num == 4:
    from F4M1 import F4M1
# elif num == 5:

# elif num == 6:

# elif num == 7:

else:
    print("Inválido")
