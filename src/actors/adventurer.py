from src import weapon, armor
from src.actors.creature import Creature
from src.dice import d6
from src.gauge import Gauge


class Adventurer(Creature):
    def __init__(self, name):
        Creature.__init__(self, name)
        self.strength = 0
        self.courage = Gauge(0)
        self.weapon = weapon.dagger()
        self.armor_locations = {
            'head': 0,
            'arms': 0,
            'body': 0,
            'waist': 0,
            'legs': 0,
        }
        self.equipment_slots = {
            'head': armor.no_armor('head'),
            'arms': armor.no_armor('arms'),
            'body': armor.no_armor('body'),
            'waist': armor.no_armor('waist'),
            'legs': armor.no_armor('legs'),
        }
        self.gold = 0
        self.run_log = {
            'monsters killed': [],
            'rooms cleared': 0,
            'gold recovered': 0
        }

    def set_strength(self, strn):
        self.strength = strn

    def set_courage(self, courage):
        self.courage = Gauge(courage)

    def reset(self):
        self.hp.reset()
        self.courage.reset()
        self.run_log = {
            'monsters killed': [],
            'rooms cleared': 0,
            'gold recovered': 0
        }
        for slot in self.equipment_slots.keys():
            self.armor_locations[slot] = self.equipment_slots[slot].armor_value

    def equip_armor(self, armor_item):
        self.equipment_slots[armor_item.slot] = armor_item

    def take_damage(self, damage, hit_location):
        def take_severe_wound():
            print(f'{self.name} suffers a severe {hit_location} wound!')
            self.courage.current -= 1
            print(f"{self.name}'s courage is decreased to {self.courage.current}!")
            if current_armor > 0:
                self.hp.current -= damage - current_armor
            else:
                self.hp.current -= damage
            print(f"{self.name}'s hp is decreased to {self.hp.current}!")

        current_armor = self.armor_locations[hit_location]

        if hit_location == 'head':
            if self.armor_locations['head'] > -1:
                self.armor_locations['head'] -= damage
            if self.armor_locations[hit_location] == -1:
                take_severe_wound()
        else:
            if self.armor_locations[hit_location] > -2:
                self.armor_locations[hit_location] -= damage
            if self.armor_locations[hit_location] == -1:
                print(f'{self.name} suffers a light {hit_location} wound!')
            elif self.armor_locations[hit_location] == -2:
                take_severe_wound()


    def take_hit_from(self, enemy):
        die_roll = d6()
        if die_roll == 1:
            print(f'{enemy.name} hits {self.name} in the head for {enemy.damage} damage')
            self.take_damage(enemy.damage, 'head')
        elif die_roll == 2:
            print(f'{enemy.name} hits {self.name} in the arms for {enemy.damage} damage')
            self.take_damage(enemy.damage, 'arms')
        elif die_roll == 3 or die_roll == 4:
            print(f'{enemy.name} hits {self.name} in the body for {enemy.damage} damage')
            self.take_damage(enemy.damage, 'body')
        elif die_roll == 5:
            print(f'{enemy.name} hits {self.name} in the waist for {enemy.damage} damage')
            self.take_damage(enemy.damage, 'waist')
        elif die_roll == 6:
            print(f'{enemy.name} hits {self.name} in the legs for {enemy.damage} damage')
            self.take_damage(enemy.damage, 'legs')

    def wants_to_heal(self):
        return self.hp.current <= self.hp.max / 2


def create_adventurer():
    hero = Adventurer('Adventurer')
    hero.set_accuracy(0)
    hero.set_strength(0)
    hero.set_evasion(0)
    hero.set_luck(0)
    hero.set_speed(0)
    hero.set_courage(3)
    hero.set_hp(5)
    hero.equip_armor(armor.leather_cap())
    hero.equip_armor(armor.leather_gloves())
    hero.equip_armor(armor.leather_cuirass())
    hero.equip_armor(armor.leather_tassets())
    hero.equip_armor(armor.leather_boots())
    hero.reset()
    return hero
