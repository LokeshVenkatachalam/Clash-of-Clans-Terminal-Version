import colorama
import sys
import os
import math
import time
import copy
import time
from colorama import Fore, Back, Style

colorama.init()



#custom modules
from input import input_to
from constants import ROW,COL
from gameplay import Game
from village import village
from buildings import empty,town_Hall,hut,cannon
from attackers import king

empty_village = [[' ' for i in range(COL)] for j in range(ROW)]
for j in range(ROW):
    empty_village[j][30]='\n';    
game = Game()
empty_village_map = [[empty(game,i,j) for i in range(COL)] for j in range(ROW)]
game.board = copy.deepcopy(empty_village)
game.map = copy.deepcopy(empty_village_map)
game.start()
game.display()
game.run()



