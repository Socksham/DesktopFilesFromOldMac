from random import randint

class Player:
    def __init__(self, height, position, strength, weight, speed, shooting, name, injury_prone, defence, age):
        self.height = height
        self.position = position
        self.strength = strength
        self.weight = weight
        self.speed = speed
        self.shooting = shooting
        self.name = name
        self.injury_prone = injury_prone
        self.defence = defence
        self.age = age

    def change_height(self, num):
        self.height -= num
    
    def change_positions(self, pos):
        self.position = pos

    def change_strength(self, num):
        self.strength -= num
    
    def change_weight(self, num):
        self.weight -= num

    def change_speed(self, num):
        self.speed -= num

    def change_shooting(self, num):
        self.shooting -= num
    
    def change_injury_prone(self, num):
        self.injury_prone -= num

    def change_defence(self, num):
        self.defence -= num

    def take_shot(self):
        shot_percentage = randint(0, 100)
        if shot_percentage <= self.shooting:
            return True
        else:
            return False
    
    def steal_ball(self):
        defence_percentage = randint(0, 100)
        if defence_percentage <= self.defence:
            return True
        else:
            return False

    def block_shot(self):
        defence_percentage = randint(0, 100)
        if defence_percentage <= self.defence/2:
            return True
        else:
            return False

    def injury(self, num):
        what_attribute = randint(1, 5)
        if what_attribute == 1:
            self.strength -= num
        elif what_attribute == 2:
            self.speed -= num
        elif what_attribute == 3:
            self.shooting -= num
        elif what_attribute == 4:
            self.defence -= num
        self.injury_prone += num
        
        if self.injury_prone >= 90:
            return True
        else:
            return False