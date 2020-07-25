import json
import os
import urllib.request
# ftp naar de remote omgeving
import ftplib
import localvar
from bs4 import BeautifulSoup
import datetime




# specify the url
toscrape_page = localvar.s

# query the website and return the html to the variable ‘page’
page = urllib.request.urlopen(toscrape_page)

# webpagina wordt in de soup gegooid
soup = BeautifulSoup(page, 'html.parser')
xtra = ''
AlleShows = []
for item in soup.find_all('div'):
    if type(item.get('class')) is list and 'agendeDetailContainer' in item.get('class'):
        # eerste de basisgegevens opzoeken
        for it in item.find_all('span'):
            if type(it.get('class')) is list and 'p15' in it.get('class'):
                aShow = it.get_text().strip().replace('\n', ';').split(';')
        #vervolgens in een ander stuk de link en en/og het uitverkocht is
        for it2 in item.find_all('a'):
            if type(it2.get('class')) is list and 'infoLink' in it2.get('class'):
                href = it2.get('href')
            if type(it2.get('class')) is list and 'ticketAT' in it2.get('class') and 'soldout' in it2.get('class'):
                xtra = [it2.get('href').split('=')[1], href,  'soldout']
            else:
                if 'ticketAT' in it2.get('class'):
                    xtra = [it2.get('href').split('=')[1], href,  '']
        newShow = aShow + xtra
        AlleShows.append(newShow)
# array van array omzetten naar array van dict's
showsArrOfDicts = []

for show in AlleShows:
    if show[1] == 'vandaag':
        today = datetime.date.today()
        show[1] = today.strftime("%d %B")
    if show[1] == 'morgen':
        tm = datetime.date.today() + datetime.timedelta(days=1)
        show[1] = tm.strftime("%d %B")

    thisdict = {'tijd': show[0], 'dag': show[1], 'naam': show[2], 'type': show[3], 'id' : show[4], 'url': show[5], 'soldout': show[6]}
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


# maximale grootte vergroten/begrenzen
ftplib.FTP.maxline = 65536
ftp = ftplib.FTP(localvar.h)
ftp.login(localvar.un, localvar.ww)

with open(myFile, 'rb') as ftpup:
    ftp.storbinary('STOR ' + myFile, ftpup)
    ftp.close()
