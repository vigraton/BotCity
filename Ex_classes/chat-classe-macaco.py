class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.estomago = []

    def comer(self, comida):
        self.estomago.append(comida)

    def verBucho(self):
        if self.estomago:
            print(f"{self.nome} está comendo:", self.estomago)
        else:
            print(f"{self.nome} está com o estômago vazio.")

    def digerir(self):
        if self.estomago:
            comida_digerida = self.estomago.pop(0)
            print(f"{self.nome} digeriu:", comida_digerida)
        else:
            print(f"{self.nome} não pode digerir nada porque seu estômago está vazio.")

def main():
    # Criando dois macacos
    macaco1 = Macaco("Macaco 1")
    macaco2 = Macaco("Macaco 2")

    # Alimentando os macacos com três alimentos diferentes
    macaco1.comer("Banana")
    macaco2.comer("Maçã")
    macaco1.comer("Uva")

    # Verificando o estômago dos macacos
    macaco1.verBucho()
    macaco2.verBucho()

    # Um macaco come o outro
    macaco1.comer(macaco2)

    # Verificando o estômago dos macacos após a interação
    macaco1.verBucho()
    macaco2.verBucho()

if __name__ == "__main__":
    main()
