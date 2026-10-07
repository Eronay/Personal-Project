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
                "energy cost": 1,
                "target": "enemy"
            },

            "Great Swing": {
                "affinity": "Strength",
                "dmg min": 1,
                "dmg max": 8,
                "die count": 1,
                "element": "physical",
                "type": "attack",
                "energy cost": 2,
                "target": "enemy"
            },

            "Endure": {
                "affinity": "Vitality",
                "block min": 1,
                "block max": 6,
                "die count": 1,
                "type": "block",
                "energy cost": 2,
                "target": "self"
            },

            "Whirlwind": {
                "affinity": "Strength",
                "dmg min": 1,
                "dmg max": 4,
                "die count": 1,
                "element": "physical",
                "type": "attack",
                "energy cost": 4,
                "target": "all"
            },

            "Rage": {
                "type": "buff",
                "duration": 5,
                "energy cost": 1,
                "effect": "rage",
                "target": "self",
                "intensity": 1
            },

            "Second Wind": {
                "type": "buff",
                "duration": 2,
                "energy cost": 3,
                "effect": "regen",
                "target": "self",
                "intensity": 1
            }

            
        }
