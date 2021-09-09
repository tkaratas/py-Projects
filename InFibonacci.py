import math


def perfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x


def isFibonacci(n):
    return perfectSquare(5*n*n+4) or perfectSquare(5*n*n-4)


number = int(input("Number: "))

if isFibonacci(number):
    print(number, "is a Fiboncci Number.")
else:
    print(number, "is not a Fibonacci Number.")
