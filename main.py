from player_setup import player_setup
from turn_resolver import resolve_turn
from player_class import Player
from enemy_class import Enemy
from enemy_setup import generate_enemies_rats

def main():
    players = []
    player = player_setup()
    players.append(player)
    enemies = generate_enemies_rats()
    i = 1
    while player.is_alive and len(enemies) > 0:
        print(f"\n/// TURN {i} ///\n")
        i += 1
        resolve_turn(players, enemies)
        print(f"\nplayer health = {player.health}\nplayer mana = {player.mana}\n")
main()
