from player_class import Player

class greatsword(Player):
    def __init__(self, name):
        super().__init__(name)
        self.abilities = {
            "Swing": {
                "affinity": "Strength",
                "dmg min": 1,
                "dmg max": 6,
                "die count": 1,
                "element": "physical",
                "type": "attack",
                "mana cost": 0
            },

            "Great Swing": {
                "affinity": "Strength",
                "dmg min": 1,
                "dmg max": 12,
                "die count": 1,
                "element": "physical",
                "type": "attack",
                "mana cost": 2
            },

            "Endure": {
                "affinity": "Vitality",
                "block min": 1,
                "block max": 6,
                "die count": 1,
                "type": "block",
                "mana cost": 10
            },

            "Whirlwind": {
                "affinity": "Strength",
                "dmg min": 1,
                "dmg max": 8,
                "die count": 3,
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
