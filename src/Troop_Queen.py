from constants import COL,ROW,INFINITY
from Build_buildings import empty
from village import village
from colorama import Fore, Back, Style
from Troop_attackers import attackers

# Queen
class Queen(attackers):

    # Intialize
    def __init__(self,game,X_coord,Y_coord,name="Queen",symbol='Q',hitpoint= 60,speed= 1,color=Fore.MAGENTA):
        super().__init__(name,game,X_coord, Y_coord, symbol, hitpoint, speed,color)
        self.strength = 800
        self.strength_Max = 800 
        self.move_direction = ''
        self.attack_direction = ''
        self.attack_Center_X = 0
        self.attack_Center_Y = 0

    # Move direction
    def move(self):
        if (self.move_direction == 'D'):
            self.move_down()
        elif (self.move_direction == 'U'):
            self.move_up()
        elif (self.move_direction == 'L'):
            self.move_left()
        elif (self.move_direction == 'R'):
            self.move_right()


    # Attack
    # 
    def attack(self,dist=8,AoE=3):

        Attack = False

        # Choose the center of attack
        if (self.attack_direction == 'D'):
            self.attack_Center_X = self.x
            self.attack_Center_Y = self.y + dist
            Attack = True
        elif (self.attack_direction == 'U'):
            self.attack_Center_X = self.x
            self.attack_Center_Y = self.y - dist
            Attack = True
        elif (self.attack_direction == 'L'):
            self.attack_Center_X = self.x - dist
            self.attack_Center_Y = self.y
            Attack = True
        elif (self.attack_direction == 'R'):
            self.attack_Center_X = self.x + dist
            self.attack_Center_Y = self.y
            Attack = True

        
        

        if Attack == True:
            # Attack
            if self.attack_Center_X>=0 and self.attack_Center_Y >= 0 and self.attack_Center_X<COL -1 and self.attack_Center_Y <ROW:
                for Building_var in self.game.village.buildings:
                    if(self.game.map[self.attack_Center_Y][self.attack_Center_X].name == Building_var):
                        self.game.map[self.attack_Center_Y][self.attack_Center_X].get_attack(self.hitpoint)

            for tile_dist in range(1,AoE): #Tile rane 1 to 3

                # Attack Row
                for x_coord in range(max(0,self.attack_Center_X-tile_dist),min((COL-2),self.attack_Center_X+tile_dist)+1):

                    # Attack Top Row [with given Tile Distance]
                    y_coord = self.attack_Center_Y - tile_dist
                    if y_coord >= 0  and y_coord < ROW :
                        for Building_var in self.game.village.build:
                            if(self.game.map[y_coord][x_coord].name == Building_var):
                                self.game.map[y_coord][x_coord].get_attack(self.hitpoint)
                    
                    # Attack Bottom Row [with given Tile Distance]
                    y_coord = self.attack_Center_Y + tile_dist
                    if y_coord >= 0  and y_coord < ROW :
                        for Building_var in self.game.village.build:
                            if(self.game.map[y_coord][x_coord].name == Building_var):
                                self.game.map[y_coord][x_coord].get_attack(self.hitpoint)
                
                # Attack Column
                for y_coord in range(max(0,self.attack_Center_Y-tile_dist+1),min((ROW-1),self.attack_Center_Y+tile_dist-1)+1):

                    # Attack Left Column [with given Tile Distance]
                    x_coord = self.attack_Center_X - tile_dist
                    if x_coord >= 0 and x_coord < COL - 1:
                        for Building_var in self.game.village.build:
                            if(self.game.map[y_coord][x_coord].name == Building_var):
                                self.game.map[y_coord][x_coord].get_attack(self.hitpoint)
                    
                    # Attack Right Column [with given Tile Distance]
                    x_coord = self.attack_Center_X + tile_dist
                    if x_coord >= 0 and x_coord < COL-1 :
                        for Building_var in self.game.village.build:
                            if(self.game.map[y_coord][x_coord].name == Building_var):
                                self.game.map[y_coord][x_coord].get_attack(self.hitpoint)
