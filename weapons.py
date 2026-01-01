weapon = {
    "total_damage": 1,
    "base_damage": 2,
    "has_weapon": True,
    "current_weapon": "Dagger",
    "weapon_damage": 9,
}

def calculate_weapon(weapon):
    pieces = [
        "base_damage",
        "weapon_damage"
    ]

    weapon["total_damage"] = sum(weapon.get(piece, 0) for piece in pieces)