"""I did not code this game all by myself. I needed help with printing the blanks (line 100-101) and hangman list"""

import random
import time

print("Welcome To Hangman Game!\n")
print("Rules: You have 6 chance to guess a letter.\nIf you ran out of your chances game over.\nIf you guess the word you won.")

wordList = ["january", "border", "image", "film", "promise",
            "kids", "lungs", "doll", "rhyme", "damage", "plants"]


def hangMan(chances):
    hangman = ["""
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   """,
               """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """,
               """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """,
               """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """,
               """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
               """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
               """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """
               ]
    return hangman[chances]


def start(chances):
    word = wordList[random.randint(0, len(wordList)-1)]
    alreadyTried = []
    length = len(word)
    alreadyGuessed = []
    blanks = "_" * length
    print("Word Length: ", length)

    hangMan(chances)

    while True:
        if chances == 0:
            playAgain("You have no chance remaining. Game Over!")

        else:
            print("Remaining Chances: ", chances)
            guess = input(">").lower()
            if guess in alreadyGuessed:
                print("You guessed this letter already. Try another letter!")
            elif guess in word:
                alreadyGuessed.append(guess)
                for i in range(0, len(word)):
                    if guess == word[i]:
                        blanks = blanks[:i] + guess + blanks[i+1:]
                print(blanks)
                if blanks == word:
                    playAgain(
                        "You guessed the word correctly! Congratulations, you won the game!")
            elif guess not in word:
                if guess in alreadyTried:
                    print("You tried this letter. Try another one!")
                    print(hangMan(chances))
                else:
                    alreadyTried.append(guess)
                    chances -= 1
                    print(hangMan(chances))


def gameOver():
    print("See you again!")
    exit()


def playAgain(reason):
    print(reason)
    print("Do you want to play again? (y or n)")
    answer = input(">").lower()
    if "y" in answer:
        start(6)
    elif "n" in answer:
        gameOver()


start(6)
