print("""Welcome to Text Based Adventure Game\n""")


def bear_room():
    print("\nThere is a bear here.\nBehind the bear is another door. The bear is eating atasty honey!\What would you do?(1 or 2)")
    print("1) Take the honey.")
    print("2) Taunt the bear.")

    answer = input(">")

    if "1" == answer:
        game_over("The bear killed you.")
    elif "2" == answer:
        print("\nYour good time, the bear moved from the door. You can go through it now!")
        diamond_room()
    else:
        game_over("\nDon't you know how to type a number?\n")
def monster_room():
    print("\nThere is a monster.\nBehind the monster is another door. The monster is sleeping. What would you do now?(1 or 2)")
    print("1)Go through the door silently.")
    print("2)Kill the monster and show your courage.")

    answer = input(">")

    if "1" == answer:
        diamond_room()
    elif "2" == answer:
        game_over("The monster was hungry, it ate you.")
    else:
        game_over("\nGo and learn how to type a number\n")

def diamond_room():
    print("\n You are now in a room filled with diamonds!\nAnd there is a door to!\What would you do? (1 or 2)")
    print("1) Take some diamonds and go through the door.")
    print("2) Just go through the door.")

    answer = input(">")

    if answer == 1:
        game_over("They were cursed diamonds! The moment you touched it, the building collapsed, and you die")
    elif answer == 2:
        print("\nNice, You are an honest man! Congrats you win the game!")
        play_again()
    else:
        game_over("Go and learn how to type!")
    


def game_over(reason):
    print("\n", reason)
    print("Game Over!")
    play_again()

def play_again():
    print("Do you want to play again?(y or n)")

    answer = input(">").lower()

    if "y" in answer:
        start()
    else:
        exit()

def start():
    print("\nYou are in a dark room.\nThere are two doors (left and right), which one do you take (l or r)?\n")
    answer = input(">").lower()

    if "l" in answer:
        bear_room()
    
    elif "r" in answer:
        monster_room()
    
    else:
        game_over("\nDon't you know how to type something properly?\n")


start()