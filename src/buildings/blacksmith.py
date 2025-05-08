from src.equipment import weapon


class Blacksmith(object):
    def __init__(self):
        self.inventory = {
            weapon.dagger(): Item(5, 5),
            weapon.shortsword(): Item(5, 10),
        }

    def visit(self, hero):
        in_stock_weapons = [w for w in self.inventory.keys() if self.inventory[w].quantity > 0]
        affordable_weapons = [w for w in in_stock_weapons if self.inventory[w].price <= hero.gold]
        desirable_weapons = [w for w in affordable_weapons if w.level > hero.weapon.level]
        if len(desirable_weapons) > 0:
            highest_level_affordable_weapon = sorted(desirable_weapons, key=lambda w: w.level)[-1]
            hero.gold -= self.inventory[highest_level_affordable_weapon].price
            self.inventory[highest_level_affordable_weapon].quantity -= 1
            hero.weapon = highest_level_affordable_weapon
            print(f'{hero.name} buys a {highest_level_affordable_weapon.name} at the blacksmith for {self.inventory[highest_level_affordable_weapon].price} gold ({hero.gold} gold left)')
        else:
            print(f'{hero.name} finds nothing affordable of interest at the blacksmith')


class Item(object):
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price