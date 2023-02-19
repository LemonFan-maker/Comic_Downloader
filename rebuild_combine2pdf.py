from PIL import Image, ImageFile
from PyPDF2 import PdfReader, PdfWriter
import os

def check_files(folders):
    empty_folders = []
    for folder in folders:
        if os.listdir(folder):
            empty_folders.append(folder)
    return empty_folders

dir = os.listdir('./new')
folders = ["./new/" + str(i) for i in dir]
empty_folders = check_files(folders)

def combine2Pdf(folderPath, pdfFilePath):
    files = os.listdir(folderPath)
    #print(files)
    files.sort(reverse=False, key=lambda x:int(x.split('.')[0]))
    jpgFiles = []
    sources = []
    for file in files:
        if '.jpg' in file:
            jpgFiles.append(folderPath + file)
    #print(jpgFiles)
    output = Image.open(jpgFiles[0])
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    jpgFiles.pop(0)
    for file in jpgFiles:
        jpgFile = Image.open(file)
        if jpgFile.mode == "RGB":
            jpgFile = jpgFile.convert("RGB")
        sources.append(jpgFile)
        #jpgFile.close()
    output.save(pdfFilePath, "pdf", save_all=True, append_images=sources)

def GetFileName(dir_path):
    file_list = [os.path.join(dirpath, filesname) \
                 for dirpath, dirs, files in os.walk(dir_path) \
                 for filesname in files]
    return file_list

def MergePDF(dir_path, file_name):
    output = PdfWriter()
    outputPages = 0
    file_list = GetFileName(dir_path)
    for pdf_file in file_list:
        print("文件：%s" % pdf_file.split('\\')[-1], end=' ')
        # 读取PDF文件
        input = PdfReader(open(pdf_file, "rb"))
        # 获得源PDF文件中页面总数
        pageCount = len(input.pages)
        outputPages += pageCount
        print("页数：%d" % pageCount)
        # 分别将page添加到输出output中
        for iPage in range(pageCount):
            output.add_page(input.pages[iPage])
    print("\n合并后的总页数:%d" % outputPages)
    # 写入到目标PDF文件
    print("PDF文件正在合并，请稍等......")
    with open(file_name, "wb") as outputfile:
        # 注意这里的写法和正常的上下文文件写入是相反的
        output.write(outputfile)
    output.close()
    print("PDF文件合并完成")