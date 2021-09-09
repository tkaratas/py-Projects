import random

"""
 _____
|     |
|  *  |
|_____|
 _____
|*    |
|    *|
|_____|

 _____
|*   *|
|  *  |
|_____|

 _____
|*   *|
|*   *|
|_____|

 _____
|* * *|
|*   *|
|_____|

 _____
|* * *|
|* * *|
|_____|

"""

one = """ _____\n|     |\n|  *  |\n|_____|\n"""
two = """ _____\n|*    |\n|    *|\n|_____|\n"""
three = """ _____\n|*   *|\n|  *  |\n|_____|\n"""
four = """ _____\n|*   *|\n|*   *|\n|_____|\n"""
five = """ _____\n|* * *|\n|*   *|\n|_____|\n"""
six = """ _____\n|* * *|\n|* * *|\n|_____|\n"""

number1 = random.randint(1,6)
number2 = random.randint(1,6)

if number1 == 1:
    print(one,end="")
elif number1 == 2:
    print(two,end="")
elif number1 == 3:
    print(three,end="")
elif number1 == 4:
    print(four,end="")
elif number1 == 5:
    print(five,end="")
else:
    print(six,end="")

if number2 == 1:
    print(one,end="")
elif number2 == 2:
    print(two,end="")
elif number2 == 3:
    print(three,end="")
elif number2 == 4:
    print(four,end="")
elif number2 == 5:
    print(five,end="")
else:
    print(six,end="")