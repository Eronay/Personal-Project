from enemy_class import Enemy
from enemies.rat import Rat
import random

def generate_enemies_rats():
    while True:
        try:
            enemy_number = int(input("\nHow many enemies would you like to face?"))
            break
        except ValueError:
            print("Input a number")
            continue

    list_of_enemies = []
    for i in range(0, enemy_number):
        list_of_enemies.append(Rat(f"Rat {i+1}"))
    return list_of_enemies


def select_enemies():
    enemy = Rat("Rat")
    return enemy

