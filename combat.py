import random
from weapons import calculate_weapon
from armour import calculate_armour

def fight(player, weapon, armour, enemy):
    enemy = enemy.copy()

    enemy_name = enemy["name"]
    enemy_health = enemy["health"]
    enemy_attack = enemy["attack"]

    max_enemy_health = enemy_health
    max_player_health = player["health"]
    turn = 1

    print("\n" + "=" * 50)
    print(f"BATTLE BEGINS! {enemy_name}")
    print("=" * 50)

    while enemy_health > 0 and player["health"] > 0:
        print(f"\n--- Turn {turn} ---")
        print(f"{enemy_name}: {enemy_health}/{max_enemy_health} HP")
        print(f"You: {player['health']}/{max_player_health} HP")

        if player.get("status") == "stunned":
            print("You are stunned and miss your turn!")
            player["status"] = None
        else:
            choice = input("(a)ttack, (d)efend, (r)un: ").lower().strip()

            if choice in ("a", "attack"):
                calculate_weapon(weapon)
                base_damage = weapon["total_damage"]

                modifier = weapon.get("modifiers", {}).get(
                    enemy_name.lower(), 1.0
                )
                damage = int(base_damage * modifier)

                if modifier != 1.0:
                    print("Your weapon reacts to this foe!")

                crit_chance = player["mystery_stat"] * 2
                if random.randint(1, 100) <= crit_chance:
                    damage = int(damage * 1.5)
                    print("🔥 CRITICAL HIT!")

                damage = max(1, damage - enemy.get("armor", 0))
                enemy_health -= damage

                print(random.choice(weapon["flavor_lines"]))
                print(f"You deal {damage} damage to {enemy_name}!")

            elif choice in ("d", "defend"):
                print("You brace for impact!")
            elif choice in ("r", "run"):
                if random.randint(1, 100) <= player["mystery_stat"] * 5:
                    print("You escape successfully!")
                    return True
                else:
                    print("Failed escape!")
            else:
                print("Invalid action.")
                continue

        if enemy_health <= 0:
            print(f"\nYou defeated the {enemy_name}!")
            return True

        print(random.choice(enemy["dialogue"]))
        enemy_damage = enemy_attack

        calculate_armour(armour)
        reduction = armour["rating"] // 3
        actual_damage = max(1, enemy_damage - reduction)
        player["health"] -= actual_damage

        print(f"{enemy_name} deals {actual_damage} damage!")

        for move in enemy.get("special_moves", []):
            if random.random() < move["chance"]:
                print(f"{move['line']}")
                if "bonus_damage" in move:
                    player["health"] -= move["bonus_damage"]
                if "status" in move:
                    player["status"] = move["status"]

        if player["health"] <= 0:
            print("\nYOU DIED")
            return False

        turn += 1
