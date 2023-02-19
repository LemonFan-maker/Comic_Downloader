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