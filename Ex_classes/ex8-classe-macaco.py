# Meu código (sem ajuda do chat, só pela misericórdia)

class Macaco():
    def __init__(self, nome, estomago):
        self.nome = nome
        self.ver_estomago = estomago

    def nivel_fome(self, sem_fome, com_fome, faminto):
        if sem_fome == 0:
            pass
        if com_fome == 1:
            pass
        if faminto == 2:
            pass

    def comer(self, uva, banana, manga):
        if banana >= 4:
            banana -= 1
            print('Você foi alimentado com uma banana.')
        else:
            print('As bananas acabaram. Seu guloso!')

        if uva >= 10:
            uva -= 1
            print('Você comeu uma uva.')
        else:
            print('As uvas acabaram ;-;')

        if manga >= 5:
            manga -= 1
            print('Você comeu uma manga.')
        else:
            print('Você comeu todas as mangas.')
    
    def digerir(self):
        pass
    
    def nivel_satisfacao(self, fome, insatisfeito, satisfeito, cheio):
        if self.ver_estomago == 0:
            self.ver_estomago = fome
        if self.ver_estomago == 1:
            self.ver_estomago = insatisfeito
        if self.ver_estomago == 2:
            self.ver_estomago = satisfeito
        else:
            self.ver_estomago = cheio

alimentos = ['Banana', 'Manga', 'Uva']

def main(self):
    inicio = input('Digite 1 para ser o macaco 1, ou 2 para ser o macaco 2: ')

    if inicio == 1:
        print('Você é o macaco 1')
    else:
        print('Você é o macaco 2')

    print(f'Seu nível de fome é {self.nivel_fome}')