import copy
import time
import sys
import termios
import tty
import signal
import copy


from input import input_to
from colorama import Fore, Back, Style
from constants import ROW,COL,TP
from village import village

from Build_buildings import empty
from Build_Town_Hall import town_Hall
from Build_Hut import hut
from Build_Cannon import cannon
from Build_WizardTower import WizardTower
from Build_Wall import wall
from Troop_attackers import attackers
from Troop_King import King
from Troop_Queen import Queen
from Troop_Archer import Archer
from Troop_Balloons import Balloon
from Troop_Barbarian import Barbarian

class Game:
    def __init__(self):

        # Game Map
        self.board = []
        self.map = []
        self.air_board = []
        self.air_map = []
        self.village = village(self)
        self.time_Running = 0

        #Troop Count
        self.Character = None    # Hero -> King or Queen
        self.Hero_Count = 0      # No of King or Queen
        self.Barbarian_Count = 0 # No of Barbarian
        self.Archer_Count = 0    # No of Archer
        self.Balloon_Count = 0   # No of Balloon

        #Spell Variables
        self.spell = False
        self.spell_1 = 0
        self.spell_1_count = 0
        self.spell_var_count = 0
        
        # Game Status
        self.level_1 = False
        self.level_2 = False    
        self.level_var = False
        self.game_over = False
        self.game_over_win = True
        self.game_over_lose = True
        
        # Input File
        self.input_File = ""
        
        
        

    #Function to Choose Hero Character
    def Choose_Character(self):
        
        for i in range(100):
            #Display the Message
            print("\033[H\033[J", end="")
            print("Choose Main Character")
            print(" `k` -> King")
            print(" `q` - Queen")

            #Get the Input
            key = input_to()
            if key == 'k':
                self.Character = "King"
                break
            elif key == 'q':
                self.Character = "Queen"
                break
            elif key == None:
                print("Invalid Input")

        if key == None :
            self.input_File = self.input_File +str('G')
        else:
            self.input_File = self.input_File +str(key)

        #Check Input Status
        if self.Character != "King" and self.Character != "Queen":
            print("No Input Given")
            self.game_over = True

    # Start Game
    def start(self):
        for object in self.village.existing_Building:
            object.display()


    # Display the Map Function
    def display(self):
        for j in range(ROW):
            for i in range(COL-1):
                if(self.air_map[j][i]!= None):

                    if(self.air_map[j][i].name=="Balloon"):
                        self.air_map[j][i].display()
                        print(self.air_board[j][i], end='')

                    elif(self.map[j][i].name!="Empty"):
                        self.map[j][i].display()
                        print(self.board[j][i], end='')

                    else:
                        self.board[j][i]=' '
                        print(self.board[j][i], end='')

                elif(self.map[j][i].name!="Empty"):
                    self.map[j][i].display()
                    print(self.board[j][i], end='')
                else:
                    self.board[j][i]=' '
                    print(self.board[j][i], end='')

                print(Style.RESET_ALL, end = '')
            print(self.board[j][COL-1], end='')
            

    # Game Function
    def run(self):

        # Starting the game and display the board
        self.time_Start = time.time()
        self.start()
        print("\033[H\033[J", end="")
        self.display()

        # Game Status update
        self.game_over_win = True
        self.game_over_lose = True
        
        # Game Loop
        while True:

            # Game Status update
            self.game_over_win = True
            self.game_over_lose = True

            # Take Input from user
            key = input_to()
            if key == None :
                self.input_File = self.input_File +str('G')
            else:
                self.input_File = self.input_File +str(key)

            # Clear screen    
            print("\033[H\033[J", end="")
            
            # Time Update
            self.time_Running = float(time.time() - self.time_Start)


            #Barbarian Spawnning
            if  (key == 'i'):
                if(self.Barbarian_Count <5 ):
                    self.village.attacker_Barbarian.append(Barbarian(self,0,12))
                    self.Barbarian_Count += 1
            elif(key == 'o'):
                if(self.Barbarian_Count <5 ):
                    self.village.attacker_Barbarian.append(Barbarian(self,15,0))
                    self.Barbarian_Count += 1
            elif(key == 'p'):
                if(self.Barbarian_Count <5 ):
                    self.village.attacker_Barbarian.append(Barbarian(self,39,12))
                    self.Barbarian_Count += 1

            #Archer Spawnning        
            elif(key == 't'):
                if(self.Archer_Count <5 ):
                    self.village.attacker_Archer.append(Archer(self,0,12))
                    self.Archer_Count += 1
            elif(key == 'y'):
                if(self.Archer_Count <5 ):
                    self.village.attacker_Archer.append(Archer(self,15,0))
                    self.Archer_Count += 1
            elif(key == 'u'):
                if(self.Archer_Count <5 ):
                    self.village.attacker_Archer.append(Archer(self,39,12))
                    self.Archer_Count += 1
            
            #Balloon Spawnning
            elif(key == 'z'):
                if(self.Balloon_Count <3 ):
                    self.village.attacker_Balloon.append(Balloon(self,0,12))
                    self.Balloon_Count += 1
            elif(key == 'x'):
                if(self.Balloon_Count <3 ):
                    self.village.attacker_Balloon.append(Balloon(self,15,0))
                    self.Balloon_Count += 1
            elif(key == 'c'):
                if(self.Balloon_Count <3 ):
                    self.village.attacker_Balloon.append(Balloon(self,39,12))
                    self.Balloon_Count += 1

            #Spells
            elif(key == 'm'):   #Rage Spell
                if(self.spell_1_count==0):
                    self.spell_1_count= 1
                    self.spell_1 = 12

                    # King
                    for King_var in self.village.attacker_King:
                        King_var.speed = 2*King_var.speed

                    # Queen
                    for Queen_var in self.village.attacker_Queen:
                        Queen_var.speed = 2*Queen_var.speed
                    
                    # Barbarian
                    for Barbarian_var in self.village.attacker_Barbarian:
                        Barbarian_var.speed = 2*Barbarian_var.speed
                    
                    # Archer
                    for Archer_var in self.village.attacker_Archer:
                        Archer_var.speed = 2*Archer_var.speed
                    
                    # Balloon
                    for Balloon_var in self.village.attacker_Balloon:
                        Balloon_var.speed = 2*Balloon_var.speed

            elif(key == 'n'):   #Health Spell 
                if(self.spell_var_count==0):
                    self.spell_var_count= 1

                    # King
                    for King_var in self.village.attacker_King:
                        King_var.health = min(100,(King_var.health + (King_var.health/2)))
                    
                    # Queen
                    for Queen_var in self.village.attacker_Queen:
                        Queen_var.health = min(100,(Queen_var.health + (Queen_var.health/2)))

                    # Barbarian
                    for Barbarian_var in self.village.attacker_Barbarian:
                        Barbarian_var.health = min(100,(Barbarian_var.health + (Barbarian_var.health/2)))
                    
                    # Archer
                    for Archer_var in self.village.attacker_Archer:
                        Archer_var.health = min(100,(Archer_var.health + (Archer_var.health/2)))    
                    
                    # Balloon
                    for Balloon_var in self.village.attacker_Balloon:
                        Balloon_var.health = min(100,(Balloon_var.health + (Balloon_var.health/2)))
                    
                    
            
            # Hero Spawnning
            elif self.Character == "King":  #King Case

                #King Spawnning
                if  (key == 'j'):
                    if(self.Hero_Count == 0):
                        self.village.attacker_King.append(King(self,0,12))
                        self.Hero_Count = 1
                elif(key == 'k'):
                    if(self.Hero_Count == 0):
                        self.village.attacker_King.append(King(self,15,0))
                        self.Hero_Count = 1
                elif(key == 'l'):
                    if(self.Hero_Count == 0):
                        self.village.attacker_King.append(King(self,39,12))
                        self.Hero_Count = 1

                #King Movement
                elif(key == 'a'):
                    if(self.Hero_Count == 1):
                        self.village.attacker_King[0].move_direction = 'L'
                elif(key == 'd'):
                    if(self.Hero_Count == 1):
                        self.village.attacker_King[0].move_direction = 'R'
                elif(key == 'w'):
                    if(self.Hero_Count == 1):
                        self.village.attacker_King[0].move_direction = 'U'
                elif(key == 's'):
                    if(self.Hero_Count == 1):
                        self.village.attacker_King[0].move_direction = 'D'
                elif(key == ' '):
                    if(self.Hero_Count == 1):
                        for i in range(0,self.village.attacker_King[0].speed):   
                            self.village.attacker_King[0].attack()
                            self.village.attacker_King[0].move_direction = ' '
            
            elif self.Character == "Queen": #Queen [Archer Queen] Case

                #Queen Spawnning
                if(key == 'j'):
                    if(self.Hero_Count == 0):
                        self.village.attacker_Queen.append(Queen(self,0,12))
                        self.Hero_Count = 1
                elif(key == 'k'):
                    if(self.Hero_Count == 0):
                        self.village.attacker_Queen.append(Queen(self,15,0))
                        self.Hero_Count = 1
                elif(key == 'l'):
                    if(self.Hero_Count == 0):
                        self.village.attacker_Queen.append(Queen(self,39,12))
                        self.Hero_Count = 1

                #Queen Movement
                elif(key == 'a'):
                    if(self.Hero_Count == 1):
                        self.village.attacker_Queen[0].move_direction = 'L'
                        self.village.attacker_Queen[0].attack_direction = 'L'
                elif(key == 'd'):
                    if(self.Hero_Count == 1):
                        self.village.attacker_Queen[0].move_direction = 'R'
                        self.village.attacker_Queen[0].attack_direction = 'R'
                elif(key == 'w'):
                    if(self.Hero_Count == 1):
                        self.village.attacker_Queen[0].move_direction = 'U'
                        self.village.attacker_Queen[0].attack_direction = 'U'
                elif(key == 's'):
                    if(self.Hero_Count == 1):
                        self.village.attacker_Queen[0].move_direction = 'D'
                        self.village.attacker_Queen[0].attack_direction = 'D'
                elif(key == ' '):
                    if(self.Hero_Count == 1):
                        for i in range(0,self.village.attacker_Queen[0].speed):   
                            self.village.attacker_Queen[0].move_direction = ' '
                            self.village.attacker_Queen[0].attack()
            
        

            # King Movement for each time step
            for King_var in self.village.attacker_King:
                if(King_var.alive == True):
                    for i in range(0,King_var.speed):
                        King_var.move()

            # Queen Movement for each time step
            for Queen_var in self.village.attacker_Queen:
                if(Queen_var.alive == True):
                    for i in range(0,Queen_var.speed):
                        Queen_var.move()

            # Barbarian Movement for each time step
            for Barbarian_var in self.village.attacker_Barbarian:
                if(Barbarian_var.alive == True):
                    for i in range(0,Barbarian_var.speed):
                        Barbarian_var.move()
            
            # Archer Movement for each time step
            for Archer_var in self.village.attacker_Archer:
                if(Archer_var.alive == True):
                    for i in range(0,Archer_var.speed):
                        Archer_var.move()
            
            # Balloon Movement for each time step
            for Balloon_var in self.village.attacker_Balloon:
                if(Balloon_var.alive == True):
                    for i in range(0,Balloon_var.speed):
                        Balloon_var.move()
            

            # Comming Back to normal after a Rage Spell
            if (self.spell_1 > 0):
                self.spell_1 -= 1

            if ((self.spell_1 == 0) and (self.spell_1_count ==1)):
                # King 
                for King_var in self.village.attacker_King:
                    King_var.speed = int(King_var.speed/2)

                #Queen 
                for Queen_var in self.village.attacker_Queen:
                    Queen_var.speed = int(Queen_var.speed/2)

                #Archer
                for Archer_var in self.village.attacker_Archer:
                    Archer_var.speed = int(Archer_var.speed/2)

                #Barbarian 
                for Barbarian_var in self.village.attacker_Barbarian:
                    Barbarian_var.speed = int(Barbarian_var.speed/2)
                
                #Balloon
                for Balloon_var in self.village.attacker_Balloon:
                    Balloon_var.speed = int(Balloon_var.speed/2)

                self.spell_1_count = 2

            # Cannon Attacking Troops in Each Time step
            for Cannon_var in self.village.existing_Building:
                if(Cannon_var.name == "Cannon" ):
                    if(Cannon_var.alive == True):
                        Cannon_var.attack()
            
            # ArcherTower Attacking Troops in Each Time step
            for WizardTower_var in self.village.existing_Building:
                if(WizardTower_var.name == "WizardTower" ):
                    if(WizardTower_var.alive == True):
                        WizardTower_var.attack()

            #Checking Extistence of Non Wall Buildings
            for building_var in self.village.existing_Building:
                if(building_var.name != "Wall" ):
                    if(building_var.alive == True):
                        self.game_over_win = False

            #Checking Extistence of Hero Character 
            if self.Hero_Count == 1:
                for King_var in self.village.attacker_King:
                    if(King_var.alive == True):         #Hero Character is Alive [No Loss]
                        self.game_over_lose = False
                        #print("King Alive")

                for Queen_var in self.village.attacker_Queen:
                    if(Queen_var.alive == True):        #Hero Character is Alive [No Loss]
                        self.game_over_lose = False
            else:
                self.game_over_lose = False             #Hero Character is not Spawnned yet No Loss]
                
            
            #Checking Extistence of Barbarian Troops
            if self.Barbarian_Count == 5:
                for Barbarian_var in self.village.attacker_Barbarian:
                    if(Barbarian_var.alive == True):
                        self.game_over_lose = False     #Some Barbarian are Alive [No Loss]
                        
            else:
                self.game_over_lose = False             #All Barbarians not Spawnned yet [No Loss]
                

            #Checking Extistence of Archer Troops
            if self.Archer_Count == 5:
                for Archer_var in self.village.attacker_Archer:
                    if(Archer_var.alive == True):
                        self.game_over_lose = False     #Some Archer are Alive [No Loss]
            else:
                self.game_over_lose = False             #All Archer not Spawnned yet [No Loss]

            #Checking Extistence of Balloon Troops
            if self.Balloon_Count == 3:
                for Balloon_var in self.village.attacker_Balloon:
                    if(Balloon_var.alive == True):
                        self.game_over_lose = False     #Some Balloon are Alive [No Loss]
            else:
                self.game_over_lose = False             #All Balloon not Spawnned yet [No Loss]

            

            
            
            # Win or Lose
            if(self.game_over_win == True):
                
                empty_village = [[' ' for i in range(COL)] for j in range(ROW)]
                for j in range(ROW):
                    empty_village[j][40]='\n';
                empty_village_map = [[empty(self,i,j) for i in range(COL)] for j in range(ROW)]
                
                self.village.attacker_King.clear()
                self.village.attacker_Queen.clear()
                self.village.attacker_Barbarian.clear()
                self.village.attacker_Archer.clear()
                self.village.attacker_Balloon.clear()
                self.village.existing_Building.clear()

                self.board.clear()
                self.map.clear()
                self.air_board.clear()
                self.air_map.clear()
                
                
                self.Barbarian_Count = 0
                self.Archer_Count = 0
                self.Balloon_Count = 0
                self.Hero_Count = 0

                self.spell = False
                self.spell_1 = 0
                self.spell_1_count = 0
                self.spell_var_count = 0                
                
                self.game_over_win = False

                self.board = copy.deepcopy(empty_village)
                self.map = copy.deepcopy(empty_village_map)
                self.air_board = copy.deepcopy(empty_village)
                self.air_map = copy.deepcopy(empty_village_map)
                
                if(self.level_1 == False):
                    self.level_1 = True
                    print("YOU CLEAR LEVEL 1")
                    self.village.existing_Building = [town_Hall(self,18,10),
                                hut(self,1,1),
                                hut(self,37,1),
                                hut(self,1,17),
                                hut(self,37,17),
                                hut(self,8,9),
                                hut(self,30,11),
                                hut(self,23,10),
                                hut(self,19,7),
                                cannon(self,23,7),
                                cannon(self,23,14),
                                WizardTower(self,16,7),
                                WizardTower(self,24,15),
                                wall(self,4,0),wall(self,4,1),wall(self,4,2),wall(self,4,3),wall(self,4,4),
                                wall(self,0,4),wall(self,1,4),wall(self,2,4),wall(self,3,4),
                                wall(self,35,0),wall(self,35,1),wall(self,35,2),wall(self,35,3),wall(self,35,4),
                                wall(self,36,4),wall(self,37,4),wall(self,38,4),wall(self,39,4),
                                wall(self,35,15),wall(self,35,16),wall(self,35,17),wall(self,35,18),wall(self,35,19),
                                wall(self,36,15),wall(self,37,15),wall(self,38,15),wall(self,39,15),
                                wall(self,4,15),wall(self,4,16),wall(self,4,17),wall(self,4,18),wall(self,4,19),
                                wall(self,0,15),wall(self,1,15),wall(self,2,15),wall(self,3,15),
                                wall(self,13,5),wall(self,14,5),wall(self,15,5),wall(self,16,5),wall(self,17,5),wall(self,18,5),wall(self,19,5),wall(self,20,5),wall(self,21,5),wall(self,22,5),wall(self,23,5),wall(self,24,5),wall(self,25,5),wall(self,26,5),
                                wall(self,13,17),wall(self,14,17),wall(self,15,17),wall(self,16,17),wall(self,17,17),wall(self,18,17),wall(self,19,17),wall(self,20,17),wall(self,21,17),wall(self,22,17),wall(self,23,17),wall(self,24,17),wall(self,25,17),wall(self,26,17),
                                wall(self,13,6),wall(self,13,7),wall(self,13,8),wall(self,13,9),wall(self,13,10),wall(self,13,11),wall(self,13,12),wall(self,13,13),wall(self,13,14),wall(self,13,15),wall(self,13,16),
                                wall(self,26,6),wall(self,26,7),wall(self,26,8),wall(self,26,9),wall(self,26,10),wall(self,26,11),wall(self,26,12),wall(self,26,13),wall(self,26,14),wall(self,26,15),wall(self,26,16),
                                wall(self,16,10),wall(self,16,11),wall(self,16,12),wall(self,16,13),wall(self,16,14),
                                wall(self,17,14),wall(self,18,14),wall(self,19,14),wall(self,20,14),wall(self,21,14),
                                wall(self,36,6),wall(self,36,7),wall(self,36,8),wall(self,36,9),wall(self,36,10),wall(self,36,11),wall(self,36,12),wall(self,36,13),wall(self,36,14),
                                wall(self,3,6),wall(self,3,7),wall(self,3,8),wall(self,3,9),wall(self,3,10),wall(self,3,11),wall(self,3,12),wall(self,3,13),wall(self,3,14),
                                wall(self,11,6),wall(self,11,7),wall(self,11,8),wall(self,11,9),wall(self,11,10),wall(self,11,11),wall(self,11,12),wall(self,11,13),wall(self,11,14),
                                wall(self,28,6),wall(self,28,7),wall(self,28,8),wall(self,28,9),wall(self,28,10),wall(self,28,11),wall(self,28,12),wall(self,28,13),wall(self,28,14),
                                wall(self,4,14),wall(self,5,14),wall(self,6,14),wall(self,7,14),wall(self,8,14),wall(self,9,14),wall(self,10,14),
                                wall(self,4,6),wall(self,5,6),wall(self,6,6),wall(self,7,6),wall(self,8,6),wall(self,9,6),wall(self,10,6),
                                wall(self,29,14),wall(self,30,14),wall(self,31,14),wall(self,32,14),wall(self,33,14),wall(self,34,14),wall(self,35,14),
                                wall(self,29,6),wall(self,30,6),wall(self,31,6),wall(self,32,6),wall(self,33,6),wall(self,34,6),wall(self,35,6),
                                
                                #LEVEL 2 addition
                                cannon(self,8,12),
                                WizardTower(self,30,8),
                                hut(self,33,8),
                                hut(self,5,11),
                                cannon(self,8,0),wall(self,7,0),wall(self,9,0),wall(self,7,1),wall(self,8,1),wall(self,9,1),
                                cannon(self,31,19),wall(self,30,19),wall(self,32,19),wall(self,30,18),wall(self,31,18),wall(self,32,18),
                                
                                # LEVEL 3 addition
                                # hut(self,5,8),
                                # hut(self,33,11),
                                # WizardTower(self,8,19),wall(self,7,19),wall(self,9,19),wall(self,7,18),wall(self,8,18),wall(self,9,18),
                                # cannon(self,31,19),wall(self,30,19),wall(self,32,19),wall(self,30,18),wall(self,31,18),wall(self,32,18),
                                
                            ]

                elif(self.level_2 == False):
                    self.level_2 = True
                    print("YOU CLEAR LEVEL 2")
                    self.village.existing_Building = [town_Hall(self,18,10),
                                hut(self,1,1),
                                hut(self,37,1),
                                hut(self,1,17),
                                hut(self,37,17),
                                hut(self,8,9),
                                hut(self,30,11),
                                hut(self,23,10),
                                hut(self,19,7),
                                cannon(self,23,7),
                                cannon(self,23,14),
                                WizardTower(self,16,7),
                                WizardTower(self,24,15),
                                wall(self,4,0),wall(self,4,1),wall(self,4,2),wall(self,4,3),wall(self,4,4),
                                wall(self,0,4),wall(self,1,4),wall(self,2,4),wall(self,3,4),
                                wall(self,35,0),wall(self,35,1),wall(self,35,2),wall(self,35,3),wall(self,35,4),
                                wall(self,36,4),wall(self,37,4),wall(self,38,4),wall(self,39,4),
                                wall(self,35,15),wall(self,35,16),wall(self,35,17),wall(self,35,18),wall(self,35,19),
                                wall(self,36,15),wall(self,37,15),wall(self,38,15),wall(self,39,15),
                                wall(self,4,15),wall(self,4,16),wall(self,4,17),wall(self,4,18),wall(self,4,19),
                                wall(self,0,15),wall(self,1,15),wall(self,2,15),wall(self,3,15),
                                wall(self,13,5),wall(self,14,5),wall(self,15,5),wall(self,16,5),wall(self,17,5),wall(self,18,5),wall(self,19,5),wall(self,20,5),wall(self,21,5),wall(self,22,5),wall(self,23,5),wall(self,24,5),wall(self,25,5),wall(self,26,5),
                                wall(self,13,17),wall(self,14,17),wall(self,15,17),wall(self,16,17),wall(self,17,17),wall(self,18,17),wall(self,19,17),wall(self,20,17),wall(self,21,17),wall(self,22,17),wall(self,23,17),wall(self,24,17),wall(self,25,17),wall(self,26,17),
                                wall(self,13,6),wall(self,13,7),wall(self,13,8),wall(self,13,9),wall(self,13,10),wall(self,13,11),wall(self,13,12),wall(self,13,13),wall(self,13,14),wall(self,13,15),wall(self,13,16),
                                wall(self,26,6),wall(self,26,7),wall(self,26,8),wall(self,26,9),wall(self,26,10),wall(self,26,11),wall(self,26,12),wall(self,26,13),wall(self,26,14),wall(self,26,15),wall(self,26,16),
                                wall(self,16,10),wall(self,16,11),wall(self,16,12),wall(self,16,13),wall(self,16,14),
                                wall(self,17,14),wall(self,18,14),wall(self,19,14),wall(self,20,14),wall(self,21,14),
                                wall(self,36,6),wall(self,36,7),wall(self,36,8),wall(self,36,9),wall(self,36,10),wall(self,36,11),wall(self,36,12),wall(self,36,13),wall(self,36,14),
                                wall(self,3,6),wall(self,3,7),wall(self,3,8),wall(self,3,9),wall(self,3,10),wall(self,3,11),wall(self,3,12),wall(self,3,13),wall(self,3,14),
                                wall(self,11,6),wall(self,11,7),wall(self,11,8),wall(self,11,9),wall(self,11,10),wall(self,11,11),wall(self,11,12),wall(self,11,13),wall(self,11,14),
                                wall(self,28,6),wall(self,28,7),wall(self,28,8),wall(self,28,9),wall(self,28,10),wall(self,28,11),wall(self,28,12),wall(self,28,13),wall(self,28,14),
                                wall(self,4,14),wall(self,5,14),wall(self,6,14),wall(self,7,14),wall(self,8,14),wall(self,9,14),wall(self,10,14),
                                wall(self,4,6),wall(self,5,6),wall(self,6,6),wall(self,7,6),wall(self,8,6),wall(self,9,6),wall(self,10,6),
                                wall(self,29,14),wall(self,30,14),wall(self,31,14),wall(self,32,14),wall(self,33,14),wall(self,34,14),wall(self,35,14),
                                wall(self,29,6),wall(self,30,6),wall(self,31,6),wall(self,32,6),wall(self,33,6),wall(self,34,6),wall(self,35,6),
                                
                                # LEVEL 2 addition
                                cannon(self,8,12),
                                WizardTower(self,30,8),
                                hut(self,33,8),
                                hut(self,5,11),
                                cannon(self,8,0),wall(self,7,0),wall(self,9,0),wall(self,7,1),wall(self,8,1),wall(self,9,1),
                                cannon(self,31,19),wall(self,30,19),wall(self,32,19),wall(self,30,18),wall(self,31,18),wall(self,32,18),
                                
                                # LEVEL 3 addition
                                hut(self,5,8),
                                hut(self,33,11),
                                WizardTower(self,8,19),wall(self,7,19),wall(self,9,19),wall(self,7,18),wall(self,8,18),wall(self,9,18),
                                cannon(self,31,0),wall(self,30,0),wall(self,32,0),wall(self,30,1),wall(self,31,1),wall(self,32,1),
                                cannon(self,19,4),wall(self,18,4),wall(self,20,4),wall(self,18,3),wall(self,19,3),wall(self,20,3),
                                
                                
                            ]

                else:
                    print("YOU WIN")
                    break
                
            elif(self.game_over_lose == True):
                print("YOU LOSE")
                break

            # Displaying the Current Status of Village
            self.start()
            self.display()

            if self.level_1 == False:
                print("level_1")
            elif self.level_2 == False:
                print("level_2")
            else:
                print("level_3")
            Hero_bar = 0
            Hero_bar_count = 0
            # Finding the Hero's Health Bar String
            if self.Character == "King":
                Hero_bar = "Kings Health:"
            elif self.Character == "Queen":
                Hero_bar = "Queens Health:"

            if(self.Hero_Count == 1):

                # Calculating no of Bars
                if(self.Character == "King"):
                    Hero_bar_count = int(self.village.attacker_King[0].health/10)
                elif(self.Character == "Queen"):
                    Hero_bar_count = int(self.village.attacker_Queen[0].health/10)

                #print(King_bar_count)
                for i in range(Hero_bar_count):
                    Hero_bar = Hero_bar +("|")
                
                # Displaying the Hero Health Bar
                print(Hero_bar)

            # Sleep
            time.sleep(TP)
            
            