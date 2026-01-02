import random

weapons = {
    "excalibur": {
        "name": "Excalibur",
        "base_damage": 11,
        "total_damage": 0,
        "modifiers": {
            "goblin": 1.3,
            "ogre": 0.8
        },
        "flavor_lines": [
            "✨ Excalibur hums with ancient power",
            "⚔️ The blade gleams as it strikes",
            "🌟 The legendary sword pulses with divine energy"
        ]
    },
    "dragonslayer": {
        "name": "Dragon Slayer",
        "base_damage": 13,
        "total_damage": 0,
        "modifiers": {
            "goblin": 1.1,
            "ogre": 1.2
        },
        "flavor_lines": [
            "🔥 The Dragon Slayer burns with righteous fury",
            "⚡ Lightning crackles along the blade's edge",
            "🐉 The weapon thirsts for draconic blood"
        ]
    },
    "frostbite": {
        "name": "Frostbite",
        "base_damage": 10,
        "total_damage": 0,
        "modifiers": {
            "goblin": 1.4,
            "ogre": 0.9
        },
        "flavor_lines": [
            "❄️ Frostbite leaves a trail of ice in the air",
            "🧊 The blade freezes everything it touches",
            "🌨️ A blizzard follows your strike"
        ]
    },
    "shadowblade": {
        "name": "Shadow Blade",
        "base_damage": 12,
        "total_damage": 0,
        "modifiers": {
            "goblin": 1.5,
            "ogre": 1.0
        },
        "flavor_lines": [
            "🌑 The Shadow Blade phases through reality",
            "💀 Darkness clings to your weapon",
            "👻 Spectral whispers echo with each strike"
        ]
    },
    "thunderstrike": {
        "name": "Thunderstrike",
        "base_damage": 14,
        "total_damage": 0,
        "modifiers": {
            "goblin": 1.0,
            "ogre": 1.3
        },
        "flavor_lines": [
            "⚡ Thunderstrike crackles with raw power",
            "🌩️ The sound of thunder accompanies your blow",
            "💥 Lightning arcs from the weapon"
        ]
    }
}

def calculate_weapon(weapon):
    roll = random.randint(1, 6)
    weapon["total_damage"] = weapon["base_damage"] + roll
