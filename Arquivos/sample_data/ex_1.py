# Faça um programa que leia um arquivo de texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos
# O número dos ips não pode passar de 255, caso contrário ele é inválido.
# Cacete finalmente o bagulho mostrou os IPs ~ caminho relativo, confia `-´ (e a barra tava pro outro lado, nhai)

#import os

#os.getcwd
#print(os.getcwd)


def validar(ip:str) -> bool:
    numeros = ip.split('.')

    if len(numeros) != 4:
        return False
    
    for n in numeros:
        if not (0 <= int(n) <= 255):
            return False
    return True

ips_validos = []
ips_invalidos = []

with open ('sample_data\ips.txt', 'r') as arquivo:
    for linha in arquivo:
        ip = linha.strip()
        if validar(ip):
            ips_validos.append(ip)
        else:
            ips_invalidos.append(ip)

        print(ip, validar(ip))

with open ('sample_data\ips.txt', 'w') as arquivo:
    arquivo.writelines('[Endereços válidos:]\n')

    for ip in ips_validos:
        arquivo.writelines(f'{ip}\n')

    arquivo.writelines('\n')
    arquivo.writelines('\n')
    arquivo.writelines('[Endereços inválidos:]\n')

    for ip in ips_invalidos:
        arquivo.writelines(f'{ip}\n')