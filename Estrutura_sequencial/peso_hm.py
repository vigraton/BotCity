# Tendo como dado de entrada a altura (h) de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, 
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

h = float(input('Qual sua altura? '))
peso_homem = (72.7*h) - 58
peso_mulher = (62.1*h) - 44.7

print(peso_homem, '\n', peso_mulher)