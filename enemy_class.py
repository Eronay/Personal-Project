import random
import math

class Enemy:
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.mana = 100
        self.buffs = {}
        self.chosen_ability = None
        self.is_alive = self.health > 0
        self.dmg_modifier = 1
        self.character_type = "enemy"
        self.target = None
        self.block_amount = 0
        

    def select_enemy_ability(self, targets):
        ability_list = list(self.abilities.keys())
        ability_chances = [self.abilities[ability]["chance"] for ability in ability_list]
        chosen_ability = random.choices(ability_list, weights = ability_chances, k=1)[0]
        self.chosen_ability = chosen_ability
        if self.abilities[chosen_ability]["type"] == "attack":
            self.target = targets[random.randint(0, len(targets) -1)]
            print(f"{self.name} has chosen to attack {self.target.name} with {chosen_ability}")
        elif self.abilities[chosen_ability]["type"] == "block":
            self.block_amount += random.randint(self.abilities[chosen_ability]["block min"], self.abilities[chosen_ability]["block max"]) + self.stats[self.abilities[chosen_ability]["affinity"]]
            print(f"{self.name} has chosen to defend themselves with {chosen_ability} for {self.block_amount} points of damage")
            self.target = None

    def enemy_turn_start(self):
        self.block_amount = 0

    def use_enemy_ability(self, ability, target):
        if self.abilities[ability]["type"] == "attack":
            damage = self.calc_enemy_damage(ability, target)
            if damage <= 0:
                print(f"The {self.name} attacks with {ability}, but {target.name} manages to block it!")
            else:
                print(f"The {self.name} attacks {target.name} with {ability} and deals {damage} damage!")
                target.health -= damage
                target.is_alive = target.health > 0


    def calc_enemy_damage(self, ability, target):
        base_damage = 0
        for i in range(0, self.abilities[ability]["die count"]):
            base_damage += random.randint(self.abilities[ability]["dmg min"], self.abilities[ability]["dmg max"])
        ability_affinity = self.abilities[ability]["affinity"]
        modified_dmg = (base_damage + self.stats[ability_affinity]) * self.dmg_modifier
        if target.block_amount > 0:
            unblocked_dmg = modified_dmg - target.block_amount
            target.block_amount -= modified_dmg
            if unblocked_dmg <= 0:
                return 0
            else:
                print(f"You managed to reduce their damage by {modified_dmg - target.block_amount}")
                return math.ceil(unblocked_dmg)

        else:
            return math.ceil(modified_dmg)

    def roll_enemy_initiative(self):
        initative_roll = random.randint(1, 6) + self.stats["Agility"]
        self.initiative = initative_roll
        print(f"The {self.name} has rolled a {initative_roll} for initiative")
