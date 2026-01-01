import random
from weapons import calculate_weapon
from armour import calculate_armour


def fight(player, weapon, armour, enemy_name, enemy_health, enemy_attack):
    
    max_enemy_health = enemy_health
    max_player_health = player["health"]
    turn = 1
    
    print(f"\n{'='*50}")
    print(f"BATTLE BEGINS!")
    print(f"{'='*50}")
    print(f"Enemy: {enemy_name}")
    print(f"Enemy Health: {enemy_health}/{max_enemy_health}")
    print(f"Your Health: {player['health']}/{max_player_health}")
    print(f"{'='*50}\n")
    
    while enemy_health > 0 and player["health"] > 0:
        print(f"\n--- Turn {turn} ---")
        print(f"{enemy_name}: {enemy_health}/{max_enemy_health} HP")
        print(f"Your Health: {player['health']}/{max_player_health} HP")
        
        # Player's turn
        print("\nWhat would you like to do?")
        choice = input("(a)ttack, (d)efend, (r)un: ").lower().strip()
        
        if choice == "a" or choice == "attack":
            # Calculate damage with potential critical hit
            calculate_weapon(weapon)
            base_damage = weapon["total_damage"]
            
            # Critical hit chance based on mystery_stat
            crit_chance = player["mystery_stat"] * 2  # 10-18% chance
            is_critical = random.randint(1, 100) <= crit_chance
            
            if is_critical:
                damage = int(base_damage * 1.5)
                print(f"CRITICAL HIT! You deal {damage} damage to {enemy_name}!")
            else:
                damage = base_damage
                print(f"You attack {enemy_name} for {damage} damage!")
            
            enemy_health -= damage
            
            if enemy_health <= 0:
                enemy_health = 0
                print(f"\nVICTORY! You have defeated {enemy_name}!")
                print(f"Your remaining health: {player['health']}/{max_player_health}")
                break
            
            # Enemy counter-attacks
            print(f"\n{enemy_name} counter-attacks!")
            enemy_damage = enemy_attack
            
            # Armor reduces damage
            calculate_armour(armour)
            damage_reduction = armour["rating"] // 3  # Armor reduces damage by rating/3
            actual_damage = max(1, enemy_damage - damage_reduction)
            
            player["health"] -= actual_damage
            if damage_reduction > 0:
                print(f"Your armor absorbs {damage_reduction} damage!")
            print(f"{enemy_name} deals {actual_damage} damage to you!")
            
        elif choice == "d" or choice == "defend":
            # Defending reduces incoming damage significantly
            print(f"You take a defensive stance!")
            
            # Enemy attacks
            enemy_damage = enemy_attack
            calculate_armour(armour)
            damage_reduction = (armour["rating"] // 2) + (enemy_damage // 2)  # Extra reduction when defending
            actual_damage = max(1, enemy_damage - damage_reduction)
            
            player["health"] -= actual_damage
            print(f"Your defense and armor reduce damage by {damage_reduction}!")
            print(f"{enemy_name} deals {actual_damage} damage to you!")
            
        elif choice == "r" or choice == "run":
            # Chance to escape based on mystery_stat
            escape_chance = player["mystery_stat"] * 5  # 25-45% chance
            if random.randint(1, 100) <= escape_chance:
                print(f"You successfully escape from {enemy_name}!")
                return True  # Escaped successfully
            else:
                print(f"You failed to escape! {enemy_name} attacks you!")
                enemy_damage = enemy_attack
                calculate_armour(armour)
                damage_reduction = armour["rating"] // 3
                actual_damage = max(1, enemy_damage - damage_reduction)
                player["health"] -= actual_damage
                if damage_reduction > 0:
                    print(f"🛡️  Your armor absorbs {damage_reduction} damage!")
                print(f"💔 {enemy_name} deals {actual_damage} damage to you!")
        else:
            print("Invalid input! Please choose (a)ttack, (d)efend, or (r)un.")
            continue
        
        # Check if player died
        if player["health"] <= 0:
            player["health"] = 0
            print(f"\nDEFEAT! {enemy_name} has defeated you!")
            print(f"Game Over...")
            return False
        
        turn += 1
    
    return True  # Player won
