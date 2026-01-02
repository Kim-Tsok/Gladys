import random
from combat import fight
from weapons import weapons
from armour import armour
from enemies import enemies

player = {
    "health": 100,
    # This mystery stat will either be assigned once at the beginning of a play through or at the start of a fight and will act as multiplier or a sort of luck stat
    "mystery_stat": random.randint(5, 9),
    "gender": "Sir",
    "status": None
}

print(f"Welcome here, {player['gender']}!")
weapon = weapons["excalibur"].copy()
fight(player, weapon, armour, enemies["goblin"])
input("You have defeated the goblin! Now you must face the ogre! ")
fight(player, weapon, armour, enemies["ogre"])
