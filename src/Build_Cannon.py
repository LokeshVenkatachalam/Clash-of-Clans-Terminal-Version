from constants import COL,ROW,INFINITY
from colorama import Fore, Back, Style
from Build_buildings import cell,building


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
            temp = None
            for manhattan_Dist in range(1,7):
                for x_coord in range(max(0,self.x_start-manhattan_Dist),min(COL-2,self.x2+manhattan_Dist)+1):
                    if(self.y_start-(manhattan_Dist-(abs(self.x_start-x_coord)))>=0):
                        y_coord = self.y_start-(manhattan_Dist-(abs(self.x_start-x_coord)))

                        if y_coord >=0 and y_coord < ROW:
                            if((self.game.map[y_coord][x_coord].name == "Barbarian") or (self.game.map[y_coord][x_coord].name == "King") or (self.game.map[y_coord][x_coord].name == "Queen") or (self.game.map[y_coord][x_coord].name == "Archer")):
                                temp = self.game.map[y_coord][x_coord]
                                break

                    if(self.y_start+(manhattan_Dist-(abs(self.x_start-x_coord)))<ROW):
                        y_coord = self.y_start+(manhattan_Dist-(abs(self.x_start-x_coord)))
                        if y_coord >=0 and y_coord < ROW:
                            if(manhattan_Dist-(abs(self.x_start-x_coord))!=0):
                                if((self.game.map[y_coord][x_coord].name == "Barbarian") or (self.game.map[y_coord][x_coord].name == "King") or (self.game.map[y_coord][x_coord].name == "Queen") or (self.game.map[y_coord][x_coord].name == "Archer")):
                                    temp = self.game.map[y_coord][x_coord]
                                    break   
                if(temp != None):
                    break
            if(temp != None):
                self.target = temp
                self.attack()
                self.active = True
        else:
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