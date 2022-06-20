#program to get song lyrics from azlyrics.com

import requests
import string
import string
from bs4 import BeautifulSoup

special = string.punctuation + ' '

#getting website address

artist = input("Enter the band/artist name: ")
song = input("Enter the song name: ")

for char in special:
    artist = artist.replace(char, '')
    song = song.replace(char, '')

root = "https://www.azlyrics.com/lyrics/"

URL = root + artist.lower() + '/' + song.lower() + '.html'

#getting content from address

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

body = soup.find("div", class_="col-xs-12 col-lg-8 text-center")

lyrics = body.text.strip()

fileName = song.lower() +'.txt'

skip = 'Submit Corrections'
is_skipped = False

#creating file with lyrics (all content until 'submit corrections')

with open(fileName, 'w') as file:
    file.write(URL + '\n \n')
    for line in lyrics:
        if 'submit corrections' in line.lower():
            is_skipped = True
            
        else:
            file.write(line )

with open(fileName,"r+") as f:
    new_f = f.readlines()
    f.seek(0)
    for line in new_f:
        if "submit correction" not in line.lower():
            f.write(line)
        else:
            break
    f.truncate()
