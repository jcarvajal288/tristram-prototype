from src.actors.creature import Creature
from src.util.dice import d10


class Monster(Creature):
    def __init__(self, name):
        super().__init__(name)
        self.toughness = 2
        self.damage = 1

    def set_toughness(self, tough):
        self.toughness = tough

    def set_damage(self, dmg):
        self.damage = dmg

    def take_hit(self, hero):
        damage_roll = d10() + hero.weapon.power + hero.strength
        damage_dealt = min(max(0, damage_roll - self.toughness), hero.weapon.power)
        print(f'{hero.name} hits {self.name} for {damage_dealt} damage (rolled {damage_roll} vs {self.toughness})')
        self.hp.current -= damage_dealt


def goblin():
    enemy = Monster('Goblin')
    enemy.set_accuracy(5)
    enemy.set_evasion(0)
    enemy.set_luck(0)
    enemy.set_speed(1)
    enemy.set_hp(3)
    enemy.set_toughness(2)
    enemy.set_damage(1)
    return enemy


def orc():
    enemy = Monster('Orc')
    enemy.set_accuracy(4)
    enemy.set_damage(1)
    enemy.set_evasion(0)
    enemy.set_luck(0)
    enemy.set_speed(2)
    enemy.set_hp(5)
    enemy.set_toughness(3)
    enemy.set_damage(1)
    return enemy
