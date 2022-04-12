from constants import COL,ROW,INFINITY
from Build_buildings import empty
from village import village
from colorama import Fore, Back, Style
from Troop_attackers import attackers

class air_attackers:

    # Intialize
    def __init__(self,name,game,X_coord, Y_coord,symbol, hitpoint, speed,color):

        self.name = name
        self.game = game
        
        # Characteristics
        self.hitpoint = hitpoint
        self.speed = speed
        self.symbol = symbol
        self.health = 100
        self.alive = True

        # Position
        self.x = X_coord
        self.y = Y_coord

        # Display
        self.color = color
        self.game.air_board[self.y][self.x] = self.symbol
        self.game.air_map[self.y][self.x] = self
        
    # Death of Troop
    def death(self):
        self.alive = False
        self.game.air_board[self.y][self.x] = ' '
        self.game.air_map[self.y][self.x] = empty(self.game,self.x,self.y)
    
    # Display
    def display(self):
        if(self.alive == True):
            self.game.air_board[self.y][self.x] = self.color+Style.BRIGHT + self.symbol


class Balloon(air_attackers):

   # Intialize
    def __init__(self,game,X_coord,Y_coord,name="Balloon",symbol='o',hitpoint= 50,speed= 2,color=Fore.BLUE ):
        super().__init__(name,game,X_coord, Y_coord, symbol, hitpoint, speed,color)
        self.strength = 350
        self.strength_Max = 350 
        self.target = None
        self.x_dir = 0
        self.y_dir = 0
        self.x_dist = 0
        self.y_dist = 0
        
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
            self.game.air_board[self.y][self.x] = self.color+self.symbol
    
    # Move
    def move(self):
        if(self.alive== True):      # Checking whether Balloon is alive
            if(self.target==None):  # Checking whether Balloon has target

                # Finding Target
                temp = None
                x_dist = 0
                y_dist = 0
                for short_Dist in range(1,max(max(self.x,(COL-2)-self.x),max(self.y,(ROW-1)-self.y))+1):
                    
                    # Checking Row Defensive Building
                    for x_coord in range(max(0,self.x-short_Dist),min(COL-2,self.x+short_Dist)+1):
                        
                        # Bottom Row
                        if(self.y>=short_Dist):
                            y_coord = self.y-short_Dist
                            for building_var in self.game.village.defensive_Building:
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
                            for building_var in self.game.village.defensive_Building:
                                if(self.game.map[y_coord][x_coord].name == building_var):
                                    temp = self.game.map[y_coord][x_coord]
                                    y_dist = y_coord - self.y
                                    x_dist = x_coord - self.x
                                    break
                        
                        if temp != None:
                            break
                        

                    # Checking Column Defensive Building
                    if(temp == None):
                        for y_coord in range(max(0,self.y-short_Dist),min(ROW-1,self.y+short_Dist)+1):
                            
                            # Left Column
                            if(self.x>=short_Dist):
                                x_coord = self.x-short_Dist
                                for building_var in self.game.village.defensive_Building:
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
                                for building_var in self.game.village.defensive_Building:
                                    if(self.game.map[y_coord][x_coord].name == building_var):
                                        temp = self.game.map[y_coord][x_coord]
                                        y_dist = y_coord - self.y
                                        x_dist = x_coord - self.x
                                        break
                            
                            if temp != None:
                                break
                    
                    if temp != None:
                        break

                if temp == None :
                    for short_Dist in range(1,max(max(self.x,(COL-2)-self.x),max(self.y,(ROW-1)-self.y))+1):

                        # Checking Row Normal Building

                        if(temp == None):
                            for x_coord in range(max(0,self.x-short_Dist),min(COL-2,self.x+short_Dist)+1):
                                
                                # Bottom Row
                                if(self.y>=short_Dist):
                                    y_coord = self.y-short_Dist
                                    for building_var in self.game.village.normal_Building:
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
                                    for building_var in self.game.village.normal_Building:
                                        if(self.game.map[y_coord][x_coord].name == building_var):
                                            temp = self.game.map[y_coord][x_coord]
                                            y_dist = y_coord - self.y
                                            x_dist = x_coord - self.x
                                            break
                                
                                if temp != None:
                                    break
                        
                        # Checking Column Normal Building

                        if(temp == None):
                            for y_coord in range(max(0,self.y-short_Dist),min(ROW-1,self.y+short_Dist)+1):
                                
                                # Left Column
                                if(self.x>=short_Dist):
                                    x_coord = self.x-short_Dist
                                    for building_var in self.game.village.normal_Building:
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
                                    for building_var in self.game.village.normal_Building:
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
                

                # Attack when reached the target
                if(self.game.map[self.y][self.x] == self.target):
                    self.attack(self.x,self.y)

                # Move towards the target
                else:
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

                    if move_x == 0 and move_y == 0 :
                        self.target = None
                        self.move()

                    elif self.game.air_map[self.y+move_y][self.x+move_x].name == "Empty":

                        self.game.air_board[self.y][self.x] = ' '
                        self.game.air_map[self.y][self.x] = empty(self.game,self.x,self.y)
                        self.x = self.x + move_x
                        self.y = self.y + move_y
                        self.x_dist = self.x_dist - move_x
                        self.y_dist = self.y_dist - move_y
                        self.game.air_board[self.y][self.x] = self.symbol
                        self.game.air_map[self.y][self.x] = self
                    
        

            elif(self.target.alive == False):
                self.target=None
                self.move()