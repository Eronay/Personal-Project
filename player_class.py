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
        self.rage_duration = 0
        self.chosen_ability = None
        self.initiative = None
        self.stats = {
            "Strength": 3,
            "Agility" : 2,
            "Intelligence" : 2,
            "Vitality" : 3
        }

    def roll_player_initiative(self):
        initiative_roll = random.randint(1, 6) + self.stats["Agility"]
        self.initiative = initiative_roll
        print(f"You rolled a {initiative_roll} for your initiative")

    def select_player_ability(self):
        while True:
            try:
                selected_number = input("\nSelect Your Ability")
                if selected_number < 1 or selected_number > len(self.abilities):
                    print("Please select a number within range")
                    continue
                chosen_ability = list(self.abilities.keys())[selected_number - 1]
                return chosen_ability
            except ValueError:
                print("You must select a number")
                continue

    def use_player_ability(self, ability, target):
        mana_cost = self.abilities[ability]["mana cost"]
        if self.mana < mana_cost:
            print("Must construct additional pylons")
            return
        if self.abilities[ability]["type"] == "buff":
            self.apply_player_buff(self.abilities[ability]["duration"], self.abilities[ability]["effect"])
            print(f"You spend {mana_cost} energy to buff yourself with {self.abilities[ability]["effect"]}")
        else:
            print(f"You spend {mana_cost} energy to cast {ability} on {target.name}")
            damage = self.calc_player_dmg(ability, target)
            if damage > 0:
                if self._vulnerable_check(ability, target) == True:
                    print(f"{target.name} appears to be VULNERABLE to {self.abilities[ability]["element"]} damage!")
                if self._resistant_check(ability, target) == True:
                    print(f"{target.name} appears to be RESISTANT to {self.abilities[ability]["element"]} damage!")
                target.health -= damage
            else:
                print(f"{target.name} managed to avoid taking damage! The cheeky bugger!")

    def apply_player_buff(self, duration, effect):
        if effect == "rage":
            self.dmg_modifier *= 2
            self.rage_duration = duration
            print("You fly into a rage")

    def player_turn_start(self):
        if self.rage_duration > 0:
            self.rage_duration -= 1
            if self.rage_duration == 0:
                self.dmg_modifier *= 0.5
                print("Your rage has worn off")
            else:
                print(f"You have {self.rage_duration} turns of rage left")

    def calc_player_dmg(self, ability, target):
        base_damage = 0
        for i in range(0, self.abilities[ability]["die count"]):
            base_damage += random.randint(self.abilities[ability]["dmg min"], self.abilities[ability]["dmg max"])
        ability_affinity = self.abilities[ability]["affinity"]
        modified_dmg = (base_damage + self.stats[ability_affinity]) * self.dmg_modifier
        if target.chosen_ability["type"] == "block":
            block_amount = random.randint(target.abilities[target.chosen_ability]["block min"], target.abilities[target.chosen_ability]["block max"]) + target.stats[f"{target.abilities[target.chosen_ability]["affinity"]}"]
            unblocked_dmg = modified_dmg - block_amount
            if unblocked_dmg <= 0:
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




