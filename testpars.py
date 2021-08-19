import requests
from bs4 import BeautifulSoup
import csv
from connect_test import *
from peewee import *
import json

URL = 'http://kenesh.kg/ru/deputy/list/35'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36', 'accept': '*/*',}
LINK = 'http://kenesh.kg'
# PATH = 'ddep.csv'


def get_html(url,params=None):
    r = requests.get(url,headers= HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html,'html.parser')
    items = soup.find_all('div', class_='dep-item')
    
    dep = []
    
    for item in items:   
        dep.append({
            'name': item.find('a',class_='name').get_text(strip=True).replace('\n', "").replace('\xa0', ""),
            'part': item.find('div',class_='info').get_text(strip=True).replace('\n', "").replace('\xa0', ""),
            'image': LINK + item.find('img',).get('src').replace('\n\n', "").replace('\xa0', ""),
            # 'number': item.find('span')

        })

    print(dep)
    with open('text.json', 'w', encoding='utf-8') as f:
        my_json = json.dumps(dep, ensure_ascii=False, indent=4)
        f.write(my_json)
    return dep
    


def db_save_product(model, lists):
    save = model.insert(lists).execute()
    return save

    
    
# def save_csv(items, path):
#     with open(path, 'w') as f:
#         writer = csv.writer(f, delimiter = ';')
#         writer.writerow(['Имя', 'Партия', 'Фотография',  'Ссылка на вото', 'номер'])
#         for item in items:
#             writer.writerow([item['name'], item['part'], item['image'], item['number'], ])




def pars_dep():
    html = get_html(URL)
    if html.status_code == 200:
        deps = get_content(html.text)
        db_save_product(Dep, deps)
        # save_csv(deps,PATH)
        
    else:
        print('eror')    

    

pars_dep()
