class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.mana = 100
        self.is_alive = self.health > 0

