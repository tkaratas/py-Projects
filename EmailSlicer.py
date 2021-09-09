email = input("Enter Your Email: ").strip()

name = email[:email.index('@')]
domain = email[email.index('@')+1:]

print("Your username is {} & domain is {}".format(name, domain))
