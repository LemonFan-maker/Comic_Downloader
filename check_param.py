import requests, sys
from fake_useragent import UserAgent

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
