from player_class import Player

class greatsword(Player):
    def __init__(self, name):
        super().__init__(name)
        self.abilities = {
            "Swing": {
                "affinity": "strength",
                "dmg min": 1,
                "dmg max": 6,
                "element": "physical",
                "type": "attack",
                "mana cost": 0
            },

            "Great Swing": {
                "affinity": "strength",
                "dmg min": 1,
                "dmg max": 12,
                "element": "physical",
                "type": "attack",
                "mana cost": 2
            },

            "Endure": {
                "affinity": "vitality",
                "block min": 1,
                "block max": 6,
                "type": "block",
                "mana cost": 10
            },

            "Whirlwind": {
                "affinity": "strength",
                "dmg min": 3,
                "dmg max": 24,
                "element": "physical",
                "type": "attack",
                "mana cost": 40
            },

            "Rage": {
                "type": "buff",
                "duration": 5,
                "mana cost": 15,
                "effect": "rage"
            }
            
        }
