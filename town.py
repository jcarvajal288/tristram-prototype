import adventurer
import dungeon
from adventurer import Adventurer


class Town(object):
    def __init__(self):
        self.heroes = []
        self.dungeon = dungeon.Dungeon()

    def add_hero(self):
        self.heroes.append(adventurer.create_adventurer())