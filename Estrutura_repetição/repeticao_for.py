#maximo = -1

# De 0 a 3 // Seja X um número inteiro tal que X pertence ao conjunto dos Naturais num intervalo entre 0 e 3
# for i in range (4):
#    maximo = max(maximo, i)
#    print(f"Número máximo encontrado até agora é: {maximo}")

maximo = float(input('Digito um número: '))

for _ in range (4):
    maximo = max(maximo, float(input('Digite um número: ')))
    print(f'Número máximo encontrado até agora é: {maximo}')


# O 'f' dentro de uma string formatada indica que a 
# string contém expressões a serem formatadas e 
# inseris dentro dela

# Uma f-string é uma maneira conveniente de criar strings
# que contêm valores de variáveis ou expressões calculadas
# de forma dinâmica

# Ao utilizar uma f-string, pode-se incorporar variáveis
# ou expressões diretamente na string, colocando-as dentro
# de chaves '{}' e precedendo a string com a caractere 'f'. 
# O Python avaliará as expressões entre chaves e as substituirá
# pelos seus valores correspondentes dentro da string formatada.