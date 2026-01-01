import random
from combat import fight
from weapons import weapon
from armour import armour

player = {
    "health": 100,
    # This mystery stat will either be assigned once at the beginning of a play through or at the start of a fight and will act as multiplier or a sort of luck stat
    "mystery_stat" : random.randint(5,9),
    "gender": "Sir"
}

fight(player, weapon, armour, "Goblin", 111, 5)