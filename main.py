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
    turn_number = 1
    while player.is_alive and len(enemies) > 0:
        print(f"\n/// TURN {turn_number} ///\n")
        turn_number += 1
        resolve_turn(players, enemies)
        print(f"\nplayer health = {player.health}\n")
        print("\n")
        for enemy in enemies:
            print(f"{enemy.name} has {enemy.health} health left")

    if player.is_alive:
        print("Congratulations! You managed to best your foes")
    else:
        print("The wicked villains have managed to fell you!")
main()
