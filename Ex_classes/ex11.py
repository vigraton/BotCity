# A média comum é que um carro percorra de 10km a 15km com 1 litro, por isso a divisão por 10. 

class Carro:
    def __init__(self, km_litro=1, qt_combustivel=5):
        self.km_litro = km_litro
        self.qt_combustivel = qt_combustivel

    def andar(self):
        km = float(input('Quantos km você deseja dirigir? '))
        gasto = km / self.km_litro
        if gasto > self.qt_combustivel:
            print('Você não tem combustível o suficiente para esta viagem.')
        else:
            self.qt_combustivel -= gasto
            print(f'Você dirigiu', km, 'km. Você gastou', gasto, 'litros de combustível.')

    def obterGasolina(self):
        if self.qt_combustivel == 0:
            print('Você está sem gasolina')
            return 0
        else:
            return self.qt_combustivel

    def adicionarGasolina(self):
        while True:
            try:
                nova_quantidade = float(input('Digite a quantidade de litros que deseja abastecer: '))
                if nova_quantidade <= 0:
                    print('Digite um valor positivo')
                    continue
                else:
                    break
            except ValueError:
                print('Valor inválido. Por favor insira um número')

        self.qt_combustivel += nova_quantidade
        print('Carro abastecido com', nova_quantidade, 'litros.')
        

    def mostrar_info():
        pass

meuCarro = Carro()
meuCarro.adicionarGasolina()

meuCarro.andar()
meuCarro.obterGasolina()