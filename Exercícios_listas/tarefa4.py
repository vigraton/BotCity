# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas 
# consoantes foram lidas. Imprima as consoantes.

letras = []

for _ in range(10):
    letra = input('Digite qualquer letra: ').upper()
    letras.append(letra)


vogais = ['A', 'E', 'I', 'O', 'U']
consoantes = []

for letra in letras:
    if letra in vogais:
        print('Vogal: ', letra)
    else:
        consoantes.append(letra)

print('Consoantes: ', consoantes)
print('Total de consoantes: ', len(consoantes))

#print('Total de vogais: ', len())

# Linha 6: underline _ foi usado pois os valores da lista não são importantes
# para ela

# 1. 'letras': É uma lista vazia criada no início do programa para armazenar as
# letras lidas

# 2. 'letra': Variável que guarda a letra lida em cada iteração do loop

# 3. '.append(letra)': Método para adiocionar um elemento ai final da lista. Nesse
# caso, adiciona-se a 'letra' lida à lista 'letras' 

# 'letras.append(letra)' acumula cada letra lida na lista 'letras'.Ao final do loop, 
# a lista letras conterá todas as 10 letras que o usuário digitou, e essa lista será 
# usada posteriormente para determinar as consoantes e vogais.
