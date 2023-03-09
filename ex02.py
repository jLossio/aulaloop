#verifica se o numero é par ou ímpar
numero = 0

while numero < 10000:
    if numero == 0:
        print("O numero é zero", numero )
    elif numero % 2 == 0:
        print("O número é par", numero)
    else:
        print("O número é impar", numero )
    numero += 1