# coding: utf-8
import requests
from bs4 import BeautifulSoup
import pandas as pd
from slugify import slugify
import db

urls = pd.read_csv('../lirik-lagu/result-liriklaguinfo.txt', delimiter = ',')

mydb = db.mysql_connection()
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
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "lxml")
        if soup:
            data_result_raw = soup.find('h1', attrs= {'class': 'entry-title'})
            if data_result_raw:
                clean_title = str(data_result_raw.string.replace('Lirik Lagu ', ''))
                clean_title = clean_title.replace('Chord Gitar ', '')
                clean_title = clean_title.replace(' plus Kunci Gitar', '')
                clean_title = clean_title.replace(' - Chord Gitar dan Lirik Lagu', '')
                clean_title = clean_title.replace(' + CHORD GITAR', '')
                clean_title = clean_title.replace(' | www.liriklagu.info', '')
                clean_title = clean_title.replace(' | Lirik Lagu dot Info', '')
                clean_title = clean_title.replace(' | Lirik Lagu dot Info www.liriklagu.info', '')

                data_result_raw = soup.find('div', attrs= {'class': 'entry-content'})
                if data_result_raw:
                    clean_body = data_result_raw.prettify(formatter="html5")
                    clean_body = clean_body.replace('&Acirc;', '')
                    clean_slug = slugify(clean_title)
                    sql = "INSERT INTO lirik_lagu (title, body, source, author, post_date, chord, slug) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    val = (str(clean_title), str(clean_body), str(url), "", "", 'True', str(clean_slug))
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print(mycursor.rowcount, "record inserted.")
                    print('-----------------------------')