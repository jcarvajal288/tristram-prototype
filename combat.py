import dungeon
from adventurer import create_adventurer
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

def summarize_run(hero, donjon):
    print('')
    print('=== Run Summary ===')
    if hero.hp <= 0:
        print('Hero is Dead!')
    elif hero.run_log['rooms cleared'] < len(donjon.rooms):
        print('Hero is Alive!')
    else:
        print('Hero is Victorious!')
    print(f'Rooms cleared: {hero.run_log["rooms cleared"]}')
    print(f'Monsters killed: {len(hero.run_log["monsters killed"])}')
    print(f'Gold recovered: {hero.gold}')
    print(f'HP left: {hero.hp}')


def main():
    hero = create_adventurer()
    donjon = dungeon.Dungeon()
    for room_num in range(len(donjon.rooms)):
        print('=========================')
        print(f'Entering room {room_num}')
        print('=========================')
        enemy = donjon.rooms[room_num].enemy
        if enemy:
            run_combat(hero, enemy)
        if hero.hp <= 0:
            print("Hero has died!")
            break
        if donjon.rooms[room_num].gold:
            print(f'Hero picks up {donjon.rooms[room_num].gold} gold!')
            hero.gold += donjon.rooms[room_num].gold
        hero.run_log['rooms cleared'] += 1
        if hero.courage <= 0:
            print("Hero retreats!")
            break
        if room_num == len(donjon.rooms) - 1:
            print("Dungeon completed!")
            break
    summarize_run(hero, donjon)



if __name__ == '__main__':
    main()
