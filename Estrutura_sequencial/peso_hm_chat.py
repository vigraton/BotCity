h = float(input('Qual sau altura? '))
sexo = input('Digite o sexo (M para masculino, F para feminino): ')

if sexo.upper() == 'M':
    peso_homem = (72.7 * h) - 58
    print('O peso ideal para um homem com essa altura é:', peso_homem)
elif sexo.upper() == 'F':
    peso_mulher = (62.1 * h) - 44.7
    print('O peso idela para uma mulher com essa altura é: ', peso_mulher)
else:
    print('Opção inválida. Digite M para masculino ou F para Feminino.')

    
# upper() = método que converte uma  string para letras maiúsculas 