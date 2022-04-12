from constants import COL,ROW,INFINITY
from Build_buildings import empty
from village import village
from colorama import Fore, Back, Style
from Troop_attackers import attackers

# Archer 
class Archer(attackers):

    def __init__(self,game,X_coord,Y_coord,name="Archer",symbol='A',hitpoint= 12.5,speed= 2,color=Fore.BLUE ):
        super().__init__(name,game,X_coord, Y_coord, symbol, hitpoint, speed,color)
        self.strength = 175
        self.strength_Max = 175
        self.target_available = False
        self.target_x = 0
        self.target_y = 0
        self.x_dir = 0
        self.y_dir = 0
        self.x_dist = 0
        self.y_dist = 0
        self.range = 2

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

    # Check Target Availability
    def check_target_available(self,X_coord,Y_coord,Range):
        
        target_Found = False
        for x_1 in range(max(0,X_coord-Range),min((COL-2),X_coord+Range)+1):

            y_1 = Y_coord-Range
            if y_1>= 0 and y_1<ROW:
                for Building_var in self.game.village.buildings:
                    if(self.game.map[y_1][x_1].name == Building_var):
                        target_Found = True
                        break
                        #self.game.map[y_1][x_1].get_attack(self.hitpoint)
            
            y_1 = Y_coord+Range
            if y_1>= 0 and y_1<ROW:
                for Building_var in self.game.village.buildings:
                    if(self.game.map[y_1][x_1].name == Building_var):
                        target_Found = True
                        break

        if target_Found == False:
            for y_1 in range(max(0,Y_coord-(Range-1)),min((ROW-1),Y_coord+(Range-1))+1):

                x_1 = X_coord-Range
                if x_1>= 0 and x_1<COL-1:
                    for Building_var in self.game.village.buildings:
                        if(self.game.map[y_1][x_1].name == Building_var):
                            target_Found = True
                            break
                            #self.game.map[y_1][x_1].get_attack(self.hitpoint)
                
                x_1 = X_coord+Range
                if x_1>= 0 and x_1<COL-1:
                    for Building_var in self.game.village.buildings:
                        if(self.game.map[y_1][x_1].name == Building_var):
                            target_Found = True
                            break
        return target_Found

    # Attack Available target
    def attack_target_available(self,X_coord,Y_coord,Range):
        
        target_Found = False
        for x_1 in range(max(0,X_coord-Range),min((COL-2),X_coord+Range)+1):

            y_1 = Y_coord-Range
            if y_1>= 0 and y_1<ROW:
                for Building_var in self.game.village.buildings:
                    if(self.game.map[y_1][x_1].name == Building_var):
                        target_Found = True
                        self.game.map[y_1][x_1].get_attack(self.hitpoint)
                        break
            
            y_1 = Y_coord+Range
            if y_1>= 0 and y_1<ROW:
                for Building_var in self.game.village.buildings:
                    if(self.game.map[y_1][x_1].name == Building_var):
                        target_Found = True
                        self.game.map[y_1][x_1].get_attack(self.hitpoint)
                        break

        if target_Found == False:
            for y_1 in range(max(0,Y_coord-(Range-1)),min((ROW-1),Y_coord+(Range-1))+1):

                x_1 = X_coord-Range
                if x_1>= 0 and x_1<COL-1:
                    for Building_var in self.game.village.buildings:
                        if(self.game.map[y_1][x_1].name == Building_var):
                            target_Found = True
                            self.game.map[y_1][x_1].get_attack(self.hitpoint)
                            break
                
                x_1 = X_coord+Range
                if x_1>= 0 and x_1<COL-1:
                    for Building_var in self.game.village.buildings:
                        if(self.game.map[y_1][x_1].name == Building_var):
                            target_Found = True
                            self.game.map[y_1][x_1].get_attack(self.hitpoint)
                            break


    # Move
    def move(self):
        if(self.alive== True):                 # Checking whether Archer is alive
            if(self.target_available==False):  # Checking whether Archer has target

                # Finding Target
                destination = False
                x_dist = 0
                y_dist = 0
                for short_Dist in range(1,max(max(self.x,(COL-2)-self.x),max(self.y,(ROW-1)-self.y))):
                    
                    # Checking Row
                    for x_coord in range(max(0,self.x-short_Dist),min(COL-2,self.x+short_Dist)+1):
                        
                        # Bottom Row
                        if(self.y>=short_Dist):
                            y_coord = self.y-short_Dist
                            if(self.check_target_available(x_coord,y_coord,self.range)):
                                y_dist = y_coord - self.y
                                x_dist = x_coord - self.x
                                self.target_available = True
                                self.target_x = x_coord
                                self.target_y = y_coord
                                break

                        if (self.y<=(ROW-1)-short_Dist):
                            y_coord = self.y+short_Dist
                            if(self.check_target_available(x_coord,y_coord,self.range)):
                                y_dist = y_coord - self.y
                                x_dist = x_coord - self.x
                                self.target_available = True
                                self.target_x = x_coord
                                self.target_y = y_coord
                                break
                    
                    if self.target_available == False:
                        for y_coord in range(max(0,self.y-short_Dist),min(ROW-1,self.y+short_Dist)+1):
                            
                            # Left Column
                            if(self.x>=short_Dist):
                                x_coord = self.x-short_Dist

                                if(self.check_target_available(x_coord,y_coord,self.range)):
                                    y_dist = y_coord - self.y
                                    x_dist = x_coord - self.x
                                    self.target_available = True
                                    self.target_x = x_coord
                                    self.target_y = y_coord
                                    break
                                

                            # Right Column
                            if(self.x<=(COL-2)-short_Dist):
                                x_coord = self.x+short_Dist
                                if(self.check_target_available(x_coord,y_coord,self.range)):
                                    y_dist = y_coord - self.y
                                    x_dist = x_coord - self.x
                                    self.target_available = True
                                    self.target_x = x_coord
                                    self.target_y = y_coord
                                    break
                    
                    if(self.target_available == True):
                        break
                
                # Assigning Target
                if(self.target_available == True):
                    
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
                    # Move after finding the target
                    self.move()

            elif(self.check_target_available(self.target_x,self.target_y,self.range) == True):
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

                if self.check_target_available(self.x,self.y,self.range) == True:
                    Move = "Attack"

                if Move == None:
                    
                    # Current move point point wall -> "Attack Wall"
                    if self.game.map[self.y+move_y][self.x+move_x].symbol == 'W':
                        Move = "Attack_1"
                    
                    # Current move point to empty space -> "Move"
                    elif (self.game.map[self.y+move_y][self.x+move_x].symbol == ' '):
                        Move = "Move"
                        
                    # Finding whether any empty space in neighbourhood 
                    else:
                        move_x = 0
                        move_y = 0
                        min_dist = max(abs(self.target_x-self.x),abs(self.target_y-self.y))


                        for x_1 in {-1,0,1}:
                            for y_1 in {-1,0,1}:
                                if self.x+x_1>=0 and self.y+y_1>=0 and self.x+x_1<COL and self.y+y_1<ROW:
                                    if(self.game.map[self.y+y_1][self.x+x_1].symbol == ' '):
                                        close_dist =  max(abs(self.target_x-(self.x+x_1)),abs(self.target_y-(self.y+y_1)))
                                        if close_dist < min_dist:
                                            move_x = x_1
                                            move_y = y_1

                        if move_x !=0 or move_y !=0:
                            Move = "Move_1"

                
                
                if Move == "Attack":
                    self.attack_target_available(self.x,self.y,self.range)

                elif Move == "Attack_1":
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
                    self.target_available = False
            
                move_x = 0
                move_y = 0

            elif(self.check_target_available(self.target_x, self.target_y,self.range) == False):
                self.target_available=False
                self.move()


