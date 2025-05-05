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