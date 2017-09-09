from urllib.request import urlopen
import csv
from bs4 import BeautifulSoup
from random import randint
from time import sleep
import csv


def get_url_list():
    master_list=[]
    with open('Book1.csv','r') as text_file:
        text_reader=csv.reader(text_file)
        for line in text_reader:
            master_list.append(line[0])
    return master_list


def scrape_prf(url):
    master_list=[]
    years=[i for i in range (1990,2014)]
    target_url=urlopen(url).read()
    soup=BeautifulSoup(target_url)
    for tr in soup.find_all('tr'):
        tds=tr.find_all('td')
        if len(tds)==31:
            master_list.append([tds[1].text,tds[5].text,tds[6].text,tds[12].text])
    return master_list
        

def main():
    qb_list=[]
    url_list=get_url_list()
    for item in url_list:
        qb_call=item[-12:-4]
        qb_list.append(scrape_prf(item))
        sleep(randint(4,7))
    print ('done scraping, writing')
    with open('age_curve.csv','w',newline='') as csv_file:
        writer=csv.writer(csv_file)
        for item in qb_list:
            for i in item:
                writer.writerow(i)

if __name__=='__main__':
    main()
