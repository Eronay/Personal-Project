import random
import math




class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.mana = 100
        self.health_regen = 0
        self.mana_regen = 5 * self.stats["Intelligence"]
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
        for i, ability in enumerate(self.abilities):
            print(f"{i+1}) {ability}")
        while True:
            try:
                selected_number = int(input("\nSelect Your Ability"))
                if selected_number < 1 or selected_number > len(self.abilities):
                    print("Please select a number within range")
                    continue
                chosen_ability = list(self.abilities.keys())[selected_number - 1]
                self.chosen_ability = chosen_ability
                return chosen_ability
            except ValueError:
                print("You must select a number")
                continue

    def use_player_ability(self, ability,  target):
        mana_cost = self.abilities[ability]["mana cost"]
        if self.mana < mana_cost:
            print("Must construct additional pylons")
            return
        self.mana -= mana_cost
        if self.abilities[ability]["type"] == "buff":
            self.apply_player_buff(self.abilities[ability]["duration"], self.abilities[ability]["effect"])
            print(f"\nYou spend {mana_cost} energy to buff yourself with {self.abilities[ability]["effect"]}")
        elif self.abilities[ability]["type"] == "attack":
            print(f"\nYou spend {mana_cost} energy to use {ability} on {target.name}")
            self.player_uses_attack(ability, target)
        elif self.abilities[ability]["type"] == "block":
            print(f"\nYou spend {mana_cost} mana in order to use {ability} to defend yourself")

    def player_uses_attack(self, ability, target):
        damage = self.calc_player_dmg(ability, target)
        if damage > 0:
            if self._vulnerable_check(ability, target) == True:
                print(f"{target.name} appears to be VULNERABLE to {self.abilities[ability]["element"]} damage!")
            if self._resistant_check(ability, target) == True:
                print(f"{target.name} appears to be RESISTANT to {self.abilities[ability]["element"]} damage!")
            print(f"You deal {damage} damage")
            target.health -= damage
            target.is_alive = target.health > 0
        else:
            print(f"{target.name} managed to avoid taking damage! The cheeky bugger!")

    def apply_player_buff(self, duration, effect):
        if effect == "rage":
            self.dmg_modifier *= 2
            self.rage_duration = duration
            print("You fly into a rage")
            

    def player_turn_start(self):
        ## Make regening mana a whole other function, then you can check for if you'll hit max mana and also apply buffs.
        self.mana += self.mana_regen
        print(f"You regain {self.mana_regen} mana at the start of your turn")
        if self.rage_duration > 0:
            self.rage_duration -= 1
            if self.rage_duration == 0:
                self.dmg_modifier /= 2
                print("Your rage has worn off")
            else:
                print(f"You have {self.rage_duration} turns of rage left")

    def calc_player_dmg(self, ability, target):
        base_damage = 0
        for i in range(0, self.abilities[ability]["die count"]):
            base_damage += random.randint(self.abilities[ability]["dmg min"], self.abilities[ability]["dmg max"])
        ability_affinity = self.abilities[ability]["affinity"]
        modified_dmg = math.ceil((base_damage + self.stats[ability_affinity]) * self.dmg_modifier)
        if target.abilities[target.chosen_ability]["type"] == "block":
            block_amount = 0
            for i in range(0, target.abilities[target.chosen_ability]["die count"]):
                block_amount += random.randint(target.abilities[target.chosen_ability]["block min"], target.abilities[target.chosen_ability]["block max"])
            modified_block = block_amount + target.stats[target.abilities[target.chosen_ability]["affinity"]]
            unblocked_dmg = modified_dmg - modified_block
            if unblocked_dmg <= 0:
                return 0
            else:
                print(f"{target.name} managed to reduce your attack by {block_amount}!")
                if self._vulnerable_check(ability, target) == True:
                    final_damage = unblocked_dmg * 2
                    return math.ceil(final_damage)
                if self._resistant_check(ability, target) == True:
                    final_damage = math.ceil(unblocked_dmg *0.5)
                    return math.ceil(final_damage)
                else:
                    return math.ceil(unblocked_dmg)
        else:
            if self._vulnerable_check(ability, target) == True:
                final_damage = math.ceil(modified_dmg * 2)
                return final_damage
            if self._resistant_check(ability, target) == True:
                final_damage = math.ceil(modified_dmg*0.5)
                return final_damage
            else:
                return math.ceil(modified_dmg)


    def _vulnerable_check(self, ability, target):
        if self.abilities[ability]["element"] in target.vulnerabilities:
            return True

    def _resistant_check(self, ability, target):
        if self.abilities[ability]["element"] in target.resistances:
            return True




