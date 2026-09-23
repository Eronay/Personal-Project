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
        print(f"{self.name} has chosen to use {chosen_ability}, think carefully!")

    def use_enemy_ability(self, ability, target):
        if self.abilities[ability]["type"] == "attack":
            damage = self.calc_enemy_damage(ability, target)
            if damage <= 0:
                print(f"The {self.name} attacks with {ability}, but you manage to block it!")
            else:
                print(f"The {self.name} attacks you with {ability} and deals {damage} damage!")
                target.health -= damage

    def calc_enemy_damage(self, ability, target):
        base_damage = 0
        for i in range(0, self.abilities[ability]["die count"]):
            base_damage += random.randint(self.abilities[ability]["dmg min"], self.abiilties[ability]["dmg max"])
        ability_affinity = self.abilities[ability]["affinity"]
        modified_dmg = (base_damage + self.stats[ability_affinity]) * self.dmg_modifier
        if target.chosen_ability["type"] == "block":
            block_amount = 0
            for i in range(0, target.abilities[target.chosen_ability]["die count"]):
                block_amount += random.randint(target.abilities[target.chosen_ability]["block min"], target.abilities[target.chosen_ability]["block max"])
            modified_block = block_amount + target.stats[target.abilities[self.chosen_ability]["affinity"]]
            unblocked_dmg = modified_dmg - modified_block
            if unblocked_dmg <= 0:
                return 0
            else:
                print(f"You managed to reduce their damage by {modified_block}")
                return unblocked_dmg

        else:
            return modified_dmg

    def roll_enemy_initiative(self):
        initative_roll = random.randint(1, 6) + self.stats["Agility"]
        self.initiative = initative_roll
        print(f"The {self.name} has rolled a {initative_roll} for initiative")
