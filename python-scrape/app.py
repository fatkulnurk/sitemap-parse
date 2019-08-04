import requests
from bs4 import BeautifulSoup
import pandas as pd
from slugify import slugify
import database

urls = pd.read_csv('../lirik-lagu/result-liriklaguindonesianet.txt', delimiter = ',')
# print(urls)

mycursor = database.mysql_connection()

for url in urls:
    # print(urls[url]) 
    # req = requests.get('https://liriklaguindonesia.net/shinta-arshinta-kependem-tresno.htm')
    
    sql = "SELECT * FROM lirik_lagu WHERE source = %s"
    adr = (urls[url])
    mycursor.execute(sql, adr)

    myresult = mycursor.fetchone()

    if myresult:
        print('Gagal insert, data sudah ada.')
    else:     
        req = requests.get(urls[url])
        soup = BeautifulSoup(req.text, "lxml")
        if soup:
            data_result_raw = soup.find('div', attrs={'style': 'background-color:#eee; padding:10px; border-top:2px solid #000; border-bottom:2px solid #000;'})
            clean_title = str(soup.title.string.replace("Lirik Lagu ", ""))
            temp = soup.find_all('span')
            clean_date_post = temp[0].span.string
            clean_author = temp[2].span.string
            # print(temp[0].span.string)
            # print(temp[1].string)
            # print(temp[2].span.string)
            data_result_raw.h2.decompose()
            data_result_raw.script.decompose()
            data_result_raw.ins.decompose()
            data_result_raw.script.decompose()
            data_result_raw.div.decompose()
            clean_body = data_result_raw.prettify()
            clean_body = clean_body.replace(' style="background-color:#eee; padding:10px; border-top:2px solid #000; border-bottom:2px solid #000;"', "")
            clean_slug = slugify(clean_title, max_length=150, word_boundary=True)
            
            sql = "INSERT INTO lirik_lagu (title, body, source, author, post_date, chord, slug) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (clean_title, clean_body, urls[url], clean_author, clean_date_post, false, clean_slug)
            mycursor.execute(sql, val)

            mycursor.commit()
