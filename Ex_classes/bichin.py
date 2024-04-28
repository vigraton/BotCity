# Tentei fazer mas ficou naquelas né

class Bichinho_Virtual:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def ter_fome(self, nivel_fome):
        pass


    def envelhecer(self):
        self.idade += 1


bichinho = Bichinho_Virtual
nome = 'Bob'

for _ in range(11):
    bichinho.envelhecer()
    print(f'Seu bichinho se chama {bichinho.nome} e tem {bichinho.idade} anos.')