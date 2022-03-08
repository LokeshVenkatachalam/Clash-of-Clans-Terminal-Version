from colorama import Fore, Back, Style
from constants import ROW,COL
import copy
from village import village
from buildings import hut, town_Hall


class Game:
    def __init__(self):
        self.board = []
        self.village = village(self)

    def start(self):
        for object in self.village.existing_Building:
            object.display()


    def display(self):
        for row in self.board:
            for c in row:
                print(c, end='')