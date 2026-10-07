import math
import random
from player_class import Player
from enemy_class import Enemy

def roll_all_initiatives(participants):
    for participant in participants:
        participant.initiative = (random.randint(1,6) + participant.stats["Agility"])
    sorted_order = sorted(participants, key = lambda participant: participant.initiative, reverse = True)
    print(f"\n //Initiative Order//\n")
    i = 1
    for character in sorted_order:
        print(f"{i}) {character.name}")
        i += 1
    print("\n")
    return sorted_order

def remove_dead(self):
    for character in self:
        if character.is_alive == False:
            print(f"{character.name} has been slain!")
            self.remove(character)

def execute_turn(self, enemies):
    if self.character_type == "player":
        for ability, target in self.chosen_abilities:
            self.target = target
            self.use_player_abilitity(ability, enemies)
    elif self.character_type == "enemy":
        self.use_enemy_ability(self.chosen_ability, self.target)

def resolve_turn(players, enemies):
    initiative_order = roll_all_initiatives(players + enemies)
    for enemy in enemies:
        enemy.select_enemy_ability(players)
    print("\n")
    for player in players:
        player.player_turn_start()
        print("\n")
        while player.remaining_energy > 0:
            print(f"{player.remaining_energy} energy remaining\n")
            chosen_ability = player.select_player_ability()
            print("\n")
            player.player_acquire_target(chosen_ability, enemies, players)
            print("\n")

    for character in initiative_order:
        execute_turn(character, enemies)
        remove_dead(enemies)


