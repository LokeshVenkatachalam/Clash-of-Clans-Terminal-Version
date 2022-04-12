from constants import COL,ROW,INFINITY
from Build_buildings import empty
from village import village
from colorama import Fore, Back, Style

# Troop
class attackers:

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
        self.game.board[self.y][self.x] = self.symbol
        self.game.map[self.y][self.x] = self
        
    # Death of Troop
    def death(self):
        self.alive = False
        self.game.board[self.y][self.x] = ' '
        self.game.map[self.y][self.x] = empty(self.game,self.x,self.y)
    
    # Display
    def display(self):
        if(self.alive == True):
            self.game.board[self.y][self.x] = self.color+Style.BRIGHT + self.symbol

    # Move left
    def move_left(self):
        if(self.x > 0): # If not at left edge
            if(self.game.board[self.y][self.x-1]==' '): # If empty

                # Changing Current Position Value
                self.game.board[self.y][self.x] = ' '
                self.game.map[self.y][self.x] = empty(self.game,self.x,self.y)

                # Changing Position
                self.x -= 1

                # Changing New Position Value
                self.game.board[self.y][self.x] = self.symbol
                self.game.map[self.y][self.x] = self
    
    # Move right
    def move_right(self): 
        if(self.x < COL - 2): # If not at right edge
            if(self.game.board[self.y][self.x+1]==' '): # If empty

                # Changing Current Position Value
                self.game.board[self.y][self.x] = ' '
                self.game.map[self.y][self.x] = empty(self.game,self.x,self.y)

                # Changing Position
                self.x += 1

                # Changing New Position Value
                self.game.board[self.y][self.x] = self.symbol
                self.game.map[self.y][self.x] = self
    
    # Move up
    def move_up(self):
        if(self.y > 0): # If not at top edge
            if(self.game.board[self.y-1][self.x]==' '): # If empty

                # Changing Current Position Value
                self.game.board[self.y][self.x] = ' '
                self.game.map[self.y][self.x] = empty(self.game,self.x,self.y)

                # Changing Position
                self.y -= 1

                # Changing New Position Value
                self.game.board[self.y][self.x] = self.symbol
                self.game.map[self.y][self.x] = self

    # Move down
    def move_down(self):
        if(self.y < ROW - 1): # If not at bottom edge
            if(self.game.board[self.y+1][self.x]==' '):

                # Changing Current Position Value
                self.game.board[self.y][self.x] = ' '
                self.game.map[self.y][self.x] = empty(self.game,self.x,self.y)

                # Changing Position
                self.y += 1

                # Changing New Position Value
                self.game.board[self.y][self.x] = self.symbol
                self.game.map[self.y][self.x] = self

