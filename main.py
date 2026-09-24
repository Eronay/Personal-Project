from player_setup import player_setup
from turn_resolver import resolve_turn
from player_class import Player
from enemy_class import Enemy
from enemy_setup import select_enemy

def main():
    player = player_setup()
    enemy = select_enemy()
    i = 1
    while player.is_alive and enemy.is_alive:
        print(f"\n/// TURN {i} ///\n")
        i += 1
        resolve_turn(player, enemy)
        print(f"\nplayer health = {player.health}\nplayer mana = {player.mana}\n\nenemy health = {enemy.health}")
    if player.is_alive == False:
        print(f"The {enemy.name} has bested you in combat, sharpen your skills and try again young adventurer")
    elif enemy.is_alive == False:
        print(f"You have slain the foul {enemy.name} in honourable combat, praise be!")
    elif enemy.is_alive == False and player.is_alive == False:
        print(f"You and the {enemy.name} have slain one another in fierce battle! You appear to have been evenly matched")



main()
