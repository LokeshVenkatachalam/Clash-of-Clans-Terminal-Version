from constants import COL,ROW,INFINITY
from Build_buildings import empty
from village import village
from colorama import Fore, Back, Style
from Troop_attackers import attackers

# Barbarian
class Barbarian(attackers):

    # Intialize
    def __init__(self,game,X_coord,Y_coord,name="Barbarian",symbol='B',hitpoint= 25,speed= 1,color=Fore.BLUE ):
        super().__init__(name,game,X_coord, Y_coord, symbol, hitpoint, speed,color)
        self.strength = 350
        self.strength_Max = 350 
        self.target = None
        self.x_dir = 0
        self.y_dir = 0
        self.x_dist = 0
        self.y_dist = 0

        # self.move_x = 0
        # self.move_y = 0
        
    # Attack
    def attack(self,X_coord,Y_coord):
        self.game.map[Y_coord][X_coord].get_attack(self.hitpoint)

    # Display
    def display(self):
        if(self.alive == True):
            if(self.health>40):
                self.color = Fore.BLUE + Style.DIM
            elif(self.health>0):
                self.color = Fore.LIGHTBLUE_EX + Style.BRIGHT
            self.game.board[self.y][self.x] = self.color+self.symbol
    
    # Move
    def move(self):
        if(self.alive== True):      # Checking whether Barbarian is alive
            if(self.target==None):  # Checking whether Barbarian has target

                # Finding Target
                temp = None
                x_dist = 0
                y_dist = 0
                for short_Dist in range(1,max(max(self.x,(COL-2)-self.x),max(self.y,(ROW-1)-self.y))):
                    
                    # Checking Row
                    for x_coord in range(max(0,self.x-short_Dist),min(COL-2,self.x+short_Dist)+1):
                        
                        # Bottom Row
                        if(self.y>=short_Dist):
                            y_coord = self.y-short_Dist
                            for building_var in self.game.village.buildings:
                                if(self.game.map[y_coord][x_coord].name == building_var):
                                    temp = self.game.map[y_coord][x_coord]
                                    y_dist = y_coord - self.y
                                    x_dist = x_coord - self.x
                                    break

                        
                        if temp != None:
                            break
                        
                        # Top Row
                        if(self.y<=(ROW-1)-short_Dist):
                            y_coord = self.y+short_Dist
                            for building_var in self.game.village.buildings:
                                if(self.game.map[y_coord][x_coord].name == building_var):
                                    temp = self.game.map[y_coord][x_coord]
                                    y_dist = y_coord - self.y
                                    x_dist = x_coord - self.x
                                    break
                        
                        if temp != None:
                            break
                        

                    # Checking Column
                    if(temp == None):
                        for y_coord in range(max(0,self.y-short_Dist),min(ROW-1,self.y+short_Dist)+1):
                            
                            # Left Column
                            if(self.x>=short_Dist):
                                x_coord = self.x-short_Dist
                                for building_var in self.game.village.buildings:
                                    if(self.game.map[y_coord][x_coord].name == building_var):
                                        temp = self.game.map[y_coord][x_coord]
                                        y_dist = y_coord - self.y
                                        x_dist = x_coord - self.x
                                        break
                            
                            if temp != None:
                                break

                            # Right Column
                            if(self.x<(COL-1)-short_Dist):
                                x_coord = self.x+short_Dist
                                for building_var in self.game.village.buildings:
                                    if(self.game.map[y_coord][x_coord].name == building_var):
                                        temp = self.game.map[y_coord][x_coord]
                                        y_dist = y_coord - self.y
                                        x_dist = x_coord - self.x
                                        break
                            
                            if temp != None:
                                break
                            
                    if(temp != None):
                        break
                
                # Assigning Target
                if(temp != None):
                    self.target = temp

                    self.x_dist = x_dist
                    self.y_dist = y_dist
                    if x_dist >=0:
                        self.x_dir  = 1
                    else:
                        self.x_dir  = -1
                    if y_dist >=0:
                        self.y_dir  = 1
                    else:
                        self.y_dir  = -1
                    
                    if min(x_dist, y_dist) > 1:
                        self.line_dist = (max(abs(x_dist), abs(y_dist))-1)/(min(abs(x_dist), abs(y_dist))-1)
                    else:
                        self.line_dist = INFINITY
                    # Move after finding the targer
                    self.move()

            elif(self.target.alive == True):
                # Move towards target

                move_x = 0
                move_y = 0

                # Finding the move directions

                if self.x_dist*self.x_dir > self.y_dist*self.y_dir:
                    
                    if self.x_dist*self.x_dir % self.line_dist == 0 :
                        move_y = self.y_dir
                    
                    move_x = self.x_dir

                else:
                    
                    if self.y_dist*self.y_dir % self.line_dist == 0 :
                        move_x = self.x_dir

                    move_y = self.y_dir

                # Checking whether move directions are valid
                    
                if(self.x+move_x < 0) or (self.y+move_x) >= COL-1: 
                    move_x = 0
                if(self.y+move_y < 0) or (self.y+move_y) >= ROW:
                    move_y = 0

               

                # Finding the type of Move ["Attack","Move"]

                Move = None
                
                # Finding the shortest distance to Target

                for x1 in {-1,0,1}:
                    for y1 in {-1,0,1}:
                        if self.x+x1>0 and self.y+y1>0 and self.x+x1<COL-1 and self.y+y1<ROW:
                            if self.game.map[self.y+y1][self.x+x1] == self.target:
                                Move = "Attack"
                                move_x = x1
                                move_y = y1
                                break

                if Move == None:
                    
                    # Current move point point wall -> "Attack Wall"
                    if self.game.map[self.y+move_y][self.x+move_x].symbol == 'W':
                        Move = "Attack"

                    # Current move point Target -> "Attack"
                    elif (self.game.map[self.y+move_y][self.x+move_x] == self.target):
                        Move = "Attack"
                    
                    # Current move point to empty space -> "Move"
                    elif (self.game.map[self.y+move_y][self.x+move_x].symbol == ' '):
                        Move = "Move"
                    
                    # Finding whether any empty space in neighbourhood 
                    else:
                        move_x = 0
                        move_y = 0
                        min_dist = INFINITY

                        for x_2 in range(self.target.x_start,self.target.x2):
                            for y_2 in range(self.target.y_start,self.target.y2):
                                if max(abs(x_2-self.x),abs(y_2-self.y)) < min_dist :
                                    min_dist = max(abs(x_2-self.x),abs(y_2-self.y))

                        for x_1 in {-1,0,1}:
                            for y_1 in {-1,0,1}:
                                if self.x+x_1>=0 and self.y+y_1>=0 and self.x+x_1<COL-1 and self.y+y_1<ROW:
                                    if(self.game.map[self.y+y_1][self.x+x_1].symbol == ' '):
                                        
                                        close_dist = INFINITY

                                        for x_2 in range(self.target.x_start,self.target.x2):
                                            for y_2 in range(self.target.y_start,self.target.y2):
                                                if max(abs(x_2-(self.x+x_1)),abs(y_2-(self.y+y_1))) < close_dist :
                                                    close_dist = max(abs(x_2-(self.x+x_1)),abs(y_2-(self.y+y_1)))

                                        
                                        if close_dist < min_dist:
                                            move_x = x_1
                                            move_y = y_1

                        if move_x !=0 or move_y !=0:
                            Move = "Move_1"

                if Move == "Attack":
                    self.attack(self.x+move_x,self.y+move_y)
                
                elif Move == "Move":

                    self.game.board[self.y][self.x] = ' '
                    self.game.map[self.y][self.x] = empty(self.game,self.x,self.y)
                    self.x = self.x + move_x
                    self.y = self.y + move_y
                    self.x_dist = self.x_dist - move_x
                    self.y_dist = self.y_dist - move_y
                    self.game.board[self.y][self.x] = self.symbol
                    self.game.map[self.y][self.x] = self

                elif Move == "Move_1":

                    self.game.board[self.y][self.x] = ' '
                    self.game.map[self.y][self.x] = empty(self.game,self.x,self.y)
                    self.x = self.x + move_x
                    self.y = self.y + move_y
                    self.x_dist = self.x_dist - move_x
                    self.y_dist = self.y_dist - move_y
                    self.game.board[self.y][self.x] = self.symbol
                    self.game.map[self.y][self.x] = self
                    
                    # Go to that position and find new target
                    self.target = None
            
                move_x = 0
                move_y = 0

            elif(self.target.alive == False):
                self.target=None
                self.move()    

    
        