from enemy_class import Enemy
from enemies.rat import Rat
import random

def generate_enemies_rats():
    number_of_enemies = random.randint(1,4)
    list_of_enemies = []
    for i in range(0, number_of_enemies):
        list_of_enemies.append(Rat(f"Rat {i}"))
    return list_of_enemies


def select_enemies():
    enemy = Rat("Rat")
    return enemy

