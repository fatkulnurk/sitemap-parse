import requests
from bs4 import BeautifulSoup
import pandas as pd
from slugify import slugify
import mysql.connector

# urls = pd.read_csv('../lirik-lagu/result-liriklaguindonesiaorg.txt', delimiter = ',')
url = 'https://liriklaguindonesia.org/lyrics/1000-bayangan/'
urls = url
url = 'https://liriklaguindonesia.org/lyrics/happy-ending/'

mydb = mysql.connector.connect(
    user="dibumico_torrent_bos",
    password="indonesiazonk",
    host="sgx9.cloudhost.id",
    database="dibumico_torrent"
)

mycursor = mydb.cursor()

for u in urls:
    url = urls[u]
    url = url.name
    sql = "SELECT * FROM lirik_lagu WHERE source = '" + url + "'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

if myresult:
    print('Gagal insert, data sudah ada.')
else:     
        # print(url)
    req = requests.get(url)
        # print(req.text)
    soup = BeautifulSoup(req.text, "lxml")
    if soup:
        article = soup.find('article')
            # article_data = article.find('div', attrs={'class': 'lyric-text margint20 marginb20'})
        # print(article)
        data_result_raw = article.find('div', attrs={'class': 'lyric-text margint20 marginb20'})
        data_result_raw = data_result_raw.find_all('p')
        # if data_result_raw:
        data_body = ''.join(str(e) for e in data_result_raw)
        #     # for data in data_result_raw
        #     #     data_body.join()
        print(data_body)
        # print(data_result_raw)