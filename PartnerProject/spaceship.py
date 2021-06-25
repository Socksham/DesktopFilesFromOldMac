class spaceship:
    def __init__(self, speed, weapon_power, health, shields, accuracy, name):
        self.speed = speed
        self.weapon_power = weapon_power
        self.health = health
        self.shields = shields
        self.name = name
        self.accuracy = accuracy
    
    def get_speed(self):
        return self.speed
    def get_weapon_power(self):
        return self.weapon_power
    def get_health(self):
        return self.health
    def get_shields(self):
        return self.shields
    def get_name(self):
        return self.name
    def get_accuracy(self):
        return self.accuracy

    def change_speed(self, num):
        self.speed += num
    def change_weapon_power(self, num):
        self.weapon_power += num
    def change_health(self, num):
        self.health += num
    def change_shields(self, num):
        self.shields += num
    def change_name(self, name):
        self.name = name
    def change_accuracy(self, num):
        self.accuracy += num
    
    def take_damage(self, num):
        self.shields -= num
        if self.shields < 0:
            self.health += self.shields
            self.shields = 0

    
    
    

