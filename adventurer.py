from dice import d6
from creature import Creature


class Adventurer(Creature):
    def __init__(self, name):
        Creature.__init__(self, name)
        self.courage = 0
        self.armor_locations = {
            'head': 0,
            'arms': 0,
            'body': 0,
            'waist': 0,
            'legs': 0,
        }
        self.run_log = {
            'monsters killed': [],
            'rooms cleared': 0
        }

    def set_courage(self, courage):
        self.courage = courage

    def take_damage(self, damage, hit_location):
        def take_severe_wound():
            print(f'{self.name} suffers a severe {hit_location} wound!')
            self.courage -= 1
            print(f"{self.name}'s courage is decreased to {self.courage}!")
            if current_armor > 0:
                self.hp -= damage - current_armor
            else:
                self.hp -= damage
            print(f"{self.name}'s hp is decreased to {self.hp}!")

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
            print(f'{enemy.name} hits {self.name} in the head for {enemy.strength} damage')
            self.take_damage(enemy.strength, 'head')
        elif die_roll == 2:
            print(f'{enemy.name} hits {self.name} in the arms for {enemy.strength} damage')
            self.take_damage(enemy.strength, 'arms')
        elif die_roll == 3 or die_roll == 4:
            print(f'{enemy.name} hits {self.name} in the body for {enemy.strength} damage')
            self.take_damage(enemy.strength, 'body')
        elif die_roll == 5:
            print(f'{enemy.name} hits {self.name} in the waist for {enemy.strength} damage')
            self.take_damage(enemy.strength, 'waist')
        elif die_roll == 6:
            print(f'{enemy.name} hits {self.name} in the legs for {enemy.strength} damage')
            self.take_damage(enemy.strength, 'legs')
