#advinhar a senha~
tentativas = 0

while tentativas < 3:
    senha = input("Digite a senha: ")
    if senha == "Senha123":
        print("Acesso concedido!")
        break
    else:
        print("Senha incoreta. Tente novamente.")
        tentativas += 1
else:
    pint("Você excedeu o número máximo de tentativas.")
