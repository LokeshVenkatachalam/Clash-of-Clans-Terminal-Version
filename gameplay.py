import copy
import time
import sys
import termios
import tty
import signal

from input import input_to
from colorama import Fore, Back, Style
from constants import ROW,COL,TP
from village import village
from buildings import hut, town_Hall
from attackers import king,barbarian

class Game:
    def __init__(self):
        self.board = []
        self.map = []
        self.village = village(self)
        self.time_Running = 0
        self.king_Count = 0
        self.barbarian_Count = 0 

    def start(self):
        for object in self.village.existing_Building:
            object.display()

    def display(self):
        for row in self.board:
            for c in row:
                print(c, end='')

    def run(self):
        self.time_Start = time.time()
        while True:
            key = input_to()
            self.time_Running = float(time.time() - self.time_Start)
            self.display()
            if(key == 'j'):
                if(self.king_Count == 0):
                    self.village.attacker_King.append(king(self,0,12))
                    self.king_Count = 1
            elif(key == 'k'):
                if(self.king_Count == 0):
                    self.village.attacker_King.append(king(self,13,0))
                    self.king_Count = 1
            elif(key == 'l'):
                if(self.king_Count == 0):
                    self.village.attacker_King.append(king(self,29,12))
                    self.king_Count = 1
            elif(key == 'a'):
                if(self.king_Count == 1):
                    self.village.attacker_King[0].move_left()
            elif(key == 'd'):
                if(self.king_Count == 1):
                    self.village.attacker_King[0].move_right()
            elif(key == 'w'):
                if(self.king_Count == 1):
                    self.village.attacker_King[0].move_up()
            elif(key == 's'):
                if(self.king_Count == 1):
                    self.village.attacker_King[0].move_down()
            elif(key == ' '):
                if(self.king_Count == 1):
                    self.village.attacker_King[0].attack()
            elif(key == 'i'):
                if(self.barbarian_Count <=6 ):
                    self.village.attacker_Barbarian.append(barbarian(self,0,12))
                    self.barbarian_Count += 1
            elif(key == 'o'):
                if(self.barbarian_Count <=6 ):
                    self.village.attacker_Barbarian.append(barbarian(self,13,0))
                    self.barbarian_Count += 1
            elif(key == 'p'):
                if(self.barbarian_Count <=6 ):
                    self.village.attacker_Barbarian.append(barbarian(self,29,12))
                    self.barbarian_Count += 1
            for barbarian in self.village.attacker_Barbarian:
                barbarian.move()
        
            print("\033[H\033[J", end="")
            self.display()
            time.sleep(TP)
            
            