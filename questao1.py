import datetime

class Jogador():
    
    def __init__(self, nome, posicao, dataDeNascimento, nacionalidade, altura, peso) -> None:
        self.__nome = nome
        self.__posicao = posicao
        self.__dataDeNascimento = dataDeNascimento
        self.__nacionalidade = nacionalidade
        self.__altura = altura
        self.__peso = peso

    def imprimir(self):
        print(f'Jogador: [{self.__nome}]',
        f'\nPosição: [{self.__posicao}]',
        f'\nData de Nascimento: [{self.__dataDeNascimento}]',
        f'\nNacionalidade: [{self.__nacionalidade}]',
        f'\nAltura: [{self.__altura}]',
        f'\nPeso: [{self.__peso}]')

    def calcularIdade(self):
        data_atual = datetime.date.today()
        ano_atual = data_atual.year
        print(f'A idade atual do jogador é {ano_atual - int(self.__dataDeNascimento[6:])} anos.')




# data_atual = datetime.date.today()
# anoatual = data_atual.year

# print(data_atual)
# print(anoatual)


jogador1 = Jogador('Rian', 'Atacante', '18/06/1998', 'Israelense', 180, 78)
jogador1.calcularIdade()