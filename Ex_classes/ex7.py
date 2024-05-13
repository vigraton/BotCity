# Código do chat

class Bichinho_Virtual():
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def alterar_fome(self, nivel_fome):
        self.fome = nivel_fome

    def alterar_saude(self, nivel_saude):
        self.saude = nivel_saude

    def envelhecer(self):
        self.idade += 1

    def alterar_humor(self):
        if self.fome >= 50 and self.saude >= 50:
            return "Feliz"
        if 20 <= self.fome and self.saude >= 30:
            return "Tédio"
        else:
            return "Triste"

    def retornar_info(self):
        return f'Nome: {self.nome}, Idade: {self.idade}, Fome: {self.fome}, Saúde: {self.saude}, Humor: {self.alterar_humor()}'

# Testanto classe Bichinho_Virtual
    
bichinho = Bichinho_Virtual("Bob", 5, 70, 2)

for _ in range(3):
    bichinho.envelhecer()
    print(bichinho.retornar_info())

bichinho.alterar_fome(60)
print(bichinho.retornar_info())

bichinho.alterar_saude(40)
print(bichinho.retornar_info())
