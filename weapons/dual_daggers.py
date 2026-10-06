from player_class import Player

class dual_daggers(Player):
    def __init__(self, name):
        super().__init__(name)
        self.abilities = {
            "Stab": {
                "affinity": "Strength",
                "dmg min": 1,
                "dmg max": 4,
                "die count": 1,
                "element": "physical",
                "type": "attack",
                "mana cost": 0,
                "target": "enemy"
            },

            "Dual Stab": {
                "affinity": "Strength",
                "dmg min": 1,
                "dmg max": 4,
                "die count": 2,
                "element": "physical",
                "type": "attack",
                "mana cost": 2,
                "target": "enemy"
            },

            "Parry": {
                "affinity": "Agility",
                "block min": 1,
                "block max": 6,
                "die count": 1,
                "type": "block",
                "mana cost": 10,
                "target": "self"
            },

            "Fan of Knives": {
                "affinity": "Strength",
                "dmg min": 1,
                "dmg max": 4,
                "die count": 1,
                "element": "physical",
                "type": "attack",
                "mana cost": 40,
                "target": "all"
            },

            "Rogueish Cunning": {
                "type": "buff",
                "duration": 2,
                "mana cost": 20,
                "effect": "regen",
                "target": "self",
                "intensity": 1
            }






        }
