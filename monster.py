from creature import Creature


class Monster(Creature):
    def __init__(self, name):
        Creature.__init__(self, name)
        self.hp = 0

    def set_hp(self, hp):
        self.hp = hp


def goblin():
    enemy = Monster('Goblin')
    enemy.set_accuracy(5)
    enemy.set_strength(1)
    enemy.set_evasion(0)
    enemy.set_luck(0)
    enemy.set_speed(4)
    enemy.set_hp(3)
    return enemy
