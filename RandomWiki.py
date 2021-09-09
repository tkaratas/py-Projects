"""I found class bcolors on stackoverflow."""

import requests
from bs4 import BeautifulSoup
import webbrowser


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


while True:
    url = 'https://www.wikipedia.org/wiki/Special:Random'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.find(id="firstHeading").text
    show = input(
        "Title: " + bcolors.OKGREEN + title + bcolors.ENDC + "\nDid you read this article?" + "\nDo you want to read this article? (yes or no)\n>").lower()
    if "y" in show:

        url2 = 'https://www.wikipedia.org/wiki/' + \
            soup.find(id="firstHeading").text
        webbrowser.open(url2)
        break
    elif "n" in show:
        break
    else:
        print("Invalid input!")
        continue
