from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
import requests

def check_pic_addr(url):
    headers = {
        "origin": "https://baozimh.org",
        "user-agent": UserAgent().random
    }
    data = requests.get(url, headers=headers)
    data = data.text
    soup = bs(data, 'lxml')
    data = soup.prettify()
    data = soup.find_all('a', attrs={'class':'wp-manga-chapterlist'})
    for i in data:
        with open('chapter.txt', 'a', encoding='utf-8') as f:
            f.write(str(i['href']))
            f.write('\n')
        f.close()