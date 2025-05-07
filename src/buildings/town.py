from src.actors import adventurer
from src.buildings.church import Church


class Town(object):
    def __init__(self):
        self.heroes = []
        self.church = Church()

    def add_hero(self):
        self.heroes.append(adventurer.create_adventurer())

    def visit(self, hero):
        print("=======================")
        print(f"{hero.name} visits town.")
        print("=======================")
        self.church.visit(hero)