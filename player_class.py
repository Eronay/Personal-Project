import random
import math




class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.health_cap = 100
        self.mana = 100
        self.mana_cap = 100
        self.health_regen = 0
        self.stats = {
                    "Strength": 3,
                    "Agility" : 2,
                    "Intelligence" : 2,
                    "Vitality" : 3
                }
        self.base_mana_regen = 5 * self.stats["Intelligence"]
        self.buffs = {}
        self.is_alive = self.health > 0
        self.dmg_modifier = 1
        self.rage_modifier = 1
        self.rage_duration = 0
        self.clarity_duration = 0
        self.clarity_intensity = 0
        self.regen_intensity = 0
        self.regen_duration = 0
        self.chosen_ability = None
        self.initiative = None
        self.character_type = "player"
        self.target = None

    def roll_player_initiative(self):
        initiative_roll = random.randint(1, 6) + self.stats["Agility"]
        self.initiative = initiative_roll
        print(f"You rolled a {initiative_roll} for your initiative")

    def select_player_ability(self):
        for i, ability in enumerate(self.abilities):
            print(f"{i+1}) {ability}")
        while True:
            try:
                selected_number = int(input("\nSelect Your Ability "))
                if selected_number < 1 or selected_number > len(self.abilities):
                    print("Please select a number within range")
                    continue
                chosen_ability = list(self.abilities.keys())[selected_number - 1]
                self.chosen_ability = chosen_ability
                return chosen_ability
            except ValueError:
                print("You must select a number")
                continue

    def player_acquire_target(self, ability, enemies, allies):
        if self.abilities[ability]["target"] == "self":
            self.target = self
        elif self.abilities[ability]["target"]  == "ally":
            for i, ally, in enumerate(allies):
                print(f"{i+1}) {ally}")
            while True:
                try:
                    self.target = allies[int(input("\nSelect your target"))]
                    break
                except ValueError:
                    print("Please select a valid target")
        elif self.abilities[ability]["target"] == "enemy":
            for i, enemy in enumerate(enemies):
                print(f"{i+1}) {enemy.name}")
            while True:
                try:
                    self.target = enemies[int(input("\nSelect your target")) -1]
                    break
                except ValueError:
                    print("Please select a valid target")
                except IndexError:
                    print("Please select a valid target")
            


    def use_player_ability(self, ability):
        mana_cost = self.abilities[ability]["mana cost"]
        if self.mana < mana_cost:
            print("Must construct additional pylons")
            return
        self.mana -= mana_cost
        if self.abilities[ability]["type"] == "buff":
            self.apply_player_buff(self.abilities[ability]["duration"], self.abilities[ability]["effect"], self.abilities[ability]["intensity"], self.target)
            print(f"\nYou spend {mana_cost} energy to buff {self.target.name} with {self.abilities[ability]["effect"]}")
        elif self.abilities[ability]["type"] == "attack":
            print(f"\nYou spend {mana_cost} energy to use {ability} on {self.target.name}")
            self.player_uses_attack(ability, self.target)
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

    def apply_player_buff(self, duration, effect, intensity, target):
        if effect == "rage":
            target.apply_player_rage(duration, intensity)
        if effect == "clarity":
            target.apply_player_clarity(duration, intensity)
        if effect == "regen":
            target.apply_player_regen(duration, intensity)

    def apply_player_regen(self, duration, intensity):
        if self.regen_duration > 0:
            print(f"{self.name}'s regeneration has been overwritten")
            self.regen_intensity = intensity
            self.regen_duration = duration
        else:
            print(f"{self.name} has started to regenerate")
            self.regen_intensity = intensity
            self.regen_duration = duration

    def handle_regen_decay(self):
        if self.regen_duration > 0:
            self.regen_duration -= 1
            if self.regen_duration == 0:
                self.regen_intensity = 0
                print(f"{self.name} has stopped regenerating")
            else:
                print(f"{self.name} has {self.regen_duration} turns left of their regeneration")

    def player_regen_health(self):
        regen_amount = self.stats["Vitality"] * self.regen_intensity
        if self.regen_duration > 0:
            self.health += regen_amount
            if self.health > self.health_cap:
                self.health = self.health_cap
                print(f"{self.name} heals back up to full")
            else:
                print(f"{self.name} heals for {regen_amount} health points")

    def apply_player_rage(self, duration, intensity):
        if self.rage_duration > 0:
            self.rage_duration += duration
            print(f"{self.name}'s rage is refreshed")
        else:
            self.rage_modifier *= 1 + intensity
            self.rage_duration = duration
            print(f"{self.name} flies into a rage")


    def handle_player_rage_decay(self):
        if self.rage_duration > 0:
            self.rage_duration -= 1
            if self.rage_duration == 0:
                self.rage_modifier = 1
                print("Your rage has worn off")
            else:
                print(f"You have {self.rage_duration} turns of rage left")

    def apply_player_clarity(self, duration, intensity):
        if self.clarity_duration > 0:
            self.clarity_duration += duration
            print(f"{self.name}'s mind sharpens and their sense of clarity extends")
        else:
            self.clarity_duration += duration
            self.clarity_intensity += intensity
            print(f"{self.name} enters a state of intense focus")

    def handle_clarity_decay(self):
        if self.clarity_duration > 0:
            self.clarity_duration -= 1
            if self.clarity_duration == 0:
                self.clarity_intensity = 0
                print("Your sense of clarity has worn off")
            else:
                print(f"You have {self.clarity_duration} turns of clarity left")

    def player_regen_mana(self):
        mana_regen = self.base_mana_regen
        if self.clarity_duration > 0:
            mana_regen *= 1 + self.clarity_intensity
        self.mana += mana_regen
        if self.mana >= self.mana_cap:
            self.mana = self.mana_cap
        print(f"You recover {mana_regen} mana at the start of your turn")

    

    def player_turn_start(self):
        self.player_regen_mana() ## decide how buffs interact with turns, whether they wear off before or after turn start calcu
        self.player_regen_health()
        self.handle_clarity_decay()
        self.handle_regen_decay()


    def calc_player_dmg(self, ability, target):
        base_damage = 0
        for i in range(0, self.abilities[ability]["die count"]):
            base_damage += random.randint(self.abilities[ability]["dmg min"], self.abilities[ability]["dmg max"])
        ability_affinity = self.abilities[ability]["affinity"]
        modified_dmg = math.ceil((base_damage + self.stats[ability_affinity]) * self.dmg_modifier * self.rage_modifier)
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




