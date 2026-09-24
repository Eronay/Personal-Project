import math
import random
from player_class import Player
from enemy_class import Enemy

def resolve_turn(player, enemy):
    player.roll_player_initiative()
    enemy.roll_enemy_initiative()
    if player.initiative > enemy.initiative:
        enemy.select_enemy_ability()
        player.select_player_ability()
        player.use_player_ability(player.chosen_ability, enemy)
        enemy.use_enemy_ability(enemy.chosen_ability, player)

    elif player.initiative < enemy.initiative:
        enemy.select_enemy_ability()
        player.select_player_ability()
        enemy.use_enemy_ability(enemy.chosen_ability, player)
        player.use_player_ability(player.chosen_ability, enemy)

    elif player.initiative == enemy.initiative:
        turn_resolution = random.randint(1, 2)
        if turn_resolution == 1:
            enemy.select_enemy_ability()
            player.select_player_ability()
            player.use_player_ability(player.chosen_ability, enemy)
            enemy.use_enemy_ability(enemy.chosen_ability, player)

        else:
            enemy.select_enemy_ability()
            player.select_player_ability()
            enemy.use_enemy_ability(enemy.chosen_ability, player)
            player.use_player_ability(player.chosen_ability, enemy)