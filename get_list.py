def get_manga_url(element, url):
    url_list=[]
    for i in range(0, element+1):
        data = "0_"+str(i)
        urls = url+data
        '"'+urls+'"'
        url_list.append(urls)
    return url_list
