import math
import random
from player_class import Player
from enemy_class import Enemy

def roll_all_initiatives(participants):
    for participant in participants:
        participant.initiative = (random.randint(1,6) + participant.stats["Agility"])
    sorted_order = sorted(participants, key = lambda participant: participant.initiative, reverse = True)
    print(sorted_order)
    return sorted_order

def remove_dead(self):
    for character in self:
        if character.is_alive == False:
            self.remove(character)

def execute_turn(self):
    if self.character_type == "player":
        self.use_player_ability(self.chosen_ability)
    elif self.character_type == "enemy":
        self.use_enemy_ability(self.chosen_ability, self.target)

def resolve_turn(players, enemies):
    initiative_order = roll_all_initiatives(players + enemies)
    for enemy in enemies:
        enemy.select_enemy_ability(players)
    for player in players:
        player.player_turn_start()
        player.select_player_ability()
        player.player_acquire_target(player.chosen_ability, enemies, players)
    for character in initiative_order:
        execute_turn(character)
    remove_dead(enemies)


