import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs
def get_elements(url):
    headers = {
        "origin": "https://baozimh.org",
        "user-agent": UserAgent().random
    }
    data = requests.get(url, headers)
    data.encoding= 'utf-8'
    data = data.text
    soup = bs(data, "html.parser")
    last_page = soup.find('a', attrs={'class':'wp-manga-chapterlist'})['href']
    last_string = last_page.split('/')[-2]
    last_element = last_string.split('_')[-1]
    last_element = int(last_element)
    return last_element
