from dice import *


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
            hero.run_log['monsters killed'].append(enemy)
            print(f'{enemy.name} dies!')
    else:
        print(f'{hero.name} misses {enemy.name}')


def enemy_turn(hero, enemy):
    print(f'{enemy.name} attacks {hero.name}')
    if d10() > enemy.accuracy:
        hero.take_hit_from(enemy)
    else:
        print(f'{enemy.name} misses {hero.name}')


def run_combat(hero, enemy):
    while True:
        print("=== New Combat Round ===")
        if did_hero_win_initiative(hero, enemy):
            hero_turn(hero, enemy)
            if enemy.hp <= 0:
                return
            enemy_turn(hero, enemy)
            if hero.hp <= 0:
                return
        else:
            enemy_turn(hero, enemy)
            if hero.hp <= 0:
                return
            hero_turn(hero, enemy)
            if enemy.hp <= 0:
                return


