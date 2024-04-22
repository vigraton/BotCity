# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo

int1 = int(input('Digite um número inteiro: '))
int2 = int(input('Digite outro número inteiro: '))
real = float(input('Digite um número real: '))

calculo = (2 * int1) * (real/2)
calculo1 = (3 * int1) + (real)
calculo2 = real ** 3

print(calculo,'\n', calculo1,'\n', calculo2)
