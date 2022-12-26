import webbrowser
from googlesearch import search
import os
os.system('cls')

keyword = input("What do you wanna search on google? \n")

links = []

for i in search(keyword, tld="com", num=5, stop=5, pause=5):
    links.append(i)

for i, a in enumerate(links): #a = link, i = index
    print("\n\n #"+str(i+1), a)

link = int(input("\n\nWhich do you want to open? (1,2,3,4,5)\n"))
webbrowser.open(links[link-1])

