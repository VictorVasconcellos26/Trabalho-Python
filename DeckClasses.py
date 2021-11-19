import random
from random import shuffle

N_CARTAS = 52
class Carta:
    def __init__(self, Naipe=0, Figura=2):
        self.Naipe = Naipe
        self.Figura = Figura

    naipe_name = ['Paus', 'Ouros', 'Copas', 'Espadas']
    figura_value = [None ,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Valete', 'Rainha', 'Rei']

    def __str__(self):
        return f'{Carta.figura_value[self.Figura]} de {Carta.naipe_name[self.Naipe]} '

    def __int__(self, other):
        if self.Naipe < other.Naipe: return True
        if self.Naipe > other.Naipe: return False
        return self.Figura < other.Figura


class Baralho:
    def __init__(self):
        self.cartas = []
        for Naipe in range(4):
            for Figura in range(1, 14):
                cartas = Carta(Naipe, Figura)
                self.cartas.append(cartas)

    def __str__(self):
        res = []
        for cartas in self.cartas:
            res.append(str(cartas))
        return '\n'.join(res)

    def tirar_carta(self, carta):
        self.cartas.remove(carta)

    def add_carta(self, carta):
        self.cartas.append(carta)

    def embaralhar(self):
        random.shuffle(self.cartas)

class Jogador():
    def __init__(self, nome, ganhou):
        self.nome = nome
        self.ganhou = ganhou
        self.mao = []


    def receber_cartas(self, carta):
        self.mao.append(carta)

    def pegue_carta(self):
        carta = self.mao.pop()
        return carta

class Partida:
    def __init__(self, baralho):
        self.listaJ = ['Pedro', 'Victor', 'Miguel', 'Gustavo']
        self.baralho = baralho

    def mesma_Carta(self):
        if len(self.listaJ) == 4:
            self.baralho = Baralho()
            self.baralho.embaralhar()

