import random

number = random.randint(1,100)
chances = 3

while True:
    print("To quit type 0. You have 3 chances")
    if(chances == 0):
        print("You couldn't find the number. Number was ",number)
        break
    guess = int(input("Type an integer: "))

    if (guess == 0):
        break 
    elif (number == guess):
        print("You found the number.\nNumber=",number)
        break
    elif(number > guess):
        print("number is greater than ",guess)
        chances -= 1
        print("Try again. Remaining chance(s)=",chances)
    elif(number < guess):
        print("number is less than ",guess)
        chances -= 1
        print("Try again. Remaining chance(s)=",chances)
    