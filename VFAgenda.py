import json
import os
import urllib.request
# ftp naar de remote omgeving
import ftplib
import localvar
from bs4 import BeautifulSoup
import requests

import datetime


def scrapePage(souped, showsArrOfDicts):
    for item in souped.select('div.article-wrapper'):
        datum = nameShow = type = url = ticketstatus = None
        url = item.find_parent('a').get('href')
        for it in item.select('span.date'):
            datum = it.get_text().strip()
        for it in item.select('h3.article-title'):
            nameShow = it.get_text().strip()
        for it in item.select('div.ticket-status'):
            ticketstatus = it.get_text().strip()
        for it in item.select('span.article-type'):
            type = it.get_text().strip()

        thisdict = {'tijd': datum.split(' - ')[1], 'dag': datum.split(' - ')[0], 'naam': nameShow, 'type': type,
                    'id': 0, 'url': url, 'soldout': ticketstatus}
        showsArrOfDicts.append(thisdict)

    return showsArrOfDicts


# specify the url
toscrape_page = localvar.s

# query the website and return the html to the variable ‘page’
html = requests.get(toscrape_page, verify=True)
soup = BeautifulSoup(html.text, 'html.parser')
allPagesShowsArrOfDicts = []
allPagesShowsArrOfDicts = scrapePage(soup, allPagesShowsArrOfDicts)

# Zoeken van laatste pagina in agenda
lastpage = 1
for item in soup.select('a.page-link'):
    lastpage = item.get('href').split('=')[1]

i = 2
while i <= int(lastpage):
#while i <= 5:
    toscrape_page = localvar.s + '?page=' + str(i)
    # query the website and return the html to the variable ‘page’
    html = requests.get(toscrape_page, verify=True)
    soup = BeautifulSoup(html.text, 'html.parser')
    allPagesShowsArrOfDicts = scrapePage(soup, allPagesShowsArrOfDicts)
    i = i + 1



myFile = 'show_json.json'
if os.path.exists(myFile):
    os.remove(myFile)
# json dump van de shows
with open(myFile, 'a') as write_file:
    write_file.write('[')
    cnt = 1
    # vervolgens iedere dict json dumpen en wrappen in een array
    for ds in allPagesShowsArrOfDicts:
        json.dump(ds, write_file)
        if cnt < len(allPagesShowsArrOfDicts):
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
