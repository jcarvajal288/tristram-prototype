import combat
import creature

from dice import *


class Dungeon(object):
    def __init__(self):
        self.current_room = 0
        self.rooms = []
        for i in range(0, 10):
            self.rooms.append(Room())

    def current_room(self):
        return self.rooms[self.current_room]

    def enter(self, hero):
        print('=========================')
        print(f'{hero.name} enters the dungeon.')
        print('=========================')
        for room_num in range(len(self.rooms)):
            print('=========================')
            print(f'Entering room {room_num}')
            print('=========================')
            enemy = self.rooms[room_num].enemy
            if enemy:
                combat.run_combat(hero, enemy)
            if hero.current_hp <= 0:
                print(f"{hero.name} has died!")
                break
            if self.rooms[room_num].gold:
                print(f'{hero.name} picks up {self.rooms[room_num].gold} gold!')
                hero.gold += self.rooms[room_num].gold
            hero.run_log['rooms cleared'] += 1
            if hero.courage <= 0:
                print(f"{hero.name} retreats!")
                break
            if room_num == len(self.rooms) - 1:
                print("Dungeon completed!")
                break
        summarize_run(hero, self)


class Room(object):
    def __init__(self):
        if d6() <= 4:
            self.enemy = creature.goblin()
        else:
            self.enemy = None
        if d6() <= 2:
            self.gold = d10()
        else:
            self.gold = 0




def summarize_run(hero, donjon):
    print('')
    print('=== Run Summary ===')
    if hero.current_hp <= 0:
        print(f'{hero.name} is Dead!')
    elif hero.run_log['rooms cleared'] < len(donjon.rooms):
        print(f'{hero.name} is Alive!')
    else:
        print(f'{hero.name} is Victorious!')
    print(f'Rooms cleared: {hero.run_log["rooms cleared"]}')
    print(f'Monsters killed: {len(hero.run_log["monsters killed"])}')
    print(f'Gold recovered: {hero.gold}')
    print(f'HP left: {hero.current_hp}')


