from bs4 import BeautifulSoup
import requests

url = 'http://fec.mofcom.gov.cn/article/gbdqzn/#'
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

with open('ids.txt','w',encoding='utf-8') as f:
    divs = soup.find_all('div', class_='more')
    for div in divs:
        a_list = div.find_all('a')
        for a in a_list:
          f.write(a.get_text() + ',')
          span = a.find('span')
          if span:
            f.write(a.find('span')['id'] + ',')