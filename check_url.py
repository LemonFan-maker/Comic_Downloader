import requests, sys
from fake_useragent import UserAgent

def get_url_status(url):
    headers = {
        "origin": "https://baozimh.org",
        "user-agent": UserAgent().random
    }
    status = requests.get(url, headers=headers)
    if status.status_code == 200:
        pass
    else:
        print("请检查地址是否存在")
        sys.exit()

def get_manga_para(url):
    headers = {
        "origin": "https://baozimh.org",
        "user-agent": UserAgent().random
    }
    get_list = url.replace("manga", "chapterlist")
    status = requests.get(get_list, headers=headers)
    if status.status_code == 200:
        pass
    else:
        print("列表不存在")
        sys.exit()
    return get_list

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