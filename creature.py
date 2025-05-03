class Creature(object):
    def __init__(self, name):
        self.name = name
        self.accuracy = 0
        self.strength = 0
        self.evasion = 0
        self.luck = 0
        self.speed = 0

    def set_accuracy(self, acc):
        self.accuracy = acc

    def set_strength(self, strn):
        self.strength = strn

    def set_evasion(self, eva):
        self.evasion = eva

    def set_luck(self, luck):
        self.luck = luck

    def set_speed(self, spd):
        self.speed = spd
