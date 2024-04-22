# Lendo o arquivo de usuários e guardando os dados em uma lista de tuplas
dados_usuarios = {}
total_espaco = 0

def bytes_mb(bytes_valor):
    return bytes_valor / (1024 ** 2)

def porcentagem_uso(espaco_usuario, espaco_total):
    return (espaco_usuario / espaco_total) * 100

with open("sample_data\\usuarios.txt", "r") as arquivo:
    for linha in arquivo:
        usuario, espaco_ocupado_str = linha.split()
        espaco_ocupado = int(espaco_ocupado_str)
        dados_usuarios[usuario] = espaco_ocupado
        total_espaco += espaco_ocupado
        #print(linha)

with open('relatorio.txt', 'w') as relatorio:
    relatorio.write('ACME Inc.                 Uso do espaco em disco pelos usuarios\n')
    relatorio.write('----------------------------------------------------------------\n')
    relatorio.write("Nr.     Usuario       Espaco utilizado         Porcentagem do uso\n\n")

    # Loop para percorrer os dados
    for i, (usuario, espaco_ocupado_str) in enumerate(dados_usuarios.items(), start=1):
        relatorio.write(f"{i:<5} {usuario:<15} {bytes_mb(espaco_ocupado):<20.2f} MB"
                        f"{porcentagem_uso(espaco_ocupado, total_espaco):<10.2f}%\n")
        relatorio.write(f"\nEspaco total ocupado: {bytes_mb(total_espaco):.2f} MB\n")
        relatorio.write(f"Espaco medio ocupado: {bytes_mb(total_espaco / len(dados_usuarios)):.2f} MB\n")

# Info adicional sobre a porcentagem de funcionários que usam o maior espaço
        
maior_espaco_percentual = (max(dados_usuarios.values()) / total_espaco) * 100
with open("relatorio.txt", "a") as relatorio:
    relatorio.write(f"\n{maior_espaco_percentual:.2f}% dos funcionarios ocupam o maior espaco.\n")