# Faça um programa que peça a temperatura em graus Fahrenheit, 
# transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9)

Fah = int(input('Digite uma temperatura em Fahrenheit: '))

Celsius = 5 * ((Fah-32) / 9)

print('Em Celsius, a temperatura que vc digitou é ',Celsius)