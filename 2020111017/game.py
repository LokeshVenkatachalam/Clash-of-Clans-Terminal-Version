import string
import colorama
import sys
import os
import os.path
import math
import time
import copy
import time
from colorama import Fore, Back, Style

colorama.init()

sys.path.append(os.path.relpath("./src"))


#custom modules
from input import input_to
from constants import ROW,COL
from gameplay import Game
from village import village
from buildings import empty,town_Hall,hut,cannon
from attackers import king,barbarian

  
file_name_found = False
file_index = 1
while(file_name_found == False):
    file_name = "./replays/Game_no_"+str(file_index)+".txt"
    if(os.path.exists(file_name) == False):
        file = open(file_name, "w")
        break
    file_index +=1

game = Game()
empty_village = [[' ' for i in range(COL)] for j in range(ROW)]
for j in range(ROW):
    empty_village[j][30]='\n';  
empty_village_map = [[empty(game,i,j) for i in range(COL)] for j in range(ROW)]
game.board = copy.deepcopy(empty_village)
game.map = copy.deepcopy(empty_village_map)
game.start()
game.run()
file.write(game.input_File)
#file.close()



