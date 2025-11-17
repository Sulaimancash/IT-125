import random
from exceptions import InvalidMoveException

class Player:
    def __init__(self, name):
        self.name = name
        self.win = 0

    def make_move(self):
        move = input('👉 Твой ход (камень, ножницы, бумага): ')
        if move not in ['камень', 'ножницы', 'бумага']:
            raise InvalidMoveException('Некорректный ход!')
        return move

class Computer:
    def make_move(self):
        return random.choice(['камень', 'ножницы', 'бумага'])
