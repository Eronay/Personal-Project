import random
import math




class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.mana = 100
        self.health_regen = 0
        self.mana_regen = 5
        self.buffs = {}
        self.is_alive = self.health > 0
        self.dmg_modifier = 1
        self.stats = {
            "Strength": 3,
            "Agility" : 2,
            "Intelligence" : 2,
            "Vitality" : 3
        }

    def use_ability(self, ability, target):
        mana_cost = self.abilities[ability]["mana cost"]
        if self.mana < mana_cost:
            print("Must construct additional pylons")
            return
        print(f"You spend {mana_cost} energy to cast {ability} on {target.name}")
        if self._vulnerable_check(ability, target) == True:
            print(f"{target.name} appears to be VULNERABLE to {self.abilities[ability]["element"]} damage!")
        if self._resistant_check(ability, target) == True:
            print(f"{target.name} appears to be RESISTANT to {self.abilities[ability]["element"]} damage!")
        damage = self.calc_dmg(ability, target)
        target.health -= damage


    def turn_start(self):
        ## maybe handle buff expiration here or something??

    def calc_dmg(self, ability, target):
        base_damage = 0
        for i in range(0, self.abilities[ability]["die count"]):
            base_damage += random.randint(self.abilities[ability]["dmg min"], self.abilities[ability]["dmg max"])
        ability_affinity = self.abilities[ability]["affinity"]
        modified_dmg = (base_damage + self.stats[ability_affinity]) * self.dmg_modifier
        if target.chosen_ability["type"] == "block":
            block_amount = random.randint(target.abilities[target.chosen_ability]["block min"], target.abilities[target.chosen_ability]["block max"]) + target.stats[f"{target.abilities[target.chosen_ability]["affinity"]}"]
            unblocked_dmg = modified_dmg - block_amount
            if unblocked_dmg <= 0:
                print(f"{target.name} managed to avoid taking damage!")
                return 0
            else:
                print(f"{target.name} managed to reduce your attack by {block_amount}!")
                if self._vulnerable_check(ability, target) == True:
                    final_damage = unblocked_dmg * 2
                    return final_damage
                if self._resistant_check(ability, target) == True:
                    final_damage = math.ceil(unblocked_dmg *0.5)
                    return final_damage
                else:
                    return unblocked_dmg
        else:
            if self._vulnerable_check(ability, target) == True:
                final_damage = modified_dmg * 2
                return final_damage
            if self._resistant_check(ability, target) == True:
                final_damage = math.ceil(modified_dmg*0.5)
                return final_damage
            else:
                return modified_dmg


    def _vulnerable_check(self, ability, target):
        if self.abilities[ability]["element"] in target.vulerabilities:
            return True

    def _resistant_check(self, ability, target):
        if self.abilities[ability]["element"] in target.resistancec:
            return True




