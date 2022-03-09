from colorama import Fore, Back, Style
from buildings import hut, town_Hall, cannon, wall

class village:
    def __init__(self,game):
        self.existing_Building =[town_Hall(game,12,10),
                                hut(game,1,1),
                                hut(game,27,1),
                                hut(game,1,17),
                                hut(game,27,17),
                                hut(game,17,10),
                                hut(game,13,7),
                                cannon(game,9,7),
                                cannon(game,17,7),
                                cannon(game,17,14),
                                wall(game,4,0),wall(game,4,1),wall(game,4,2),wall(game,4,3),wall(game,4,4),
                                wall(game,0,4),wall(game,1,4),wall(game,2,4),wall(game,3,4),
                                wall(game,25,0),wall(game,25,1),wall(game,25,2),wall(game,25,3),wall(game,25,4),
                                wall(game,26,4),wall(game,27,4),wall(game,28,4),wall(game,29,4),
                                wall(game,25,15),wall(game,25,16),wall(game,25,17),wall(game,25,18),wall(game,25,19),
                                wall(game,26,15),wall(game,27,15),wall(game,28,15),wall(game,29,15),
                                wall(game,4,15),wall(game,4,16),wall(game,4,17),wall(game,4,18),wall(game,4,19),
                                wall(game,0,15),wall(game,1,15),wall(game,2,15),wall(game,3,15),
                                wall(game,7,5),wall(game,8,5),wall(game,9,5),wall(game,10,5),wall(game,11,5),wall(game,12,5),wall(game,13,5),wall(game,14,5),wall(game,15,5),wall(game,16,5),wall(game,17,5),wall(game,18,5),wall(game,19,5),wall(game,20,5),
                                wall(game,7,17),wall(game,8,17),wall(game,9,17),wall(game,10,17),wall(game,11,17),wall(game,12,17),wall(game,13,17),wall(game,14,17),wall(game,15,17),wall(game,16,17),wall(game,17,17),wall(game,18,17),wall(game,19,17),wall(game,20,17),
                                wall(game,7,6),wall(game,7,7),wall(game,7,8),wall(game,7,9),wall(game,7,10),wall(game,7,11),wall(game,7,12),wall(game,7,13),wall(game,7,14),wall(game,7,15),wall(game,7,16),
                                wall(game,20,6),wall(game,20,7),wall(game,20,8),wall(game,20,9),wall(game,20,10),wall(game,20,11),wall(game,20,12),wall(game,20,13),wall(game,20,14),wall(game,20,15),wall(game,20,16),
                                wall(game,10,10),wall(game,10,11),wall(game,10,12),wall(game,10,13),wall(game,10,14),
                                wall(game,11,14),wall(game,12,14),wall(game,13,14),wall(game,14,14),wall(game,15,14)]
        self.attacker_King = []
        self.attacker_Barbarian = []
