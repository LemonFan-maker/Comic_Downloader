import check_param, check_url, check_pic, get_list, get_newest_elements
import os, time

# start_time = time.time()
# main_url = "https://baozimh.org/manga/qianhaizhanji-qianhaiyueluwenhuayuantongkengshuxiaohaican/"

# check_url.get_url_status(main_url)
# manga_url = check_param.get_manga_para(main_url)
# check_pic.check_pic_addr(manga_url)
# elements = get_newest_elements.get_elements(manga_url)
# data = get_list.get_manga_url(element=elements, url=main_url)

import get_every_page, combine2pdf

#get_every_page()
combine2pdf()
#stop_time = time.time()

#print('耗时:',stop_time-start_time)
