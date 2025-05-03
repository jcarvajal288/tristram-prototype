import random

def d10():
    return random.randint(1, 10)

def d6():
    return random.randint(1, 6)


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
        


class Monster(Creature):
    def __init__(self, name):
        Creature.__init__(self, name)
    
    def set_hp(self, hp):
        self.hp = hp


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
    
    def set_courage(self, courage):
        self.courage = courage

    def take_damage(self, damage, hit_location):
        if hit_location == 'head':
            if self.armor_locations['head'] > -1:
                self.armor_locations['head'] -= damage
            if self.armor_locations[hit_location] == -1:
                print(f'{self.name} suffers a severe head wound!')
                self.courage -= 1
                print(f"{self.name}'s courage is decreased to {self.courage}!")
        else:
            if self.armor_locations[hit_location] > -2:
                self.armor_locations[hit_location] -= damage
            if self.armor_locations[hit_location] == -1:
                print(f'{self.name} suffers a light {hit_location} wound!')
            elif self.armor_locations[hit_location] == -2:
                print(f'{self.name} suffers a severe {hit_location} wound!')
                self.courage -= 1
                print(f"{self.name}'s courage is decreased to {self.courage}!")

    
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


def did_adventurer_win_initiative(adventurer, enemy):
    adventurer_roll = d10()
    enemy_roll = d10()
    adventurer_passed = adventurer_roll < adventurer.speed
    enemy_passed = enemy_roll < enemy.speed
    if adventurer_passed and enemy_passed or not adventurer_passed and not enemy_passed:
        return adventurer_roll >= enemy_roll
    return adventurer_passed


def adventurer_turn(adventurer, enemy):
    print(f'{adventurer.name} attacks {enemy.name}')
    if d10() > adventurer.accuracy:
        print(f'{adventurer.name} hits {enemy.name} for {adventurer.strength} damage')
        enemy.hp -= adventurer.strength
        if enemy.hp <= 0:
            print(f'{enemy.name} dies!')
            return True;
    else: 
        print(f'{adventurer.name} misses {enemy.name}')
    return False

def enemy_turn(adventurer, enemy):
    print(f'{enemy.name} attacks {adventurer.name}')
    if d10() > enemy.accuracy:
        adventurer.take_hit_from(enemy)
        if adventurer.courage <= 0:
            print(f'{adventurer.name} retreats!')
            return True
    else: 
        print(f'{enemy.name} misses {adventurer.name}')
    return False


def run_combat(adventurer, enemy):
    while True:
        print("New Combat Round")
        if did_adventurer_win_initiative(adventurer, enemy):
            monster_died = adventurer_turn(adventurer, enemy)
            if monster_died:
                break;
            adventurer_retreated = enemy_turn(adventurer, enemy)
            if adventurer_retreated:
                break;
        else:
            adventurer_retreated = enemy_turn(adventurer, enemy)
            if adventurer_retreated:
                break;
            monster_died = adventurer_turn(adventurer, enemy)
            if monster_died:
                break;
            


def main():
    adventurer = Adventurer('Adventurer')
    adventurer.set_accuracy(4)
    adventurer.set_strength(1)
    adventurer.set_evasion(0)
    adventurer.set_luck(0)
    adventurer.set_speed(5)
    adventurer.set_courage(3)

    monster = Monster('Goblin') 
    monster.set_accuracy(5)
    monster.set_strength(1)
    monster.set_evasion(0)
    monster.set_luck(0)
    monster.set_speed(4)
    monster.set_hp(3)

    run_combat(adventurer, monster)


if __name__ == '__main__':
    main()
