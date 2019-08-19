# import libraries
# import csv
import json
import os
import urllib.request

from bs4 import BeautifulSoup

# specify the url
toscrape_page = 'https://www.verkadefabriek.nl/programma/'

# query the website and return the html to the variable ‘page’
page = urllib.request.urlopen(toscrape_page)

# webpagina wordt in de soup gegooid
soup = BeautifulSoup(page, 'html.parser')

# unused
inSection = True

# Eerst in een array zetten
AlleShows = []

# groffe filter
for item in soup.find_all('span'):
    #    if (item.get('id') == 'MainContent_ProgramsRepeater_pnlBg_0'):
    #       inSection = True
    cl = item.get('class')
    if type(cl) is list:
        hasTextWrap = False
        hasP15 = False
        for c in cl:
            if c == 'text-wrap':
                hasTextWrap = True
            # het gaat om span's met class='p15' waarbij de spans met class='text-wrap' moeten worden uitgesloten
            if c == 'p15' and len(item.get_text().strip()) > 0 and inSection:
                hasP15 = True

        if not hasTextWrap and hasP15:
            aShow = item.get_text().strip().replace('\n', ';').split(';')
            AlleShows.append(aShow)

# array van array omzetten naar array van dict's
showsArrOfDicts = []
import datetime

for show in AlleShows:
    if show[1] == 'vandaag':
        today = datetime.date.today()
        show[1] = today.strftime("%d %B")
    if show[1] == 'morgen':
        tm = datetime.date.today() + datetime.timedelta(days=1)
        show[1] = tm.strftime("%d %B")

    thisdict = {'tijd': show[0], 'dag': show[1], 'naam': show[2], 'type': show[3]}
    showsArrOfDicts.append(thisdict)

myFile = 'show_json.json'
if os.path.exists(myFile):
    os.remove(myFile)
# json dump van de shows
with open(myFile, 'a') as write_file:
    write_file.write('[')
    cnt = 1
    # vervolgens iedere dict json dumpen en wrappen in een array
    for ds in showsArrOfDicts:
        json.dump(ds, write_file)
        if cnt < len(showsArrOfDicts):
            write_file.write(',')
        cnt += 1
    write_file.write(']')

# ftp naar itstudy.eu, de login gaat automatisch naar de juiste dir itstudy.eu/zaalwacht
import ftplib

import localvar

# maximale grootte vergroten/begrenzen
ftplib.FTP.maxline = 65536
ftp = ftplib.FTP(localvar.h)
ftp.login(localvar.un, localvar.ww)

with open(myFile, 'rb') as ftpup:
    ftp.storbinary('STOR ' + myFile, ftpup)
    ftp.close()
