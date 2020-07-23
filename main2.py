# import libraries
# import csv
import json
import os
import urllib.request
# ftp naar de remote omgeving
import ftplib
import localvar
from bs4 import BeautifulSoup
import datetime
from requests import Session

# specify the ur
login_page = localvar.tl
page_toscrape = localvar.t

# webpagina wordt in de soup gegooid
# soup = BeautifulSoup(page, 'html.parser')

with Session() as s:
    site = s.get(login_page)
    bs_content = BeautifulSoup(site.content, "html.parser")
    login_data = {"EmailAddress": "abu.saebu@home.nl", "Password": "Vjack2002"}
    s.post(login_page, login_data)

    home_page = s.get(page_toscrape)
    bs_content = BeautifulSoup(home_page.content, "html.parser")

    script = bs_content.findAll('script')[9].string

    script = script.split("var jsonCart =", 1)[-1].rsplit(';', 3)[0]

    data = json.loads(script)

    # print(data['Shows'][0]['EditData']['Seats'])
    aantalavailable = 0
    for i in data['Shows'][0]['EditData']['Seats']:
        if i['S'] == True and i['B'] == False:
            aantalavailable += 1

    print(aantalavailable)