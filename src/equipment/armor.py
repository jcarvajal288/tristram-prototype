class Armor(object):
    def __init__(self, name, slot, armor_value):
        self.name = name
        self.slot = slot
        self.armor_value = armor_value

def no_armor(slot):
    return Armor("Empty", slot, 0)

def leather_cap():
    return Armor('Leather Cap', 'head', 1)

def leather_gloves():
    return Armor('Leather Gloves', 'arms', 1)

def leather_cuirass():
    return Armor('Leather Cuirass', 'body', 1)

def leather_tassets():
    return Armor('Leather Tassets', 'waist', 1)

def leather_boots():
    return Armor('Leather Boots', 'legs', 1)
