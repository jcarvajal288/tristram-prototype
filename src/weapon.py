class Weapon(object):
    def __init__(self):
        self.speed = 1
        self.accuracy = 9
        self.power = 1

    def set_speed(self, speed):
        self.speed = speed

    def set_accuracy(self, accuracy):
        self.accuracy = accuracy

    def set_power(self, power):
        self.power = power


def dagger():
    weapon = Weapon()
    weapon.set_speed(2)
    weapon.set_accuracy(7)
    weapon.set_power(1)
    return weapon