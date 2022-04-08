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
                

class town_Hall(building):

    def __init__(self,game,x_start,y_start,name="Town Hall",health=100,strength = 700,color=Fore.GREEN,symbol="T",height=3,width=4):
        super().__init__(game,name,health,strength,color,symbol,x_start,y_start,height,width)

    
            
    
        
class hut(building):

    def __init__(self,game,x_start,y_start,name="Hut",health=100,strength = 250,color=Fore.BLUE,symbol="H",height=2,width=2):
        super().__init__(game,name,health,strength,color,symbol,x_start,y_start,height,width)


class cannon(building):

    def __init__(self,game,x_start,y_start,target=1,damage=50,name="Cannon",health=100,strength = 300,color=Fore.RED,symbol="C",height=1,width=1):
        super().__init__(game,name,health,strength,color,symbol,x_start,y_start,height,width)
        self.damage =  damage
        self.target = None
        self.active = False

    def display(self):
        if(self.active == True):
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
                        self.game.board[y_coord][x_coord] = self.color + Style.BRIGHT + self.symbol
        else:
            super().display()


    def attack(self):
        
        if(self.target==None):
            self.active = False
            #print("None")
            temp = None
            for manhattan_Dist in range(1,7):
                for x_coord in range(max(0,self.x_start-manhattan_Dist),min(29,self.x2+manhattan_Dist)):
                    if(self.y_start-(manhattan_Dist-(abs(self.x_start-x_coord)))>=0):
                        y_coord = self.y_start-(manhattan_Dist-(abs(self.x_start-x_coord)))
                        #print(x_coord,y_coord,self.y_start)
                        if((self.game.map[y_coord][x_coord].name == "Barbarian") or (self.game.map[y_coord][x_coord].name == "KING")):
                            temp = self.game.map[y_coord][x_coord]
                            break
                    if(self.y_start+(manhattan_Dist-(abs(self.x_start-x_coord)))<=19):
                        y_coord = self.y_start+(manhattan_Dist-(abs(self.x_start-x_coord)))
                        #print(x_coord,y_coord)
                        if(manhattan_Dist-(abs(self.x_start-x_coord))!=0):
                            if((self.game.map[y_coord][x_coord].name == "Barbarian") or (self.game.map[y_coord][x_coord].name == "KING")):
                                temp = self.game.map[y_coord][x_coord]
                                break   
                if(temp != None):
                    break
            if(temp != None):
                self.target = temp
                self.attack()
                self.active = True
        else:
            #print(self.target.name)
            x_diff = abs(self.target.x-self.x_start)
            y_diff = abs(self.target.y-self.y_start)
            if(x_diff+y_diff < 6):
                self.target.strength -= self.damage
                self.target.health = max(0,((self.target.strength/self.target.strength_Max)*100))
                if(self.target.strength <= 0):
                    self.target.death()
                    self.target = None
            else:
                self.target = None
                self.active = False

    def destroy_building(self):
        self.active = False
        super().destroy_building()

class wall(building):

    def __init__(self,game,x_start,y_start,name="Wall",health=100,strength = 100,color=Fore.YELLOW,symbol="W",height=1,width=1):
        super().__init__(game,name,health,strength,color,symbol,x_start,y_start,height,width)

class empty(cell):
    def __init__(self,game,x_start,y_start,name="Empty",symbol = ' '):
        super().__init__(game,name,x_start,y_start)
        self.symbol = symbol
    def attack(self,hitpoint):
        pass