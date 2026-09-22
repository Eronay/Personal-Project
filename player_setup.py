from player_class import Player
from weapons.greatsword import greatsword

def create_player_name():
    while True:
        player_name = input("\nWhat is your name traveller?\n")
        if len(player_name) > 20:
            print("\nPlease select a shorter name\n")
            continue
        return player_name

    
def choose_weapon():
    weapons = ["Greatsword"]
    for i, weapon in enumerate(weapons):
        print(f"{i+1}, {weapon}")
    while True:
        try:
            chosen_number = int(input("\nPlease select a worthy weapon\n"))
            if chosen_number <1 or chosen_number > len(weapons):
                print("Please select a valid option")
                continue
            chosen_weapon = weapons[chosen_number - 1]
            return chosen_weapon
        except ValueError:
            print("\nPlease select a number within range\n")

def create_player(player_name, chosen_weapon):
    if chosen_weapon == "Greatsword":
        player = greatsword(player_name)
    return player




def player_setup():
    player_name = create_player_name()
    chosen_weapon = choose_weapon()
    player = create_player(player_name, chosen_weapon)
    print(f"{player.name}, you have chosen the {chosen_weapon} to wield in glorious combat. May you strikes land true!")
    return player

player_setup()