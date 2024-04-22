lista = []
for _ in range (5):
    numero = float(input('Digite um número: '))
    lista.append(numero)
print(lista)

# '_' é usado quando é desejado iterar apenas um número
# fixo de vezes sem se importar com os valores da iteração,
# enquanto 'i' (ou qualquer outro nome) é usado quando
# é preciso acessar os valores da sequência durante o loop