numero_secreto = 9
chute = 0 # numero de tentativas
limite = 3

while chute < limite:
    adivinhe = int(input('Adivinhe o número: '))
    chute +=1
    if adivinhe == numero_secreto:
        print('Você venceu!')
        break
else:
    print('Você perdeu!')