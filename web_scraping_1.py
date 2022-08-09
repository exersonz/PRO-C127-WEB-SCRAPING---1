from attr import attr
from bs4 import BeautifulSoup
import time
import csv
import requests

START_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
page = requests.get(START_URL)
time.sleep(5)

def scrape():
    headers = ['name', 'distance', 'mass', 'radius']
    star_data = []
    for i in range(0, 5):
        soup = BeautifulSoup(page.content, 'html.parser')
        for table in soup.find_all('table', attrs={'class': 'wikitable sortable jquery-tablesorter'}):
            thead_tags = table.find_all('thead')
            temp_list = []
            for thead_tag in thead_tags:
                tr_tags = thead_tag.find_all('tr')
                try:
                    temp_list.append(tr_tags.contents[0])
                except:
                    temp_list.append('')
            for tr_tag in tr_tags:
                th_tags = tr_tag.find_all('th')
                try:
                    temp_list.append(th_tags.contents[0])
                except:
                    temp_list.append('')
            star_data.append(temp_list)
    with open('scrapper.csv', 'w') as m:
        csvwriter = csv.writer(m)
        csvwriter.writerow(headers)
        csvwriter.writerows(star_data)
    
scrape()  