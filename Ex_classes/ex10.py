class BombaCombustivel:
    def __init__ (self, tipo, valor_litro, quantidade_combustivel):
        self.tipo = tipo
        self.valor_litro = valor_litro 
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        litros_abastecidos = valor / self.valor_litro
        self.quantidade_combustivel += litros_abastecidos
        return litros_abastecidos

    def abastecer_por_litro(self, litros):
        valor_pagar = litros * self.valor_litro
        self.quantidade_combustivel -= litros
        return valor_pagar

    def alterar_valor(self, novo_valor):
        self.valor_litro = novo_valor        

    def alterar_combustivel(self, novo_tipo):
         self.tipo = novo_tipo

    def alterar_quantidade_combustivel(self, nova_quantidade):
        self.quantidade_combustivel = nova_quantidade


# Criando uma bomba com tipo, valor_litro e quantidade_combustivel inicial
bomba = BombaCombustivel('Gasolina', 5.0, 100) 

# Abastecendo R$ 50 
print('Quantidade de litros abastecidos: ',bomba.abastecer_por_valor(50))

# Abastecendo 10 litros
print('Valor a ser pago: ', bomba.abastecer_por_litro(10))

# Alterando o valor do litro
bomba.alterar_valor(5.5)

# Alterando o tipo do combustível
bomba.alterar_combustivel('Álcool')

# Alterando a quantidade de combustível na bomba
bomba.alterar_quantidade_combustivel(150)

