class Tv:
    def __init__(self):
        self.canal_atual = None

    def mudar_canal(self, novo_canal):
        self.canal_atual = novo_canal

    def mudar_volume(self, mudar):
        if mudar == '+':
            print('Você aumentou o volume')
        elif mudar == '-':
            print('Você diminuiu o volume')
        else:
            print('Você desligou a TV.')
        
    def retorno(self):
        print(f'Você está assistindo {self.canal_atual}.')


televisor = Tv()

televisor.mudar_canal('Canal 1')
televisor.mudar_canal('Canal 2')
#televisor.mudar_canal('Canal 3')
televisor.mudar_volume('+')
televisor.retorno()

