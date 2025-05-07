from dice import *


def did_hero_win_initiative(hero, enemy):
    hero_roll = d10() + hero.evasion
    enemy_roll = d10() + enemy.evasion
    hero_passed = hero_roll < hero.speed
    enemy_passed = enemy_roll < enemy.speed
    if hero_passed and enemy_passed or not hero_passed and not enemy_passed:
        return hero_roll >= enemy_roll
    return hero_passed


def hero_turn(hero, enemy):
    for i in range(hero.weapon.speed + hero.speed):
        attack_roll = d10()
        target = hero.weapon.accuracy - hero.accuracy + enemy.evasion
        print(f'{hero.name} attacks {enemy.name} (rolled {attack_roll} vs {target})')
        if attack_roll >= target:
            enemy.take_hit(hero)
            if enemy.hp.current <= 0:
                hero.run_log['monsters killed'].append(enemy)
                print(f'{enemy.name} dies!')
                return
        else:
            print(f'{hero.name} misses {enemy.name}')


def enemy_turn(hero, enemy):
    for i in range(enemy.speed):
        attack_roll = d10()
        target = enemy.accuracy + enemy.evasion
        print(f'{enemy.name} attacks {hero.name} (rolled {attack_roll} vs {target})')
        if attack_roll >= target:
            hero.take_hit_from(enemy)
        else:
            print(f'{enemy.name} misses {hero.name}')


def run_combat(room, hero):
    for enemy in room.enemies:
        while True:
            print("=== New Combat Round ===")
            if did_hero_win_initiative(hero, enemy):
                hero_turn(hero, enemy)
                if enemy.hp.current <= 0:
                    break
                enemy_turn(hero, enemy)
                if hero.hp.current <= 0:
                    return
            else:
                enemy_turn(hero, enemy)
                if hero.hp.current <= 0:
                    return
                hero_turn(hero, enemy)
                if enemy.hp.current <= 0:
                    break


