import random

import adventurer
import dungeon


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
            


def main():
    hero = adventurer.Adventurer('Adventurer')
    hero.set_accuracy(4)
    hero.set_strength(1)
    hero.set_evasion(0)
    hero.set_luck(0)
    hero.set_speed(5)
    hero.set_courage(3)
    hero.set_hp(5)

    donjon = dungeon.Dungeon()
    for room_num in range(len(donjon.rooms)):
        print('=========================')
        print(f'Entering room {room_num}')
        print('=========================')
        run_combat(hero, donjon.rooms[room_num].enemy)
        if hero.hp <= 0:
            print("Hero has died!")
            break
        if hero.courage <= 0:
            print("Hero retreats!")
            break





if __name__ == '__main__':
    main()
