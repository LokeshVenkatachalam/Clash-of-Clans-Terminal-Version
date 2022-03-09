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
            if(self.x-1>0):
                self.game.map[self.y][self.x-1].attack(self.game,self.hitpoint)
        elif(self.last_Move == 'R'):
            if(self.x+1<COL-1):
                self.game.map[self.y][self.x+1].attack(self.game,self.hitpoint)
        elif(self.last_Move == 'U'):
            if(self.y-1>0):
                self.game.map[self.y-1][self.x].attack(self.game,self.hitpoint)
        elif(self.last_Move == 'D'):
            if(self.y+1<ROW-1):
                self.game.map[self.y+1][self.x].attack(self.game,self.hitpoint)