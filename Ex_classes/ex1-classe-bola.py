class CirculoPerfeito:
    def __init__(self):
        self.cor = 'Azul'
        self.circunferencia = 4
        self.material = 'Papel'

    # Métodos:
    def mostra_cor(self):
        return self.cor
    
    def troca_cor(self, cor):
        self.cor = cor

circulo_primeiro = CirculoPerfeito()
circulo_segundo = CirculoPerfeito()

print(type(circulo_primeiro))
print(type(circulo_primeiro is circulo_segundo))
print(id(circulo_primeiro), circulo_primeiro.mostra_cor())
print(id(circulo_segundo), circulo_segundo.mostra_cor())
circulo_segundo.mostra_cor = 'Roxo'
print(circulo_primeiro.cor, circulo_segundo.cor)

print(circulo_primeiro.cor, circulo_segundo.cor)
