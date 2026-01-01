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