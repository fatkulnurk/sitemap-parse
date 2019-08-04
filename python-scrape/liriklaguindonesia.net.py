import requests
from bs4 import BeautifulSoup
import json
import re

def crawl_data_liriklaguindonesianet(url, mysqlcursor):
    req = requests.get(url)
    # req = requests.get('https://liriklaguindonesia.net/shinta-arshinta-kependem-tresno.htm')
    soup = BeautifulSoup(req.text, "lxml")
    # print(soup.title.string)
    # print(soup.h1.string)
    # dapat banyak, bentuk obj
    # data_result_array_raw = soup.find_all('div', attrs={'style': 'background-color:#eee; padding:10px; border-top:2px solid #000; border-bottom:2px solid #000;'});
    # raw_data_result = data_result_array_raw

    temp = soup.find_all('span')
    print(temp[0].span.string)
    print(temp[1].string)
    print(temp[2].span.string)

    # dapat banyak bentuk, string
    for raw_lyric in soup.find_all('div', attrs={'style': 'background-color:#eee; padding:10px; border-top:2px solid #000; border-bottom:2px solid #000;'}):
        raw_data_result = raw_lyric

    clean_title = str(soup.title.string.replace("Lirik Lagu ", ""))
    clean_title_raw = clean_title.split(" ")

    if (clean_title.find("-") != -1): 
        index = clean_title.find('-')
        print('benar')
        print(index)
        clean_song__name = clean_title[:index]
        clean_song_title = clean_title[index:]
    else: 
        clean_song__name = ''
        clean_song_title = ''

    print(clean_title)
    print(clean_song__name)
    print(clean_song_title)