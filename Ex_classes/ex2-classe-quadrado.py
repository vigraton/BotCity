class Quadrado:
    def __init__ (self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def mostrar_lado(self):
        return self.tamanho_lado
    
    def mudar_lado(self, novo_tamanho):
        self.tamanho_lado = novo_tamanho

    def calcular_area(self):
        return self.tamanho_lado ** 2
    
quadrado = Quadrado(5)
print("Lado do quadrado: ", quadrado.mostrar_lado())
print("Área do quadrado: ", quadrado.calcular_area())

# Mudando o lado do quadrado:
quadrado.mudar_lado(7)
print("Novo lado do quadrado: ", quadrado.mostrar_lado())
print("Nova área do quadrado: ", quadrado.calcular_area())



# class Quadrado:
    # def __init__ (self, lado = 1):
        # self.lado = lado

    # def calcular_area (self):
        # return self.lado ** 2

#    quadrado = Quadrado (4)
#    print(quadrado.lado, quadrado.calcular_area())

