from colorama import Fore, Back, Style

class cell:
    def __init__(self,game,name,x_coord,y_coord):
        self.game = game
        self.name = name
        self.x_start = x_coord
        self.y_start = y_coord

class building(cell):
    
    def __init__(self,game,name,health,strength,color,symbol,x_start,y_start,height,width):
        super().__init__(game,name,x_start,y_start)
        self.health = health
        self.strength = strength
        self.strength_max = strength
        self.color = color
        self.symbol = symbol
        self.height = height
        self.width = width
        self.x2 = self.x_start + width 
        self.y2 = self.y_start + height
        self.alive = True 
    
    def display(self):
        if(self.alive == True):
            for x_coord in range(self.x_start,self.x2):
                for y_coord in range(self.y_start,self.y2):
                    self.game.map[y_coord][x_coord] = self
                    if(self.health>50):
                        self.color = Fore.GREEN
                    elif(self.health>20):
                        self.color = Fore.YELLOW
                    elif(self.health>0):
                        self.color = Fore.RED
                    self.game.board[y_coord][x_coord] = self.color + Style.DIM+ self.symbol
        
    
    def get_attack(self,hitpoint):
        self.strength-= hitpoint
        self.health = (self.strength/self.strength_max)*100
        if(self.strength <= 0):
            self.destroy_building()
    
    def destroy_building(self):
        for x_coord in range(self.x_start,self.x2):
            for y_coord in range(self.y_start,self.y2):
                self.game.board[y_coord][x_coord] = ' '
                self.game.map[y_coord][x_coord] = empty(self.game,x_coord,y_coord)
        self.alive = False
                
class empty(cell):
    def __init__(self,game,x_start,y_start,name="Empty",symbol = ' '):
        super().__init__(game,name,x_start,y_start)
        self.symbol = symbol
    def attack(self,hitpoint):
        pass

