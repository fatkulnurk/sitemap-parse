import requests
from bs4 import BeautifulSoup
import pandas as pd
from slugify import slugify
import mysql.connector

urls = pd.read_csv('../lirik-lagu/result-liriklaguindonesianet.txt', delimiter = ',')
# print(urls)

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
    # myresult = mycursor.fetchone()

    if myresult:
        print('Gagal insert, data sudah ada.')
    else:     
        # print(url)
        req = requests.get(url)
        # print(req.text)
        soup = BeautifulSoup(req.text, "lxml")
        if soup:
            data_result_raw = soup.find('div', attrs={'style': 'background-color:#eee; padding:10px; border-top:2px solid #000; border-bottom:2px solid #000;'})
            if data_result_raw:
                clean_title = str(soup.title.string.replace("Lirik Lagu ", ""))
                temp = soup.find_all('span')
                clean_date_post = temp[0].span.string
                clean_author = temp[2].span.string
                # print(temp[0].span.string)
                # print(temp[1].string)
                # print(temp[2].span.string)
                data_result_raw.h2.decompose()
                if data_result_raw.script:
                    data_result_raw.script.decompose()

                if data_result_raw.ins:
                    data_result_raw.ins.decompose()  

                if data_result_raw.script:
                    data_result_raw.script.decompose()
                    
                if data_result_raw.div:
                    data_result_raw.div.decompose()
    
                clean_body = data_result_raw.prettify()
                clean_body = clean_body.replace(' style="background-color:#eee; padding:10px; border-top:2px solid #000; border-bottom:2px solid #000;"', "")
                clean_slug = slugify(clean_title, max_length=150, word_boundary=True)
                sql = "INSERT INTO lirik_lagu (title, body, source, author, post_date, chord, slug) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                val = (str(clean_title), str(clean_body), str(url), str(clean_author), str(clean_date_post), False, str(clean_slug))
                mycursor.execute(sql, val)
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")
                print('-----------------------------')
