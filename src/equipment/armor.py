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


def hard_leather_cap():
    return Armor('Hard Leather Cap', 'head', 2)

def hard_leather_gloves():
    return Armor('Hard Leather Gloves', 'arms', 2)

def hard_leather_cuirass():
    return Armor('Hard Leather Cuirass', 'body', 2)

def hard_leather_tassets():
    return Armor('Hard Leather Tassets', 'waist', 2)

def hard_leather_boots():
    return Armor('Hard Leather Boots', 'legs', 2)
