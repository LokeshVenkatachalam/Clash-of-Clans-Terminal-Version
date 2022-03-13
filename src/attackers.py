from constants import COL,ROW
from buildings import empty
from colorama import Fore, Back, Style
class attackers:
    def __init__(self,name,game,X_coord, Y_coord,symbol, hitpoint, speed,color):
        self.name = name
        self.game = game
        self.hitpoint = hitpoint
        self.speed = speed
        self.symbol = symbol
        self.health = 100
        self.x = X_coord
        self.y = Y_coord
        self.color = color
        self.game.board[self.y][self.x] = self.symbol
        self.game.map[self.y][self.x] = self
        self.alive = True

    def death(self):
        self.alive = False
        self.game.board[self.y][self.x] = ' '
        self.game.map[self.y][self.x] = empty(self.game,self.x,self.y)
    

    def display(self):
        if(self.alive == True):
            self.game.board[self.y][self.x] = self.color+Style.BRIGHT + self.symbol 
class king(attackers):
    def __init__(self,game,X_coord,Y_coord,name="KING",symbol='K',hitpoint= 80,speed= 1,color=Fore.MAGENTA):
        super().__init__(name,game,X_coord, Y_coord, symbol, hitpoint, speed,color)
        self.strength = 800
        self.strength_Max = 800 
        self.move_direction = ''
        
    def move(self):
        if (self.move_direction == 'D'):
            self.move_down()
        elif (self.move_direction == 'U'):
            self.move_up()
        elif (self.move_direction == 'L'):
            self.move_left()
        elif (self.move_direction == 'R'):
            self.move_right()


    def move_left(self):
        if(self.x > 0):
            if(self.game.board[self.y][self.x-1]==' '):
                self.game.board[self.y][self.x] = ' '
                self.game.board[self.y][self.x-1] = self.symbol
                self.game.map[self.y][self.x] = empty(self.game,self.x,self.y)
                self.x -= 1
                self.game.board[self.y][self.x] = self.symbol
                self.game.map[self.y][self.x] = self
    
    def move_right(self):
        if(self.x < COL - 2):
            if(self.game.board[self.y][self.x+1]==' '):
                self.game.board[self.y][self.x] = ' '
                self.game.board[self.y][self.x+1] = self.symbol
                self.game.map[self.y][self.x] = empty(self.game,self.x,self.y)
                self.x += 1
                self.game.board[self.y][self.x] = self.symbol
                self.game.map[self.y][self.x] = self

    def move_up(self):
        if(self.y > 0):
            if(self.game.board[self.y-1][self.x]==' '):
                self.game.board[self.y][self.x] = ' '
                self.game.map[self.y][self.x] = empty(self.game,self.x,self.y)
                self.y -= 1
                self.game.board[self.y][self.x] = self.symbol
                self.game.map[self.y][self.x] = self

    def move_down(self):
        if(self.y < ROW - 1):
            if(self.game.board[self.y+1][self.x]==' '):
                self.game.board[self.y][self.x] = ' '
                self.game.map[self.y][self.x] = empty(self.game,self.x,self.y)
                self.y += 1
                self.game.board[self.y][self.x] = self.symbol
                self.game.map[self.y][self.x] = self

    def attack(self):
        for manhattan_Dist in range(1,4):
            for x_coord in range(max(0,self.x-manhattan_Dist),min(29,self.x+manhattan_Dist+1)):
                if(self.y-(manhattan_Dist-(abs(self.x-x_coord)))>=0):
                    y_coord = self.y-(manhattan_Dist-(abs(self.x-x_coord)))
                    #print(x_coord,y_coord,self.y_start)
                    if((self.game.map[y_coord][x_coord].name == "Wall") or (self.game.map[y_coord][x_coord].name == "Hut") or (self.game.map[y_coord][x_coord].name == "Town_Hall") or (self.game.map[y_coord][x_coord].name == "Cannon")):
                        self.game.map[y_coord][x_coord].get_attack(self.hitpoint)
                if((manhattan_Dist-(abs(self.x-x_coord)))>0):
                    if(self.y+(manhattan_Dist-(abs(self.x-x_coord)))<=19):
                        y_coord = self.y+(manhattan_Dist-(abs(self.x-x_coord)))
                        #print(x_coord,y_coord)
                        if((self.game.map[y_coord][x_coord].name == "Wall") or (self.game.map[y_coord][x_coord].name == "Hut") or (self.game.map[y_coord][x_coord].name == "Town_Hall") or (self.game.map[y_coord][x_coord].name == "Cannon")):
                            self.game.map[y_coord][x_coord].get_attack(self.hitpoint)
#
        #if(self.Move == 'L'):
        #    if(self.x-1>=0):
        #        if(self.game.map[self.y][self.x-1].name != "Barbarian"):   
        #            self.game.map[self.y][self.x-1].get_attack(self.hitpoint)
        #elif(self.last_Move == 'R'):
        #    if(self.x+1<COL-1):
        #        if(self.game.map[self.y][self.x+1].name != "Barbarian"):   
        #            self.game.map[self.y][self.x+1].get_attack(self.hitpoint)
        #elif(self.last_Move == 'U'):
        #    if(self.y-1>=0):
        #        if(self.game.map[self.y-1][self.x].name != "Barbarian"):   
        #            self.game.map[self.y-1][self.x].get_attack(self.hitpoint)
        #elif(self.last_Move == 'D'):
        #    if(self.y+1<=ROW-1):
        #        if(self.game.map[self.y+1][self.x].name != "Barbarian"):   
        #            self.game.map[self.y+1][self.x].get_attack(self.hitpoint)
#

class barbarian(attackers):
    def __init__(self,game,X_coord,Y_coord,name="Barbarian",symbol='B',hitpoint= 25,speed= 1,color=Fore.BLUE ):
        super().__init__(name,game,X_coord, Y_coord, symbol, hitpoint, speed,color)
        self.strength = 350
        self.strength_Max = 350 
        self.target = None
        self.move_x = 0
        self.move_y = 0
        

    def attack(self,X_coord,Y_coord):
        self.game.map[Y_coord][X_coord].get_attack(self.hitpoint)

    def display(self):
        if(self.alive == True):
            if(self.health>40):
                self.color = Fore.BLUE + Style.DIM
            elif(self.health>0):
                self.color = Fore.LIGHTBLUE_EX + Style.BRIGHT
            self.game.board[self.y][self.x] = self.color+self.symbol

    def move(self):
        if(self.alive== True):
            if(self.target==None):
                temp = None
                for short_Dist in range(1,max(max(self.x,29-self.x),max(self.y,19-self.y))):
                    for x_coord in range(max(0,self.x-short_Dist),min(29,self.x+short_Dist)+1):
                        if(self.y>=short_Dist):
                            y_coord = self.y-short_Dist
                            if((self.game.map[y_coord][x_coord].name == "Hut") or (self.game.map[y_coord][x_coord].name == "Town_Hall") or (self.game.map[y_coord][x_coord].name == "Cannon")):
                                temp = self.game.map[y_coord][x_coord]
                                break
                        if(self.y<=19-short_Dist):
                            y_coord = self.y+short_Dist
                            if((self.game.map[y_coord][x_coord].name == "Hut") or (self.game.map[y_coord][x_coord].name == "Town_Hall") or (self.game.map[y_coord][x_coord].name == "Cannon")):
                                temp = self.game.map[y_coord][x_coord]
                                break
                    if(temp == None):
                        for y_coord in range(max(0,self.y-short_Dist),min(19,self.y+short_Dist)+1):
                            if(self.x>=short_Dist):
                                x_coord = self.x-short_Dist
                                if((self.game.map[y_coord][x_coord].name == "Hut") or (self.game.map[y_coord][x_coord].name == "Town Hall") or (self.game.map[y_coord][x_coord].name == "Cannon")):
                                    temp = self.game.map[y_coord][x_coord]
                                    break
                            if(self.x<=29-short_Dist):
                                x_coord = self.x+short_Dist
                                if((self.game.map[y_coord][x_coord].name == "Hut") or (self.game.map[y_coord][x_coord].name == "Town Hall") or (self.game.map[y_coord][x_coord].name == "Cannon")):
                                    temp = self.game.map[y_coord][x_coord]
                                    break
                    if(temp != None):
                        break
                if(temp != None):
                    self.target = temp
                    #print(self.target.x_start,self.target.y_start,self.target.name)
                    self.move()
            elif(self.target.alive == True):
                Move = None
                best_Move = 29
                #print(self.target.name,self.target.health)      
                for x_Dir in {-1,0,1}:
                    for y_Dir in {-1,0,1}:
                        if (x_Dir != 0 or y_Dir !=0):
                            min_x = 29
                            min_y = 19
                            if(self.x+x_Dir>=0 and self.x+x_Dir<=29 and self.y+y_Dir>=0 and self.y+y_Dir<=19):
                                for x_final in range(self.target.x_start,self.target.x2):
                                    for y_final in range(self.target.y_start,self.target.y2):
                                        if (max(abs(x_final-(self.x+x_Dir)),abs(y_final-(self.y+y_Dir)))<max(min_x,min_y)):
                                            min_x = abs(x_final-(self.x+x_Dir))
                                            min_y = abs(y_final-(self.y+y_Dir))
                                #print(self.x+x_Dir,self.y+y_Dir)
                                if(Move == None):
                                    if((self.game.map[self.y+y_Dir][self.x+x_Dir].symbol == ' ') or (self.game.map[self.y+y_Dir][self.x+x_Dir].symbol == 'W')):
                                        self.move_x = x_Dir
                                        self.move_y = y_Dir
                                        Move = "Move"
                                        best_Move = max(min_x,min_y)
                                    elif(self.game.map[self.y+y_Dir][self.x+x_Dir] == self.target):
                                        Move = "Attack"
                                        self.move_x = x_Dir
                                        self.move_y = y_Dir
                                        self.attack(self.x+x_Dir,self.y+y_Dir)
                                        break
                                elif(Move == "Move"):
                                    if((self.game.map[self.y+y_Dir][self.x+x_Dir].symbol == ' ') or (self.game.map[self.y+y_Dir][self.x+x_Dir].symbol == 'W')):
                                        if(max(min_x,min_y)<best_Move):
                                            self.move_x = x_Dir
                                            self.move_y = y_Dir
                                            Move = "Move"
                                            best_Move = max(min_x,min_y)
                                    elif(self.game.map[self.y+y_Dir][self.x+x_Dir] == self.target):
                                        Move = "Attack"
                                        self.move_x = x_Dir
                                        self.move_y = y_Dir
                                        self.attack(self.x+x_Dir,self.y+y_Dir)
                                        break
                                #print(Move,self.move_x,self.move_y)
                    if(Move == "Attack"):
                        #print(self.game.map[self.y+self.move_y][self.x+self.move_x].health)
                        break
                #print(Move,self.y,self.move_y,self.x,self.move_x)
                #print(self.game.board[self.y+self.move_y][self.x+self.move_x])
                #print(self.game.map[self.y+self.move_y][self.x+self.move_x].symbol)
                if(Move == "Move"):
                    if(self.game.map[self.y+self.move_y][self.x+self.move_x].symbol == 'W'):
                        self.attack(self.x+self.move_x,self.y+self.move_y)
                    elif(self.game.map[self.y+self.move_y][self.x+self.move_x].symbol == ' '):
                        self.game.board[self.y][self.x] = ' '
                        self.game.map[self.y][self.x] = empty(self.game,self.x,self.y)
                        self.x = self.x +self.move_x 
                        self.y = self.y +self.move_y
                        self.game.board[self.y][self.x] = self.symbol
                        self.game.map[self.y][self.x] = self
                #print(Move,self.move_y,self.move_x)
                self.move_x = 0
                self.move_y = 0
            elif(self.target.alive == False):
                self.target=None
                self.move()

        #if(self.target==None):
        #    temp = None
        #    for building in self.village.Buildings:
        #        if(building.name!="Wall"):
        #            if(building.barbarian_Attack_Status==None):
        #                if(temp == None):
        #                   temp = building
        #                elif(max(abs(temp.x_start-self.X_coord),abs(temp.y_start-self.Y_coord))>max(abs(building.x_start-self.X_coord),abs(building.y_start-self.Y_coord))):
        #                    temp = building
        #    self.target = temp
        #elif(self.target.alive==True):
        #    if(abs(self.target.x_start-self.X_coord)<abs(self.target.y_start-self.Y_coord)):
        #        Y_length = abs(self.target.y_start-self.Y_coord)
        #        X_length = abs(self.target.x_start-self.X_coord)