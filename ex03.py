#teste para tentar advinhar o número secreto
numero_secreto = 42
tentativa = 1

while tentativa <= 3:
    palpite = int(input("Adivinhe o número secreto: "))
    if palpite == numero_secreto:
        print("Parabéns, você acertou o numero secreto")
        break
    else:
        if palpite > numero_secreto:
            print("O numero secreto é menor do que", palpite)
        else:
            print("O numerro secreto é maior do que", palpite)
    tentativa += 1
    
if tentativa > 3:
    print("Suas tentativas acabaram, o numero secreto era", numero_secreto)