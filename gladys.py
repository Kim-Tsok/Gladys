import random

player = {
    "health": 100,
    # This mystery stat will either be assigned once at the beginning of a play through or at the start of a fight and will act as multiplier or a sort of luck stat
    "mystery_stat" : random.randint(5,9),
    "gender": "Sir"
}

weapon = {
    "total_damage": 1,
    "base_damage": 2,
    "has_weapon": True,
    "current_weapon": "Dagger",
    "weapon_damage": 9,
}

armour = {
    "rating": 1,
    "has_helmet": True,
    "helmet": "Knight's Helmet",
    "helmet_rating": 5,
    "has_shield": False,
    "shield": "none",
    "shield_rating": 0,
    "has_breastplate": True,
    "breastplate": "Knight's Breastplate",
    "breastplate_rating": 5,
    "has_boots": True,
    "boots": "Knight's Boots",
    "boots_rating": 5,
    "has_gloves": True,
    "gloves": "Knight's Gloves",
    "gloves_rating": 5,
    "has_pants": True,
    "pants": "Knight's Pants",
    "pants_rating": 5
}


def calculate_armour(armour):
    # gets the rating of all the 'pieces' of armour and sums them up to get a total
    pieces = [
        "helmet_rating",
        "shield_rating",
        "breastplate_rating",
        "boots_rating",
        "gloves_rating",
        "pants_rating"
    ]

    armour["rating"] = sum(armour.get(piece, 0) for piece in pieces)


def calculate_weapon(weapon):
    pieces = [
        "base_damage",
        "weapon_damage"
    ]

    weapon["total_damage"] = sum(weapon.get(piece, 0) for piece in pieces)


def fight(player, weapon, enemy_name, enemy_health, enemy_attack):
    while enemy_health > 0:
        choice1 = input(enemy_name + " stands before you, do you wish to attack? (y/n): ")

        if (choice1 == "y"):
            calculate_weapon(weapon)
            enemy_health -= weapon["total_damage"]
            print(enemy_health)
        elif (choice1 == "n"):
            player["health"] -= enemy_attack
            print(player["health"])
        else:
            print("Invalid input")



fight(player, weapon, "Goblin", 111, 5)