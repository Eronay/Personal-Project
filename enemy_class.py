import random
import math

class Enemy:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.mana = 100
        self.buffs = {}
        self.chosen_ability = None
        self.is_alive = self.health > 0
        self.dmg_modifier = 1

    def select_enemy_ability(self):
        ability_list = list(self.abilities.keys())
        ability_chances = [self.abilities[ability]["chance"] for ability in ability_list]
        chosen_ability = random.choices(ability_list, weights = ability_chances, k=1)[0]
        self.chosen_ability = chosen_ability

    def use_enemy_ability(self, ability, target):
        if target.chosen_ability["type"] == "block":
            ## TBC

    def calc_enemy_damage(self, ability, target):
        ## TBC

    def roll_enemy_initiative(self):
        initative_roll = random.randint(1, 6) + self.stats["Agility"]
        self.initiative = initative_roll
        print(f"The {self.name} has rolled a {initative_roll} for initiative")
