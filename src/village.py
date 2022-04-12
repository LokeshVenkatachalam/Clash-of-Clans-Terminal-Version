from colorama import Fore, Back, Style
from Build_buildings import empty
from Build_Town_Hall import town_Hall
from Build_Hut import hut
from Build_Cannon import cannon
from Build_WizardTower import WizardTower
from Build_Wall import wall
class village:
    def __init__(self,game):
        self.existing_Building =[town_Hall(game,18,10),
                                hut(game,1,1),
                                hut(game,37,1),
                                hut(game,1,17),
                                hut(game,37,17),
                                hut(game,8,9),
                                hut(game,30,11),
                                hut(game,23,10),
                                hut(game,19,7),
                                cannon(game,23,7),
                                cannon(game,23,14),
                                WizardTower(game,16,7),
                                WizardTower(game,24,15),
                                wall(game,4,0),wall(game,4,1),wall(game,4,2),wall(game,4,3),wall(game,4,4),
                                wall(game,0,4),wall(game,1,4),wall(game,2,4),wall(game,3,4),
                                wall(game,35,0),wall(game,35,1),wall(game,35,2),wall(game,35,3),wall(game,35,4),
                                wall(game,36,4),wall(game,37,4),wall(game,38,4),wall(game,39,4),
                                wall(game,35,15),wall(game,35,16),wall(game,35,17),wall(game,35,18),wall(game,35,19),
                                wall(game,36,15),wall(game,37,15),wall(game,38,15),wall(game,39,15),
                                wall(game,4,15),wall(game,4,16),wall(game,4,17),wall(game,4,18),wall(game,4,19),
                                wall(game,0,15),wall(game,1,15),wall(game,2,15),wall(game,3,15),
                                wall(game,13,5),wall(game,14,5),wall(game,15,5),wall(game,16,5),wall(game,17,5),wall(game,18,5),wall(game,19,5),wall(game,20,5),wall(game,21,5),wall(game,22,5),wall(game,23,5),wall(game,24,5),wall(game,25,5),wall(game,26,5),
                                wall(game,13,17),wall(game,14,17),wall(game,15,17),wall(game,16,17),wall(game,17,17),wall(game,18,17),wall(game,19,17),wall(game,20,17),wall(game,21,17),wall(game,22,17),wall(game,23,17),wall(game,24,17),wall(game,25,17),wall(game,26,17),
                                wall(game,13,6),wall(game,13,7),wall(game,13,8),wall(game,13,9),wall(game,13,10),wall(game,13,11),wall(game,13,12),wall(game,13,13),wall(game,13,14),wall(game,13,15),wall(game,13,16),
                                wall(game,26,6),wall(game,26,7),wall(game,26,8),wall(game,26,9),wall(game,26,10),wall(game,26,11),wall(game,26,12),wall(game,26,13),wall(game,26,14),wall(game,26,15),wall(game,26,16),
                                wall(game,16,10),wall(game,16,11),wall(game,16,12),wall(game,16,13),wall(game,16,14),
                                wall(game,17,14),wall(game,18,14),wall(game,19,14),wall(game,20,14),wall(game,21,14),
                                wall(game,36,6),wall(game,36,7),wall(game,36,8),wall(game,36,9),wall(game,36,10),wall(game,36,11),wall(game,36,12),wall(game,36,13),wall(game,36,14),
                                wall(game,3,6),wall(game,3,7),wall(game,3,8),wall(game,3,9),wall(game,3,10),wall(game,3,11),wall(game,3,12),wall(game,3,13),wall(game,3,14),
                                wall(game,11,6),wall(game,11,7),wall(game,11,8),wall(game,11,9),wall(game,11,10),wall(game,11,11),wall(game,11,12),wall(game,11,13),wall(game,11,14),
                                wall(game,28,6),wall(game,28,7),wall(game,28,8),wall(game,28,9),wall(game,28,10),wall(game,28,11),wall(game,28,12),wall(game,28,13),wall(game,28,14),
                                wall(game,4,14),wall(game,5,14),wall(game,6,14),wall(game,7,14),wall(game,8,14),wall(game,9,14),wall(game,10,14),
                                wall(game,4,6),wall(game,5,6),wall(game,6,6),wall(game,7,6),wall(game,8,6),wall(game,9,6),wall(game,10,6),
                                wall(game,29,14),wall(game,30,14),wall(game,31,14),wall(game,32,14),wall(game,33,14),wall(game,34,14),wall(game,35,14),
                                wall(game,29,6),wall(game,30,6),wall(game,31,6),wall(game,32,6),wall(game,33,6),wall(game,34,6),wall(game,35,6),
                                
                                # LEVEL 2 addition
                                # cannon(game,8,12),
                                # WizardTower(game,30,8),
                                # hut(game,33,8),
                                # hut(game,5,11),

                                # LEVEL 3 addition
                                # hut(game,5,8),
                                # hut(game,33,11),
                                # WizardTower(game,8,19),wall(game,7,19),wall(game,9,19),wall(game,7,18),wall(game,8,18),wall(game,9,18),
                                # cannon(game,31,19),wall(game,30,19),wall(game,32,19),wall(game,30,18),wall(game,31,18),wall(game,32,18),
                                
                            ]
        
        self.attacker_King = []
        self.attacker_Queen = []
        self.attacker_Barbarian = []
        self.attacker_Archer = []
        self.attacker_Balloon = []

        self.troop = ["Archer","King","Barbarian","Queen","Balloon"]
        self.ground_Troops = ["Archer","King","Barbarian","Queen"]
        self.aerial_Troops = ["Balloon"]
        self.defensive_Building = ["Cannon","WizardTower"]
        self.normal_Building = ["Town Hall","Hut"]
        self.buildings = ["Cannon","WizardTower","Town Hall","Hut"]
        self.build = ["Cannon","WizardTower","Town Hall","Hut","Wall"]
    
