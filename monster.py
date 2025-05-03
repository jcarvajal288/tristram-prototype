from creature import Creature


class Monster(Creature):
    def __init__(self, name):
        Creature.__init__(self, name)

    def set_hp(self, hp):
        self.hp = hp
