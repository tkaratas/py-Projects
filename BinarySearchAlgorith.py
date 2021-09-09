import random
searchlist = []

for i in range(0, 100):
    x = random.randint(1, 100)
    searchlist.append(x)
searchlist.sort()
print(searchlist)

search = int(input("Enter your number: "))


def binarySearch(search, start, end, searchlist):
    if end >= start:
        mid = (end+start) // 2

        if searchlist[mid] == search:
            return mid
        elif searchlist[mid] < search:
            return binarySearch(search, mid+1, end, searchlist)
        else:
            return binarySearch(search, start, mid-1, searchlist)
    else:
        return "Cannot Found"


result = binarySearch(search, 0, len(searchlist)-1, searchlist)
print("Result: ", result)
