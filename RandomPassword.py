import string
import random

path = "path/for/txt-file"  # CHANGE IT
charackters = list(string.ascii_letters + string.digits + "!@#+$%&*")

print("""
1. Create a Password
2. Forget Your Password?
""")

a = int(input("1 or 2: "))
if a == 1:
    key = input("Enter a Keyword to remember your Password: ")
    length = int(input("Enter Password Length: "))
    random.shuffle(charackters)
    password = ""
    for i in range(length):
        password += str(random.choice(charackters))
    with open(path, 'a') as file:
        file.write(key+": "+password+"\n")
    print(password)
    print(len(password))

elif a == 2:
    key = input("Enter Your key:")
    with open(path, 'r') as file:
        content = file.readlines()
        keyFound = False
        for line in content:
            index = line.find(':')
            found = line[:index]
            if key == found:
                keyFound = True
                if keyFound:
                    print(line.rstrip())
        if not keyFound:
            raise NameError('KeyWord Not Found.')

else:
    raise NameError('Invalid Input')
