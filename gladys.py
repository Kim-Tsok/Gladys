import random
import traceback

from colorama import Fore

def main():
    from combat import fight
    from weapons import weapons
    from armour import armour
    from enemies import enemies
    from characters import characters
    from instructions import instructions
    
    player = {
        "health": 100,
        "mystery_stat": random.randint(5, 9),
        "gender": "Sir",
        "status": None
    }
    

    # Game Start
    input("Press Enter to start the game...")

    # Instructions
    instructions()

    # Prologue
    input(f"{characters['unknown']} What is your motivation for all of this, why do you do this? ")
    input(f"{characters['-unknown']}Make it easier on yourself, just give up. ")
    input(f"{characters['-unknown']}Give up on this stupid dream of trying to beat me. ")
    input("")
    input(f"{characters['person01']} Hey wake up! wake up you idiot. ")
    input(f"{characters['player']} What happened? ")
    input(f"{characters['person01']} You were shaking and mumbling something in your sleep. ")
    input(f"{characters['player']} I had a dream. ")
    input(f"{characters['person01']} You saw him again, didn't you? ")
    input(f"{characters['player']} It was terrifying. My movements felt heavy, my breathing was off. ")
    input(f"{characters['-player']}I'm terrified ")
    
    while True:
        choice = input(
            f"{characters['person01']} Wanna spar cause we're weirdos? (y/n) "
        ).strip().lower()

        if choice == "y":
            weapon = weapons["excalibur"].copy()
            fight(player, weapon, armour, enemies["knight01"])
            break

        elif choice == "n":
            input(f"{characters['-person01']}That's alright")
            break

        else:
            print("Invalid input. Type y or n.")

        # fight(player, weapon, armour, enemies["knight01"])
        
    input("")
    input("Didn't that feel rejuvinating. Doesn't it feel nice to stretch a bit")



if __name__ == "__main__":
    try:
        main()
    except Exception:
        traceback.print_exc()
        input("\nGame crashed. Press Enter to exit...")
