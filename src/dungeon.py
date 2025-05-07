import combat
from src.actors import monster

from src.util.dice import *


class Dungeon(object):
    def __init__(self):
        self.current_room = 0
        self.rooms = []
        for i in range(0, 10):
            self.rooms.append(Room())

    def current_room(self):
        return self.rooms[self.current_room]

    def enter(self, hero):
        hero.reset()
        print('=========================')
        print(f'{hero.name} enters the dungeon.')
        print('=========================')
        for room_num in range(len(self.rooms)):
            print('=========================')
            print(f'Entering room {room_num}')
            print('=========================')
            self.rooms[room_num].enter(hero)
            if hero.courage.current <= 0 < hero.hp.current:
                print(f"{hero.name} retreats!")
                break
            if hero.hp.current <= 0:
                break
            if room_num == len(self.rooms) - 1:
                print("Dungeon completed!")
                break
        summarize_run(hero, self)


class Room(object):
    def __init__(self):
        self.enemies = []
        self.gold = 0
        self.populate_room()

    def populate_room(self):
        monster_roll = d10()
        if monster_roll <= 4:
            self.enemies.append(monster.goblin())
        elif monster_roll <= 6:
            self.enemies.append(monster.orc())
        else:
            self.enemies = []

        if d6() <= 2:
            self.gold = d10()
        else:
            self.gold = 0

    def enter(self, hero):
        combat.run_combat(self, hero)
        if hero.hp.current <= 0:
            print(f"{hero.name} has died!")
            self.gold += hero.gold
            hero.gold = 0
            return
        [self.enemies.remove(enemy) for enemy in self.enemies if enemy.hp.current <= 0]
        if self.gold:
            print(f'{hero.name} picks up {self.gold} gold!')
            hero.gold += self.gold
            hero.run_log['gold recovered'] += self.gold
            self.gold = 0
        hero.run_log['rooms cleared'] += 1


def summarize_run(hero, donjon):
    print('')
    print('=== Run Summary ===')
    if hero.hp.current <= 0:
        print(f'{hero.name} is Dead!')
    elif hero.run_log['rooms cleared'] < len(donjon.rooms):
        print(f'{hero.name} is Alive!')
    else:
        print(f'{hero.name} is Victorious!')
    print(f'Rooms cleared: {hero.run_log["rooms cleared"]}')
    print(f'Monsters killed: {len(hero.run_log["monsters killed"])}')
    print(f'Gold recovered: {hero.gold}')
    print(f'HP left: {hero.hp.current}')


