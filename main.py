import check_param, check_url, check_pic, get_list, get_newest_elements
import os, time, shutil

lst = ['./data', './new', './results', './uncombine']
for i in lst:
    if os.path.exists(i):
        print(i)
        shutil.rmtree(i)

for u in lst:
    if not os.path.exists(u):
        print(u)
        os.mkdir(u)

lst2 = ['./chapter.txt']

for i in lst2:
    if os.path.exists(i):
        os.unlink(i)

start_time = time.time()
main_url = "https://baozimh.org/manga/qianhaizhanji-qianhaiyueluwenhuayuantongkengshuxiaohaican/"

check_url.get_url_status(main_url)
manga_url = check_param.get_manga_para(main_url)
check_pic.check_pic_addr(manga_url)
elements = get_newest_elements.get_elements(manga_url)
data = get_list.get_manga_url(element=elements, url=main_url)

import get_every_page, rebuild_combine2pdf

try:
    get_every_page()
    pass
except:
    pass

dir = os.listdir('./new')
folders = ["./new/" + str(i) for i in dir]
print(folders)
empty_folders = rebuild_combine2pdf.check_files(folders)

num = 0
for i in empty_folders:
    num +=1
    folder = i+'/'
    pdfFile = "./uncombine/contract"+str(num)+".pdf"
    rebuild_combine2pdf.combine2Pdf(folder, pdfFile)
    print('读取成功...')
dir_path = './uncombine/'
# 目标文件的名字
file_name = "./results/合并.pdf"
rebuild_combine2pdf.MergePDF(dir_path, file_name)
stop_time = time.time()

print('耗时:',stop_time-start_time)
