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
        self.color = color
        self.symbol = symbol
        self.height = height
        self.width = width
        self.x2 = self.x_start + width 
        self.y2 = self.y_start + height 
    
    def display(self):
        
        for x_coord in range(self.x_start,self.x2):
            for y_coord in range(self.y_start,self.y2):
                self.game.board[y_coord][x_coord] =self.color+self.symbol
                self.game.map[y_coord][x_coord] = self
    
    def attack(self,hitpoint):
        self.health -= hitpoint
        if(self.health <= 0):
            self.destroy_building(self)
    
    def destroy_building(self):

        for x_coord in range(self.x_start,self.x2):
            for y_coord in range(self.y_start,self.y2):
                self.game.board[y_coord][x_coord] = ' '
                self.game.map[y_coord][x_coord] = empty(self.game,x_coord,y_coord)
                

class town_Hall(building):

    def __init__(self,game,x_start,y_start,name="Town Hall",health=100,strength = 250,color=Fore.GREEN,symbol="T",height=3,width=4):
        super().__init__(game,name,health,strength,color,symbol,x_start,y_start,height,width)

    
            
    
        
class hut(building):

    def __init__(self,game,x_start,y_start,name="Hut",health=100,strength = 150,color=Fore.BLUE,symbol="H",height=2,width=2):
        super().__init__(game,name,health,strength,color,symbol,x_start,y_start,height,width)


class cannon(building):

    def __init__(self,game,x_start,y_start,target=1,damage=1,name="Cannon",health=100,strength = 100,color=Fore.RED,symbol="C",height=2,width=2):
        super().__init__(game,name,health,strength,color,symbol,x_start,y_start,height,width)
        self.damage =  damage
        self.target = target
        self.active = True

    def destroy_building(self):
        self.active = False
        super().destroy_building()

class wall(building):
    def __init__(self,game,x_start,y_start,name="Wall",health=100,strength = 50,color=Fore.YELLOW,symbol="W",height=1,width=1):
        super().__init__(game,name,health,strength,color,symbol,x_start,y_start,height,width)

class empty(cell):
    def __init__(self,game,x_start,y_start,name="Empty"):
        super().__init__(game,name,x_start,y_start)
    