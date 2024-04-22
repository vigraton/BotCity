# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

def calcular_media(nota1, nota2, nota3, nota4):
    media = (nota1 + nota2 + nota3 + nota4) / 4
    return media

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media_calculada = calcular_media(nota1, nota2, nota3, nota4)

print(f'Notas: {nota1}, {nota2}, {nota3}, {nota4}')
print(f'Média: {media_calculada}')


 