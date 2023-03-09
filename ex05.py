#armazena um nuúmero pequeno
maior_numero = -9999999

#entra com o primeiro númeo
number = int (input("Entre com um número ou digite -1 para parar: "))

while number != -1:
    if number > maior_numero:
        maior_numero = number
    number = int(input("Entre com um número ou digite -1 para parar:"))
    
print("O Maior número é:", maior_numero)