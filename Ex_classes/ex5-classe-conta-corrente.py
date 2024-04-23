class Conta_Corrente:
    def __init__(self, numero, nome, valor):
        self.conta = numero
        self.correntista = nome
        self.saldo = valor

    def alterar_Nome(self, novo_nome):
        self.correntista = novo_nome

    def deposito(self, valor):
        self.saldo += valor
        print('Depósito realizado com sucesso!')

    def saque(self, valor_saque):
        if self.saldo >= valor_saque:
            self.saldo -= valor_saque
            print('Saque realizado com sucesso!')
        else:
            print('Saldo insuficiente para realizar o saque.')

def main():
    correntistas = ["João", "Maria", "José", "Ana"]

    conta = Conta_Corrente(123, "João", 1000)

    print('Escolha um correntista')
    for i, nome in enumerate(correntistas):
        print(f'{i+1}. {nome}')

    escolha = int(input('Digite o número correspondente ao correntista desejado: '))

    if escolha >= 1 and escolha <= len(correntistas):
        novo_correntista = correntistas[escolha - 1]   
        conta.alterar_Nome(novo_correntista)
        print(f'O correntista doi alterado para {novo_correntista}')

    else:
        print('Escolha inválida')

if __name__ == "__main__":
    main()