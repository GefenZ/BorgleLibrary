from enum import IntEnum

class Constants:
    # hp levels:
    SIDE_TOWER_HP = [10, 14, 18, 22, 26, 30, 34, 38, 42, 46]
    MIDDLE_TOWER_HP = [13, 22, 31, 40, 49, 58, 67, 76, 85, 94]

    # income levels:
    SIDE_TOWER_INCOME = [2, 3, 4, 5, 7, 9, 11, 14, 17, 20]
    MIDDLE_TOWER_INCOME = [4, 5, 6, 8, 10, 13, 16, 20, 24, 28]

class Type(IntEnum):
    REGISTER = 0
    GET_USERS = 1
    SUBMIT = 2
    FIGHT = 3

class TowerType(IntEnum):
    SIDE = 0
    MIDDLE = 1

class BorgleException(Exception):
    pass

class State:

    pass

class Game:
    def calcTurn(state: State):
        print("this is an automatic response of turn calculating")

class Player:
    def __init__(self):
        self.level = 1
        self.towers = (Tower.generate(TowerType.SIDE), Tower.generate(TowerType.MIDDLE), Tower.generate(TowerType.SIDE))

class Tower:
    def __init__(self, hp, income):
        self.hp = hp
        self.income = income
    
    def upgrade(self):
        pass

    def generate(tower_type: TowerType):
        if tower_type == TowerType.SIDE:
            return Tower(Constants.SIDE_TOWER_HP[0], Constants.SIDE_TOWER_INCOME[0])
        elif tower_type == TowerType.MIDDLE:
            return Tower(Constants.MIDDLE_TOWER_HP[0], Constants.MIDDLE_TOWER_INCOME[0]) 
        else:
            raise BorgleException("Unknown tower type")




