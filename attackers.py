from sqlalchemy import null
from constants import COL,ROW

class attackers:
    def __init__(self,name,game,X_coord, Y_coord,symbol, hitpoint, speed):
        self.name = name
        self.game = game
        self.hitpoint = hitpoint
        self.speed = speed
        self.symbol = symbol
        self.health = 100
        self.x = X_coord
        self.y = Y_coord
        self.alive = True


class king(attackers):
    def __init__(self,game,X_coord,Y_coord,name="KING",symbol='K',hitpoint= 50,speed= 1 ):
        super().__init__(name,game,X_coord, Y_coord, symbol, hitpoint, speed)
        self.Strength = 500
        self.last_Move = ""
        self.game.board[self.y][self.x] = self.symbol


    def move_left(self):
        self.last_Move = 'L'
        if(self.x > 0):
            if(self.game.board[self.y][self.x-1]==' '):
                self.game.board[self.y][self.x] = ' '
                self.game.board[self.y][self.x-1] = self.symbol
                self.x -= 1
    
    def move_right(self):
        self.last_Move = 'R'
        if(self.x < COL - 2):
            if(self.game.board[self.y][self.x+1]==' '):
                self.game.board[self.y][self.x] = ' '
                self.game.board[self.y][self.x+1] = self.symbol
                self.x += 1

    def move_up(self):
        self.last_Move = 'U'
        if(self.y > 0):
            if(self.game.board[self.y-1][self.x]==' '):
                self.game.board[self.y][self.x] = ' '
                self.game.board[self.y-1][self.x] = self.symbol
                self.y -= 1

    def move_down(self):
        self.last_Move = 'D'
        if(self.y < ROW - 1):
            if(self.game.board[self.y+1][self.x]==' '):
                self.game.board[self.y][self.x] = ' '
                self.game.board[self.y+1][self.x] = self.symbol
                self.y += 1

    def attack(self):
        if(self.last_Move == 'L'):
            if(self.x-1>=0):
                self.game.map[self.y][self.x-1].attack(self.hitpoint)
        elif(self.last_Move == 'R'):
            if(self.x+1<COL-1):
                self.game.map[self.y][self.x+1].attack(self.hitpoint)
        elif(self.last_Move == 'U'):
            if(self.y-1>=0):
                self.game.map[self.y-1][self.x].attack(self.hitpoint)
        elif(self.last_Move == 'D'):
            if(self.y+1<=ROW-1):
                self.game.map[self.y+1][self.x].attack(self.hitpoint)

###
class barbarian(attackers):
    def __init__(self,game,X_coord,Y_coord,name="Barbarian",symbol='B',hitpoint= 20,speed= 1 ):
        super().__init__(name,game,X_coord, Y_coord, symbol, hitpoint, speed)
        self.Strength = 100
        self.target = None
        self.game.board[self.y][self.x] = self.symbol
        

    def attack(self,X_coord,Y_coord):
        self.game.map[Y_coord][X_coord].attack(self.hitpoint)

    def move(self):
        if(self.target==None):
            temp = None
            for building in self.village.Buildings:
                if(building.name!="Wall"):
                    if(building.barbarian_Attack_Status==None):
                        if(temp == None):
                            temp = building
                        elif(max(abs(temp.x_start-self.X_coord),abs(temp.y_start-self.Y_coord))>max(abs(building.x_start-self.X_coord),abs(building.y_start-self.Y_coord))):
                            temp = building
            self.target = temp
        elif(self.target.alive==True):
            if(abs(self.target.x_start-self.X_coord)<abs(self.target.y_start-self.Y_coord)):
                Y_length = abs(self.target.y_start-self.Y_coord)
                X_length = abs(self.target.x_start-self.X_coord)