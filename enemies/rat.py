from enemy_class import Enemy

class Rat(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.stats = {
            "Strength": 1,
            "Agility": 2,
            "Intelligence": 0,
            "Vitality": 1,
        }


        self.abilities = {
            "Scratch": {
                "affinity": "strength",
                "dmg min": 1,
                "dmg max": 4,
                "die count": 1,
                "element": "physical",
                "type": "attack",
                "chance": 0.4
            },

            "Bite":{
                "affinity": "strength",
                "dmg min": 1,
                "dmg max": 6,
                "die count": 1,
                "element": "physical",
                "type": "attack",
                "chance": 0.2
            },

            "Tail Block":{
                "affinity": "vitality",
                "block min": 1,
                "block max": 4,
                "die count": 1,
                "type": "block",
                "chance": 0.4
            }
        }