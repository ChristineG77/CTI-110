# CTI 110 
# P3T1
# Gilbert
# 9/22/2026 
# Warmup with IF statements

#main() is the programs starting point
# You don't need to use it, but its good and useful

def main():
#part 1 level checking
    print("Hello and welcome to the dungeon.")
    level = int(input("What level are you? "))
    if level >= 21:
        print("You can enter the dungeon!")
    else:
        print("Try leveling up more first")
        

#part 2 - list your potions
    print("If you have potions in the two slots avaliable to you, please enter them here or enter None.")
    P1 = str(input("Please enter the potion name in your first slot: "))
    P2 = str(input("Please enter the potion name in your second slot: "))
    if P1 != "None":
        #put nested loop to check for numbers in the the name slot
        print("You have",P1,"in your first potion slot!")
    else:
        print("You have no potions in this slot") 
    if P2 != "None":
        print("You have",P2,"in your second potion slot!")
    else:
        print("You have no potions in this slot") 
#Ask how many potions you have
    print("Time to enter the dungeon!")
    potions = int(input("How many health potions did you bring? "))
    if potions == 0:
        print("Its too dangerous to go alone without potions!")
    elif potions == 1:
        print(f"You have {potions} health potion.")
    elif potions >= 1:
        print(f"You have {potions} health potions.")
    else:
        print(f"How did you get {potions} health potions? Its less than zero!")

#part 3, boss battle
    print("You have entered the boss room! The Orge turns to look at your puny stature and raises its club!")
    print("Good luck!")
    if level >=25:
        if potions > 3:
            print("It takes three potions to survive the battle!")
            print("**You will WIN!**")
        else:
            print("You run out of healing before he dies.")
            print("**You have LOST**")
    else:
        print("His armor is too tough for your to strike through")
        print("You have lost!")
        print("**GAMEOVER**")
# at the bottom -- start the program
main()