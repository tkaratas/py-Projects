def leapOrNot(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


year = int(input("Year: "))

result = leapOrNot(year)

if result == True:
    print("{} is a leap year".format(year))
else:
    print("{} is a common year".format(year))
