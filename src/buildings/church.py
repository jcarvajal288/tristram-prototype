class Church(object):
    def __init__(self):
        self.healing_cost = 5

    def visit(self, hero):
        if hero.wants_to_heal():
            if hero.gold >= self.healing_cost:
                hero.hp.reset()
                hero.gold -= self.healing_cost
                print(f'{hero.name} spends {self.healing_cost} gold to heal at the church. ({hero.gold} gold left)')
            else:
                print(f"{hero.name} wants to heal, but can't afford it.")