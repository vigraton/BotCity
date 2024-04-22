salario_hora = float(input('Quanto você ganha por hora? '))
hora_mes = float(input('Quantas horas você trabalha por mês? '))

salario_bruto = salario_hora * hora_mes

print('Seu salário bruto é', salario_bruto)

imposto_renda = 0.11 * salario_bruto
print('Seu imposto de renda é', imposto_renda)
inss = 0.08 * salario_bruto
print('Seu INSS é', inss)
sindicato = 0.05 * salario_bruto
print('Seu sindicato é', sindicato)

salario_liquido = salario_bruto - imposto_renda - inss - sindicato
print('Seu salário líquido é', salario_liquido)