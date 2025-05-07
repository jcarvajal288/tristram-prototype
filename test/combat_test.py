import unittest
from unittest.mock import patch

from src import combat
from src.actors import adventurer, monster


class TestCombat(unittest.TestCase):

    @patch('combat.d10')
    def test_hero_turn(self, d10_mock):
        hero = adventurer.create_adventurer()
        goblin = monster.goblin()
        d10_mock.side_effect = [9, 9]
        combat.hero_turn(hero, goblin)
        self.assertEqual(goblin.current_hp, goblin.max_hp - 2)

    @patch('combat.d10')
    def test_hero_turn_2(self, d10_mock):
        hero = adventurer.create_adventurer()
        goblin = monster.goblin()
        d10_mock.side_effect = [6, 10]
        combat.hero_turn(hero, goblin)
        self.assertEqual(goblin.current_hp, goblin.max_hp - 1)
