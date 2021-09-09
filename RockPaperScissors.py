"""Rock Paper Scissors"""
import random


move = ["Rock", "Paper", "Scissors"]


def ai_choose():
    ai_r = random.randint(0, 2)
    ai = move[ai_r]
    return ai


def choose():
    print("Choose Your Move!")
    print("1) Rock\n2) Paper\n3) Scissors")
    you_c = int(input(">"))
    if you_c == 1:
        you = move[0]
        return you

    elif you_c == 2:
        you = move[1]
        return you
    elif you_c == 3:
        you = move[2]
        return you
    else:
        print("Unvalid number")
        return choose()


def win(you, ai):
    if (you == "Rock" and ai == "Scissors") or (you == "Scissor" and ai == "Paper") or (you == "Paper" and ai == "Rock"):
        print("You won!")
    elif (ai == "Rock" and you == "Scissors") or (ai == "Scissor" and you == "Paper") or (ai == "Paper" and you == "Rock"):
        print("You Lost!")
    else:
        print("Draw!")


def play():
    ai = ai_choose()
    you = choose()
    print("You:", you, "AI:", ai)
    win(you, ai)
    playAgain()


def playAgain():
    print("Do you want to play again? (y or n)")
    answer = input(">").lower()
    if "y" in answer:
        play()
    elif "n" in answer:
        print("See You Again!")
        exit()
    else:
        print("What?")
        playAgain()


while True:
    play()
