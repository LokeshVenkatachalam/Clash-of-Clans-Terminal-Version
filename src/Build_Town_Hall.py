from colorama import Fore, Back, Style
from Build_buildings import cell,building

class town_Hall(building):

    def __init__(self,game,x_start,y_start,name="Town Hall",health=100,strength = 700,color=Fore.GREEN,symbol="T",height=3,width=4):
        super().__init__(game,name,health,strength,color,symbol,x_start,y_start,height,width)
 