from colorama import Fore, Back, Style
from Build_buildings import cell,building

class wall(building):

    def __init__(self,game,x_start,y_start,name="Wall",health=100,strength = 100,color=Fore.YELLOW,symbol="W",height=1,width=1):
        super().__init__(game,name,health,strength,color,symbol,x_start,y_start,height,width)
