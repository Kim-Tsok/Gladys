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


input("Press Enter to start the game...")
print(" ")
# Start a game
input("Unknown: What is your motivation for all of this, why do you do this? All this for what? All this pain and suffering? ")
input("Make it easier on yourself, just give up. ")
input("Give up on this stupid dream of trying to beat me, you and your stupid team of dancing ponies. ")
input("")
input("person01: Hey wake up! wakeup you idiot. ")
input ("You: What happened? ")
input("person01: You were shaking and mumbling something in your sleep. ")
input("You: I had a dream. ")
input("person01: You saw him again, didn't you? ")
input("You: It was terrifying, last time this happened was when it first appeared. ")
choice = input("person01: Well since we're having a convo, why don't we just spar cause we're weirdos. You up for it? (y/n) ")
if(choice == "y"):
    weapon = weapons["excalibur"].copy()
    fight(player, weapon, armour, enemies["goblin"])
elif(choice == "n"):
    input("You're still gonna fight again. ")
    weapon = weapons["excalibur"].copy()
    fight(player, weapon, armour, enemies["goblin"])
else:
    input("Not an option idiot: ")
    choice = input("person01: Well since we're having a convo, why don't we just spar cause we're weirdos. You up for it? (y/n) ")

print(f"Welcome here, {player['gender']}!")
weapon = weapons["excalibur"].copy()
fight(player, weapon, armour, enemies["goblin"])
input("You have defeated the goblin! Now you must face the ogre! ")
fight(player, weapon, armour, enemies["ogre"])
