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
from constants import ROW,COL
from gameplay import Game
from village import village
from buildings import town_Hall,hut


empty_village = [[' ' for i in range(COL)] for j in range(ROW)]        
for j in range(ROW):
    empty_village[j][30]='\n';    
game = Game()
game.board = copy.deepcopy(empty_village)
game.start()
game.display()



