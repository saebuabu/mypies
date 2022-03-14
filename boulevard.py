import urllib.request
import numpy as np
from bs4 import BeautifulSoup
import datetime
import re


def scrape_event_info(event):
    '''
    scraping van 1 programma-item
    '''
    req_event = urllib.request.urlopen(event)
    bs_event = BeautifulSoup(req_event, "html.parser")
    info_dict = {}

    h1 = bs_event.findAll('h1')
    for title in h1:
        info_dict['titel'] = title.getText()
        break

    titles = []
    for bs_info in bs_event.findAll('span', attrs={'class': 'event-info-title'}):
        titles.append(bs_info.getText())

    values = []
    for bs_info in bs_event.findAll('span', attrs={'class': 'event-info-value'}):
        values.append(bs_info.getText())

    for i,t in enumerate(titles):
        info_dict[t] = values[i]

    return info_dict


# startpagina van het programma van de boulevard
page_toscrape = 'https://www.festivalboulevard.nl/nl/programma/'
reqpage = urllib.request.urlopen(page_toscrape)
bs_content = BeautifulSoup(reqpage, "html.parser")

alleitems = []

for link in bs_content.findAll('a', attrs={'href': re.compile("^https://www.festivalboulevard.nl/nl/programma/id-.*")}):
    alleitems.append(link.get('href'))

# omzetten naar numpy object
np_Alleitems = np.array(alleitems)

alle_events_info = []
for event in np.unique(np_Alleitems):
    event_info = alle_events_info.append(scrape_event_info(event))
    alle_events_info.append(event_info)

print(alle_events_info)