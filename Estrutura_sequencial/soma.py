# Faça um programa que peça dois números e imprima a soma

num1 = int(input('Escolha um número: '))
num2 = int(input('Escolha um número: '))
soma = (num1 + num2)

print(soma)

# Na primeira tentativa eu escrevi:

# num1 = input(print('Escolha um número: '))
# num1 = input(print('Escolha um número: '))
# soma = num1 +  num2

# print(soma)

# Se eu colocasse em num1 = 1 e num2 = 2, apareceria a seguinte mesnagem:
# Escolha  um número: None1
# Escolha um número: None2
# 12

# Resposta do chatLGBT:

# O problema em seu código original ocorre devido ao uso incorreto da função print() dentro da função input(). 
# A função print() retorna None, e ao passar print('Escolha um número: ') como argumento para input(), 
# você está efetivamente passando None como a mensagem a ser exibida.
