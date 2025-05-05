class Creature(object):
    def __init__(self, name):
        self.name = name
        self.accuracy = 0
        self.strength = 0
        self.evasion = 0
        self.luck = 0
        self.speed = 0
        self.max_hp = 0
        self.current_hp = 0

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

    def set_hp(self, hp):
        self.max_hp = hp
        self.current_hp = hp


def goblin():
    enemy = Creature('Goblin')
    enemy.set_accuracy(5)
    enemy.set_strength(1)
    enemy.set_evasion(0)
    enemy.set_luck(0)
    enemy.set_speed(4)
    enemy.set_hp(3)
    return enemy
