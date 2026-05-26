import requests
from bs4 import BeautifulSoup
import sqlite3


url = 'https://divar.ir/s/tehran/car'
creat_table = 'CREATE TABLE car(name varchar(100), info INT, price INT)'
insert_data = 'INSERT INTO car VALUES(?,?,?)'


res = requests.get(url)
data = res.text
soup = BeautifulSoup(data, 'html.parser')


ads = soup.select('.kt-post-card__info')

ads_name = []
ads_info = []
ads_price = []

for ad in ads:
    name = ad.select('.kt-post-card__title')
    info = ad.select('.kt-post-card__description')
    for i in info :
        if 'کیلومتر' in i.text:
            ads_info.append(i.text.replace(' کیلومتر', '').replace(',', ''))
        else:
            ads_price.append(i.text.replace(' تومان', '').replace(',', ''))
    for n in name:
        ads_name.append(n.text)
    
 
        
conn = sqlite3.connect('cars.db')
cursor = conn.cursor()
cursor.execute(creat_table)
conn.commit()

for i in range(len(ads_name)):
    cursor.execute(insert_data,(ads_name[i],ads_info[i],ads_price[i]))
    conn.commit()
    
conn.close()

