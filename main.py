import random
import json
import time
import os.path



classes = json.load(open("classes.json", "r"))

class Character:
    def __init__(self, name, weapon, health, damage):
        self.name = name
        self.weapon = weapon
        self.health = health
        self.damage = damage
    def save(self):
        file = open("character.json", "w")
        file.write(json.dumps(self.__dict__))
        file.close()

print("Start of game. Thank you Xaa for contributing to bug testing.")
time.sleep(0.5)
print("Checking for previous save...")
time.sleep(0.856)
new = input("Load a previous save? [Y] [N] | ")
if new == "N" or new == "n":
    name = input("Hello, distant traveller. What is your name? | ") # Input: Name
    if name == "Admin": # Admin login
        admpass = input("Password? ")
        if admpass == "123321": # Admin Password
            name = "Admin"
        else:
            name = "Fake Admin" # Fake Admin
            quit()
    print(f"Hello, {name}, This adventure was made by yngryzen, and will hold many trials.")
    time.sleep(3),
    print("You will go through tedious tasks and traps, however you are given an option.")
    time.sleep(3),
    print("You must choose a class between Knight, Barbarian, Prisoner or  Priest. You will be able to get new ones later.")
    time.sleep(4),
    characterclass = input("Now, you must choose between Knight, Barbarian, Prisoner or Priest | ")
    if characterclass == ("Knight") or characterclass == ("Barbarian") or characterclass == ("Prisoner") or characterclass == ("Priest"): # Input: Class
        print("Great.")
    else:
        print("You did not take this opportunity accordingly.. Given Peasant class.")
        characterclass = "Peasant" # Class: Peasant
        wtc = input("Do you wish to continue? [Y] [N] | ")
        if wtc == "Y" or wtc == "y":
            print("Okay.")
        else:
            quit()
    print(f"You have set your class to: {characterclass}")
    for cclass in classes:
        if cclass["Class"] == characterclass:
            character = Character(name, cclass["Weapon"], cclass["Health"], cclass["Damage"])
            character.save()
else:
    if os.path.isfile("character.json"):
        characterdata = json.load(open("character.json", "r"))
        character = Character(characterdata["name"], characterdata["weapon"], characterdata["health"], characterdata["damage"])
        print(f"Data saved. {character.name}")
        time.sleep(5)
    else:
        print("You don't have a save.")
        quit()
# --------------------------------  INTRODUCTION END -------------------------------- #
print(f"Welcome, {character.name}. You were chosen to take part on a trip to the Everglade forest.")
time.sleep(3)
print("It will be very tough, but you will make it.")
time.sleep(1)
print("Throughout this journey, you will be given Items, these will not be saved if you wish to stop.")
time.sleep(3)
print("Choose a starting item to begin.")
time.sleep(1)
print("> You enter a tavern, with broken walls and little to show.")
time.sleep(1)
print("Hello. I am the owner of this lowly shop. What may I do for you?")
time.sleep(1)
sitem = input("He puts 2 things on the desk. A knife and a Bandage. Which do you grab? [Knife] [Bandages] | ") # Item selection
if sitem == "Knife" or sitem == "Bandages":
    print(f"You have chosen the {sitem}.")
else:
    print("Something went wrong.")
time.sleep(1)
print("Thank you for your patronage, traveller.")
time.sleep(1)
print(f"> You leave the shop with your {sitem} and go towards the forest.")
time.sleep(1.5)
print(f"As you enter, you hear something whispers '{character.name}'.")
time.sleep(4)
if sitem == "Knife":
    print("You pull out your knife and point it towards the voice.")
    time.sleep(1)
    print("You hear running away. Phew.")
    task1 = "K"
else: 
    task1 = input("What will you do? [R] Run Away [F] Fight Back? | ")
if task1 == "R":
        print("You are not cut out for this adventure.")
        quit()
else: 
    print("Rolling 1,10 to see if you survive.")
    roll = random.randint(1, character.damage)
    print(roll)
    if roll == 1:
        print("You died to the wandering ghost. Character save deleted.")
        os.remove("character.json")
        quit()
    else:
        print("As you moved you realised it was the wind.")
if task1 == "K":
    print("Oh well.")
time.sleep(2)
print("> Congrats on getting it this far.")
time.sleep(1)
print("You enter the generic forest until you see a campfire.")
time.sleep(1)
if character.damage > 15:
    task2 = input("What would you like to do? [M] Massacre them [R] Run away | ")
    if task2 == "M":
        print("> I like that. +5 health")
        character.health + 5
        print(character.name, " Your new health is: ", character.health)
else:
    print("You are too weak for them. You Run.")
time.sleep(2)
print("You come across a sign.")
randomsign = random.randint(1, character.health)
if randomsign < 5:
    print("It says, Left is Death. Right is Fight.")
    time.sleep(3)
    print("> Finally, A truthful sign.")
else:
    print("It says Right is Death, Left is Life.")
    time.sleep(3)
    print("> That is a lie. ")
randomsignpath = input("> What path do you choose? [L] Left [R] Right | ")
if randomsignpath == "L":
    print("> I'm here to help. ")
    time.sleep(2)
    print("??? has smited you. Data save deleted.")
    os.remove("character.json")
else:
    print("> Good... ")
    time.sleep(3)
    print("As you walk, it seems peaceful. It is harmony.")
time.sleep(5)
print("You walk for seconds.")
time.sleep(1)
print("You walk for hours")
time.sleep(5)
print("You walk for days.")
time.sleep(10)
print("You are starving. You see a kingdom in the distance. You use your last might to go towards it.")
time.sleep(2)
print("> Goblins incoming.")
time.sleep(2)
print("You ignore the voice, and continue forward due to hunger.")
time.sleep(3)
task3 = input("> QUICK, ATTACK THEM. YOU ARE STRONG ENOUGH. [A] Attack them [F] Flee | ")
if task3 == "A":
    print("Rolling if you survive, goblins need 6 damage to kill.")
    task3r = random.randint(1, character.damage)
    if task3r > 6:
        print("You survived and killed the goblin, but at a cost.")
        print("> -25 health.")
        character.health - 25
        print(f"{character.name}, you have {character.health} remaining.")
    else:
        print("You have died to the goblins. Save deleted")
        os.remove("character.json")
        print(f"> Details: {task3} out of {character.damage} (You needed more than 6)")
else:
    print("You narrowly escape.")
time.sleep(2)
print("You enter the kingdom.")
time.sleep(5)
print("'That's weird',  you say to yourself. 'There's no security.'")
time.sleep(1)
print("GOD REST YE MERRY GENTLEMAN \n LET NOTHING YOU DISMAY \n REMEMBER CHRIST OUR SAVIOUR \n WAS BORN ON CHRISTMAS DAY")
time.sleep(4)
print("> Okay. I'm going to give you an option to save your character.")
save1 = input("Save? [Y] [N] | ")
if save1 == "Y":
    character.save()
else:
    print("> Brave choice. +15 health")
    character.health + 15
task4 = input("You see a Dragon in the palace instead of people. What do you do? [S] Sneak around [F] Fight")
if task4 == "S":
    print("You sneak around.")
    time.sleep(1)
    print("> What did you hope to find?")
    time.sleep(4)
    print("You sneak around and see a chain attached to the dragons leg.")
    finaldecider = True
    time.sleep(4)
else:
    print("You choose to fight.")
    time.sleep(3)
    print("> Wise choice.")
finaltask = input("What do you do? [F] Strike it now [S] Steal the gold")
time.sleep(5)
print("> I like your bravery.")
if finaltask == "F":
    print("You need 100 health and 15 damage to succeed.")
    time.sleep(5)
    if sitem == "Knife":
        print("Knife has added 15 damage points.")
        character.damage + 15
    else: print("No knife")
    if character.weapon == "Holy Magic":
        print("Holy magic is effective against dragons. + 20 damage")
    else: print("No magic")
    if sitem == "Bandages":
        print("Added health from bandages. + 50")
        character.health + 50
    else: print("No bandages.")
    print(f"You attempt to fight the dragon (Current stats: Damage{character.damage} Health:{character.health})")
    if character.damage >= 100 & character.health >= 15:
        print("Welldone. You have slayed the dragon.")
        print("Manually exit.")
        os.remove("character.json")
        time.sleep(10000000)
    else:
        print("> You are not worthy enough.")
        time.sleep(10)
        print("The dragon has digested you.")
        print("> Thanks for the meal.")
        print("Leave manually.")
        os.remove("character.json")
        time.sleep(10000000)
else:
    print("You steal the gold")
    time.sleep(5)
    print("> Do you know?")
    if finaldecider == True:
        print("> You figured out I was chained??")
        time.sleep(5)
        print("You stole gold and ran away before he could melt the place.")
        time.sleep(5)
        print("Welldone, hero.")
        time.sleep(5)
        print(f"Thank you for playing {character.name}. Your stats have been deleted and we appreciate you taking the time to play. \n If you have any suggestions, add yngryzen on discord.")
        os.remove ("character.json")
    else:
        print("You run towards the dragon, whos jaws clamp down on you and you split in half.")
        time.sleep(5)
        print("> Close call.")
        print(f"Thank you for playing {character.name}. Your stats have been deleted and we appreciate you taking the time to play. \n If you have any suggestions, add yngryzen on discord.")
        os.remove("character.json")
print("Manually close.")
time.sleep(10000000)