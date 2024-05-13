# Ao terminar os métodos, o programa deve pedir ao usuário que informe as medidas de um local. 
# Depois, deve criar um objeto com as medidas e clacular a quantidade de pisos
# e de rodapés necessários para o local.

class Retangulo:
    def __init__(self):
        self.base = 10
        self.altura = 4

    def mudar_lados(self, nova_base, nova_altura):
        self.base = nova_base
        self.altura = nova_altura

    def retornar_lados(self):
        return self.base, self.altura

    def calcular_area(self):
        area = self.base * self.altura
        return area

    def calcular_perimetro(self):
        perimetro = (2 * self.base) + (2 * self.altura)
        return perimetro


retangulo = Retangulo(10, 5)
retangulo.calcular_area()
print(retangulo.calcular_area())
print(retangulo.mudar_lados(90, 25))
print(retangulo.calcular_area())