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
        try:
            url = item.find_parent('a').get('href')
        except AttributeError:
            print(item)
            url = ""

        for it in item.select('span.date'):
            datum = it.get_text().strip()
        for it in item.select('h3.article-title'):
            nameShow = it.get_text().strip()
        for it in item.select('div.ticket-status'):
            ticketstatus = it.get_text().strip()
        for it in item.select('span.article-type'):
            type = it.get_text().strip()

        tijd = ''
        try:
            tijd = datum.split(' - ')[1]
        except AttributeError:
            print(item)
            tijd = '00:00'
        except:
            tijd = ''

        dag = ''
        try:
            dag = datum.split(' - ')[0]
        except AttributeError:
            print(item)
            dag = '?? ??'


        thisdict = {'tijd': tijd, 'dag': dag, 'naam': nameShow, 'type': type,
                    'id': 0, 'url': 'https://verkadefabriek.nl' + url, 'soldout': ticketstatus}
        showsArrOfDicts.append(thisdict)
    return showsArrOfDicts


# specify the url
toscrape_page = localvar.s

# query the website and return the html to the variable ‘page’
html = requests.get(toscrape_page, verify=True)
soup = BeautifulSoup(html.text, 'html.parser')
allPagesShowsArrOfDicts = []
allPagesShowsArrOfDicts = scrapePage(soup, allPagesShowsArrOfDicts)

print(allPagesShowsArrOfDicts)

# Zoeken van laatste pagina in agenda
lastpage = 1
for item in soup.select('a.page-link'):
    lastpage = item.get('href').split('=')[1]


i = 2
while i <= int(lastpage):
    toscrape_page = localvar.s + '?page=' + str(i)
    print(toscrape_page)
    # query the website and return the html to the variable ‘page’
    html = requests.get(toscrape_page, verify=True)
    soup = BeautifulSoup(html.text, 'html.parser')
    allPagesShowsArrOfDicts = scrapePage(soup, allPagesShowsArrOfDicts)
    print(allPagesShowsArrOfDicts)
    i = i + 1

# all pages ares scraped and the shows are in allPagesShowsArrOfDicts
# I want from this array of dicts only the ones with type = 'Film' and  add them with the cosmicjs api
# to the cosmicjs bucket, if the film does not exist yet
# first I need to import the class CosmicJsApi from cosmicJsApi.py
# then I need to create an instance of the class with the bucket_slug, read_key and write_key
# then I can loop through the allPagesShowsArrOfDicts and add the films to the cosmicjs bucket
# after that I scraped the page from the url and added the description and directors to the film

import cosmicJsApi as cja
cosmicjs = cja.CosmicJsApi(localvar.COSMIC_BUCKET_SLUG, localvar.COSMIC_READ_KEY, localvar.COSMIC_WRITE_KEY)

for show in allPagesShowsArrOfDicts:
    count = 0
    if show['type'] == 'Film':
        title = show['naam']
        #from the url I want to scrape the description and the directors
        url = show['url']
        #slug is the last part of the url
        slug = url.split('/')[-1]   
        
        html = requests.get(url, verify=True)
        soup = BeautifulSoup(html.text, 'html.parser')
        # description is an empty array
        description = []
        directors = ''
        for item in soup.select('h4.subtitle'):
            directors = item.get_text().strip()
            #only the first .subtitle has the director(s)
            break
            
        for item in soup.select('section.contentblock-TextOneColumn p'):
            # item.get_text().strip() add this to description
            description.append(item.get_text().strip())

        content = {'title' : title, 'description': description, 'directors': directors, 'count': 0, 'reviewTotal':0 }
        
        print(cosmicjs.add_movie(title, slug, content))
        count += 1
        

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
