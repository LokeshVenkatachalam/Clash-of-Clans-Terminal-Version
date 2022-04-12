from constants import COL,ROW,INFINITY
from Build_buildings import empty
from village import village
from colorama import Fore, Back, Style
from Troop_attackers import attackers

# King
class King(attackers):

    # Intialize
    def __init__(self,game,X_coord,Y_coord,name="King",symbol='K',hitpoint= 80,speed= 1,color=Fore.MAGENTA):
        super().__init__(name,game,X_coord, Y_coord, symbol, hitpoint, speed,color)
        self.strength = 800
        self.strength_Max = 800 
        self.move_direction = ''

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


    # def move_left(self):
    #     if(self.x > 0):
    #         if(self.game.board[self.y][self.x-1]==' '):
    #             self.game.board[self.y][self.x] = ' '
    #             self.game.board[self.y][self.x-1] = self.symbol
    #             self.game.map[self.y][self.x] = empty(self.game,self.x,self.y)
    #             self.x -= 1
    #             self.game.board[self.y][self.x] = self.symbol
    #             self.game.map[self.y][self.x] = self
    
    # def move_right(self):
    #     if(self.x < COL - 2):
    #         if(self.game.board[self.y][self.x+1]==' '):
    #             self.game.board[self.y][self.x] = ' '
    #             self.game.board[self.y][self.x+1] = self.symbol
    #             self.game.map[self.y][self.x] = empty(self.game,self.x,self.y)
    #             self.x += 1
    #             self.game.board[self.y][self.x] = self.symbol
    #             self.game.map[self.y][self.x] = self

    # def move_up(self):
    #     if(self.y > 0):
    #         if(self.game.board[self.y-1][self.x]==' '):
    #             self.game.board[self.y][self.x] = ' '
    #             self.game.map[self.y][self.x] = empty(self.game,self.x,self.y)
    #             self.y -= 1
    #             self.game.board[self.y][self.x] = self.symbol
    #             self.game.map[self.y][self.x] = self

    # def move_down(self):
    #     if(self.y < ROW - 1):
    #         if(self.game.board[self.y+1][self.x]==' '):
    #             self.game.board[self.y][self.x] = ' '
    #             self.game.map[self.y][self.x] = empty(self.game,self.x,self.y)
    #             self.y += 1
    #             self.game.board[self.y][self.x] = self.symbol
    #             self.game.map[self.y][self.x] = self

    # Tile Attack
    def attack(self):

        for tile_dist in range(1,3): #Tile rane 1 to 3

            # Attack Row
            for x_coord in range(max(0,self.x-tile_dist),min(COL-2,self.x+tile_dist)+1):

                # Attack Top Row [with given Tile Distance]
                y_coord = self.y - tile_dist
                if y_coord >= 0 :
                    for Building_var in self.game.village.build:
                        if(self.game.map[y_coord][x_coord].name == Building_var):
                            self.game.map[y_coord][x_coord].get_attack(self.hitpoint)
                            
                
                # Attack Bottom Row [with given Tile Distance]
                y_coord = self.y + tile_dist
                if y_coord < ROW :
                    for Building_var in self.game.village.build:
                        if(self.game.map[y_coord][x_coord].name == Building_var):
                            self.game.map[y_coord][x_coord].get_attack(self.hitpoint)
            
            # Attack Column
            for y_coord in range(max(0,self.y-tile_dist+1),min(ROW-1,self.y+tile_dist-1)+1):

                # Attack Left Column [with given Tile Distance]
                x_coord = self.x - tile_dist
                if x_coord >= 0 :
                    for Building_var in self.game.village.build:
                        if(self.game.map[y_coord][x_coord].name == Building_var):
                            self.game.map[y_coord][x_coord].get_attack(self.hitpoint)
                
                # Attack Right Column [with given Tile Distance]
                x_coord = self.x + tile_dist
                if x_coord < COL - 1 :
                    for Building_var in self.game.village.build:
                        if(self.game.map[y_coord][x_coord].name == Building_var):
                            self.game.map[y_coord][x_coord].get_attack(self.hitpoint)

