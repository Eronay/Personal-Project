from player_setup import player_setup
from turn_resolver import resolve_turn
from player_class import Player
from enemy_class import Enemy
from enemy_setup import select_enemy

def main():
    player = player_setup()
    enemy = select_enemy()
    while player.is_alive and enemy.is_alive:
        resolve_turn(player, enemy)
        print(f"\nplayer health = {player.health}\nenemy health = {enemy.health}")



main()
