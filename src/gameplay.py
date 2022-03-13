import copy
import time
import sys
import termios
import tty
import signal
import copy
from buildings import hut, town_Hall

from input import input_to
from colorama import Fore, Back, Style
from constants import ROW,COL,TP
from village import village
from attackers import king,barbarian

class Game:
    def __init__(self):
        self.board = []
        self.map = []
        self.village = village(self)
        self.time_Running = 0
        self.king_Count = 0
        self.barbarian_Count = 0 
        self.spell_1_count = 0
        self.spell_1 = 0
        self.spell = False
        self.game_over_win = True
        self.game_over_lose = True
        self.spell_2_count = 0
        self.input_File = ""

    def start(self):
        for object in self.village.existing_Building:
            object.display()
        for object in self.village.attacker_Barbarian:
            object.display()

    def display(self):
        for j in range(ROW):
            for i in range(COL-1):
                if(self.map[j][i].name!="Empty"):
                    self.map[j][i].display()
                else:
                    self.board[j][i]=' '
                print(self.board[j][i], end='')
                print(Style.RESET_ALL, end = '')
            print(self.board[j][COL-1], end='')
            #for c in row:
            #    print(self.board[j][i], end='')

    def run(self):
        self.time_Start = time.time()
        self.start()
        self.display()
        self.game_over_win = True
        self.game_over_lose = True
        while True:
            self.game_over_win = True
            self.game_over_lose = True
            key = input_to()
            if key == None :
                self.input_File = self.input_File +str('G')
            else:
                self.input_File = self.input_File +str(key)

            print("\033[H\033[J", end="")
            self.time_Running = float(time.time() - self.time_Start)
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
                    self.village.attacker_King[0].move_direction = 'L'
            elif(key == 'd'):
                if(self.king_Count == 1):
                    self.village.attacker_King[0].move_direction = 'R'
            elif(key == 'w'):
                if(self.king_Count == 1):
                    self.village.attacker_King[0].move_direction = 'U'
            elif(key == 's'):
                if(self.king_Count == 1):
                    self.village.attacker_King[0].move_direction = 'D'
            elif(key == ' '):
                if(self.king_Count == 1):
                    for i in range(0,self.village.attacker_King[0].speed):   
                        self.village.attacker_King[0].attack()
                self.village.attacker_King[0].move_direction = ' '    
            elif(key == 'i'):
                if(self.barbarian_Count <6 ):
                    self.village.attacker_Barbarian.append(barbarian(self,0,12))
                    self.barbarian_Count += 1
            elif(key == 'o'):
                if(self.barbarian_Count <6 ):
                    self.village.attacker_Barbarian.append(barbarian(self,13,0))
                    self.barbarian_Count += 1
            elif(key == 'p'):
                if(self.barbarian_Count <6 ):
                    self.village.attacker_Barbarian.append(barbarian(self,29,12))
                    self.barbarian_Count += 1
            elif(key == 'm'):
                if(self.spell_1_count==0):
                    self.spell_1_count= 1
                    self.spell_1 = 12
                    for king_1 in self.village.attacker_King:
                        king_1.speed = 2*king_1.speed
                    for barbarian_1 in self.village.attacker_Barbarian:
                        barbarian_1.speed = 2*barbarian_1.speed
            elif(key == 'n'):
                if(self.spell_2_count==0):
                    self.spell_2_count= 1
                    for barbarian_1 in self.village.attacker_Barbarian:
                        barbarian_1.health = min(100,(barbarian_1.health + (barbarian_1.health/2)))
                    for king_1 in self.village.attacker_King:
                        king_1.health = min(100,(king_1.health + (king_1.health/2)))

            for king_2 in self.village.attacker_King:
                if(king_2.alive == True):
                    for i in range(0,king_2.speed):
                        king_2.move()
            for barbarian_2 in self.village.attacker_Barbarian:
                if(barbarian_2.alive == True):
                    for i in range(0,barbarian_2.speed):
                        barbarian_2.move()
            
            #for barbarian_1 in self.village.attacker_Barbarian:
            #    #print("YES")
            #    if(barbarian_1.alive == True):
            #        barbarian_1.move()
            #    #print(barbarian_1.x,barbarian_1.y)
            #    #print(barbarian_1.health)
            #
            #
            #for king_1 in self.village.attacker_King:
            #    if king_1.alive == True:
            #        if (king_1.move == 'D'):
            #            king_1.move_down()
            #        elif (king_1.move == 'U'):
            #            king_1.move_up()
            #        elif (king_1.move == 'L'):
            #            king_1.move_left()
            #        elif (king_1.move == 'R'):
            #            king_1.move_right()
  
            if (self.spell_1 > 0):
                self.spell_1 -= 1

            if ((self.spell_1 == 0) and (self.spell_1_count ==1)):
                for king_1 in self.village.attacker_King:
                    king_1.speed = int(king_1.speed/2)
                for barbarian_1 in self.village.attacker_Barbarian:
                    barbarian_1.speed = int(barbarian_1.speed/2)
                self.spell_1_count = 2


            for building_1 in self.village.existing_Building:
                if(building_1.name == "Cannon" ):
                    if(building_1.alive == True):
                        building_1.attack()
            
            for building_2 in self.village.existing_Building:
                if(building_2.name != "Wall" ):
                    if(building_2.alive == True):
                        self.game_over_win = False

            if self.king_Count == 1:
                for king_2 in self.village.attacker_King:
                    if(king_2.alive == True):
                        self.game_over_lose = False
                        #print("King Alive")
            else:
                self.game_over_lose = False
                #print("No King")
            if self.barbarian_Count == 6:
                for barbarian_2 in self.village.attacker_Barbarian:
                    if(barbarian_2.alive == True):
                        self.game_over_lose = False
                        #print("Barbarian Alive")
            else:
                self.game_over_lose = False
                #print("No Barbarian")

            

            #print("time_period")
            
            

            if(self.game_over_win == True):
                print("YOU WIN")
                break
            elif(self.game_over_lose == True):
                print("YOU LOSE")
                break
            self.start()
            self.display()
            king_bar = "Kings Health:"
            if(self.king_Count == 1):
                king_bar_count = int(self.village.attacker_King[0].health/10)
                #print(king_bar_count)
                for i in range(king_bar_count):
                    king_bar = king_bar +("|")
            print(king_bar)
            time.sleep(TP)
            
            