class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir_ponto(self):
        print(f'{self.x}, {self.y}')

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def achar_centro(self):
        centro_largura = self.largura / 2
        centro_altura = self.altura / 2
        # print(f'{centro_largura}, {centro_altura}')
        return (centro_largura, centro_altura)




# Criando objetos da classe Retangulo
retangulo = Retangulo(6, 4)
retangulo.achar_centro()

print(f'Centro do retângulo: ', retangulo.achar_centro())

#centro_x = retangulo.achar_centro()
#centro_y = retangulo.achar_centro()





