from constants import COL,ROW,INFINITY
from colorama import Fore, Back, Style
from Build_buildings import cell,building,empty


class WizardTower(building):
    def __init__(self,game,x_start,y_start,target=1,damage=50,name="WizardTower",health=100,strength = 300,color=Fore.RED,symbol="Z",height=1,width=1):
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
                            if(self.game.air_map[y_coord][x_coord].name == "Balloon"):
                                temp = self.game.air_map[y_coord][x_coord]
                                break
                    if(self.y_start+(manhattan_Dist-(abs(self.x_start-x_coord)))<ROW):
                        y_coord = self.y_start+(manhattan_Dist-(abs(self.x_start-x_coord)))
                        
                        if y_coord >=0 and y_coord < ROW:
                            if(manhattan_Dist-(abs(self.x_start-x_coord))!=0):
                                if(self.game.air_map[y_coord][x_coord].name == "Balloon"):
                                    temp = self.game.air_map[y_coord][x_coord]
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
                x_target = self.target.x
                y_target = self.target.y
                for x_1 in range(max(0,x_target-1),min((COL-2),x_target+1)+1):
                    for y_1 in range(max(0,y_target-1),min((ROW-1),y_target+1)+1):
                        if(self.game.air_map[y_1][x_1].name == "Balloon"):
                            self.game.air_map[y_1][x_1].strength -= self.damage
                            self.game.air_map[y_1][x_1].health = max(0,((self.game.air_map[y_1][x_1].strength/self.game.air_map[y_1][x_1].strength_Max)*100))
                            if self.game.air_map[y_1][x_1].strength <= 0 :
                                self.game.air_map[y_1][x_1].death()
                                self.target = None
            else:
                self.target = None
                self.active = False

    def destroy_building(self):
        self.active = False
        super().destroy_building()    