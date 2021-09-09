print("\nEvery morning before washing your __(NOUN)__, massage it \ngently with a/an __(NOUN)__ "
      "that has been soaked overnight \nin an __(CONTAINER)__ full of warm __(LIQUID)__.\n")

noun = input("Type a Noun: ")
noun2 = input("Type your 2. Noun: ")
container = input("Type your Container: ")
liquid = input("Type your Liquid: ")

print("\nEvery morning before washing your {0}, massage it \ngently with a/an {1} that has been soaked overnight \nin an {2} full of warm {3}.\n"
      .format(noun, noun2, container, liquid))
