import creature


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
        self.enemy = creature.goblin()