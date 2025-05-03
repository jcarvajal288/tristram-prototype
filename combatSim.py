import random

import adventurer
import monster


def d10():
    return random.randint(1, 10)

def d6():
    return random.randint(1, 6)


def did_hero_win_initiative(hero, enemy):
    hero_roll = d10()
    enemy_roll = d10()
    hero_passed = hero_roll < hero.speed
    enemy_passed = enemy_roll < enemy.speed
    if hero_passed and enemy_passed or not hero_passed and not enemy_passed:
        return hero_roll >= enemy_roll
    return hero_passed


def hero_turn(hero, enemy):
    print(f'{hero.name} attacks {enemy.name}')
    if d10() > hero.accuracy:
        print(f'{hero.name} hits {enemy.name} for {hero.strength} damage')
        enemy.hp -= hero.strength
        if enemy.hp <= 0:
            print(f'{enemy.name} dies!')
            return True
    else: 
        print(f'{hero.name} misses {enemy.name}')
    return False

def enemy_turn(hero, enemy):
    print(f'{enemy.name} attacks {hero.name}')
    if d10() > enemy.accuracy:
        hero.take_hit_from(enemy)
        if hero.courage <= 0:
            print(f'{hero.name} retreats!')
            return True
    else: 
        print(f'{enemy.name} misses {hero.name}')
    return False


def run_combat(hero, enemy):
    while True:
        print("New Combat Round")
        if did_hero_win_initiative(hero, enemy):
            monster_died = hero_turn(hero, enemy)
            if monster_died:
                break
            hero_retreated = enemy_turn(hero, enemy)
            if hero_retreated:
                break
        else:
            hero_retreated = enemy_turn(hero, enemy)
            if hero_retreated:
                break
            monster_died = hero_turn(hero, enemy)
            if monster_died:
                break
            


def main():
    hero = adventurer.Adventurer('Adventurer')
    hero.set_accuracy(4)
    hero.set_strength(1)
    hero.set_evasion(0)
    hero.set_luck(0)
    hero.set_speed(5)
    hero.set_courage(3)

    enemy = monster.Monster('Goblin')
    enemy.set_accuracy(5)
    enemy.set_strength(1)
    enemy.set_evasion(0)
    enemy.set_luck(0)
    enemy.set_speed(4)
    enemy.set_hp(3)

    run_combat(hero, enemy)


if __name__ == '__main__':
    main()
