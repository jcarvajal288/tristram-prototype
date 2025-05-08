class Weapon(object):
    def __init__(self, name):
        self.name = name
        self.speed = 1
        self.accuracy = 9
        self.power = 1
        self.level = 0

    def set_speed(self, speed):
        self.speed = speed

    def set_accuracy(self, accuracy):
        self.accuracy = accuracy

    def set_power(self, power):
        self.power = power

    def set_level(self, level):
        self.level = level


def dagger():
    weapon = Weapon('Dagger')
    weapon.set_speed(2)
    weapon.set_accuracy(7)
    weapon.set_power(1)
    weapon.set_level(0)
    return weapon

def shortsword():
    weapon = Weapon('Short Sword')
    weapon.set_speed(2)
    weapon.set_accuracy(7)
    weapon.set_power(2)
    weapon.set_level(1)
    return weapon
