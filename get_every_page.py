from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
import requests, re, os

with open('chapter.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
data = ''.join(data)
url = data.split('\n')
del(url[-1])

num = 0
pas = 0
for urls in url:
    num += 1
    os.mkdir('./new/'+str(num))
    headers = {
        "origin": "https://baozimh.org",
        "User-Agent": UserAgent().random
    }

    def get_one_manga(url, headers):
        data = requests.get(url, headers=headers)
        data.encoding='utf-8'
        data = data.text
        soup = bs(data, 'lxml')
        all_item = soup.select("#post-1985862 > div > div > div > div > div.gb-container.gb-container-1c32c60b > div")
        for items in all_item:
            img = items.find_all('img', attrs={'class':'lazyload'})[-1]
            last_number = int(img['alt'])
            last_url = img['data-src']
        return last_number, last_url

    def get_pic_add(url, headers, number):
        new_url = []
        for i in range(1, number+1):
            urls = re.sub(r'\b\w+(?=.jpg\b)', str(i), url)
            new_url.append(urls)
        return new_url

    def save_list(url):
        for i in url:
            with open('./data/manga_per'+str(num)+'.txt', 'a', encoding='utf-8') as f:
                f.write(i)
                f.write('\n')
        f.close()
        with open('./data/manga_per'+str(num)+'.txt', 'r', encoding='utf-8') as f:
            data = f.readlines()
        data = ''.join(data)
        data = data.split('\n')
        del(data[-1])
        return data
    try:
        last_number, last_url = get_one_manga(url=urls, headers=headers)
        new_url = get_pic_add(url=last_url, headers=headers, number=last_number)
        url_list = save_list(url=new_url)

    except:
        pas += 1
        print(pas)
        pass

files = os.listdir('./data')
lens = len(files)
regex =  r"\d"
subst = ''
for i in range(1, last_number+1):
    try:
        #cmd = 'aria2c -x 4 -s 8 -j 12 -d ./new/'+str(i)+' -i ./data/manga_per'+str(i)+'.txt --continue=true' # 个人使用
        cmd = 'aria2c -x 16 -s 32 -j 32 -d ./new/'+str(i)+' -i ./data/manga_per'+str(i)+'.txt --continue=true
        print(cmd)
        os.system(cmd)
        print('下载成功!')
    except:
        print('出现错误')

try:
    for i in range(1, last_number):
        cmd = 'aria2c -x 16 -s 32 -j 32 -d ./new/'+str(i)+' -i ./data/manga_per'+str(i)+'.txt --continue=true'
        os.system(cmd)
        print('校验完毕')
except:
    print('出现错误')
