from colorama import Fore, Back, Style
from Build_buildings import cell,building

class hut(building):

    def __init__(self,game,x_start,y_start,name="Hut",health=100,strength = 250,color=Fore.BLUE,symbol="H",height=2,width=2):
        super().__init__(game,name,health,strength,color,symbol,x_start,y_start,height,width)
