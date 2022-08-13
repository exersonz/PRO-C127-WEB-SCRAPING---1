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
        for tr_tag in soup.find_all('tr'):
            th_tags = tr_tag.find_all('th')
            temp_list = []
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