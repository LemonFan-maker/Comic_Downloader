# 声明: 本爬虫仅供学习(应该没人会看我写的吧:rofl:)。

# 项目介绍:

## 爬取地址:

**[包子漫画](https://baozimh.org)**

## 爬虫框架:

**BeautifulSoup**

- BeautifulSoup官方文档: [https://beautifulsoup.cn](https://beautifulsoup.cn/)

## 依赖库

```shell
bs4(BeautifulSoup)
requests
fake_useragent
PIL(pillow)
PyPDF2
sys
time
os
shutil
re
```

# 特性

1. img转PDF(实验性)
2. PDF合并PDF

# 使用方法

## Step1. 安装依赖

```shell
pip install pillow requests fake_useragent bs4 PyPDF2 lxml
```

## Step2. 获取漫画地址

1. 点击首页想看的漫画![](./assets/helper1.png)

2. 查看漫画链接![](./assets/helper2.png)

3. 运行程序，在`input`中输入地址

​	**注意:** 输入地址时不要忘记最后的正斜杠(**/**) 

​	正确的地址:`https://baozimh.org/manga/yaoguaijiuguan-muba/`

​	错误的地址:`https://baozimh.org/manga/yaoguaijiuguan-muba`, `https://baozimh.org/chapterlist/yaoguaijiuguan-muba/`, `https://baozimh.org/chapterlist/yaoguaijiuguan-muba`等等。

# BUG?

在使用中如果出现bug，请前往反馈，[点这里](https://github.com/LemonFan-maker/Comic_Spider/issues)

**注意：** 提交Bug时，请复制所有报错信息，并附加漫画地址。

**目前已知BUG:**

	1. PDF排版(包括合并版(合并.pdf)与分集版(contract{n}.pdf))顺序出错
	2. 可能出现重复画面(极少部分)

# GitHub Action 下载教程

1. 修改`main.py`文件`main_url`处地址为自己想下载漫画的地址(见**使用方法**)
2. 保存提交
3. 运行Action，等待下载完成。

# 个人下载(电脑&手机)教程

**注意:**不建议自己下载，网速太慢(能嫖20MB/S的下载速度为啥有人要在个人设备上运行**:see_no_evil:**?)。

**电脑操作(Windows&Linux)**

*预先条件*

​	I. Windows: **系统可以成功调用aria2下载程序**

​	II. Linux:  `sudo apt install aria2`

1. 同**GitHub Action 下载教程**
2. 安装依赖
3. 修改`cmd = 'aria2c -x 16 -s 32 -j 32 -d ./new/'+str(i)+' -i ./data/manga_per'+str(i)+'.txt --continue=true'`中`-x `、`-s`、`-j`之后的数值(改小，目前这是最大值)
4. 保存运行。

**手机操作**

 	1. 手机安装[Termux](https://github.com/termux/termux-app/releases)(直达release下载地址)
 	2. Termux换源`termux-chage-repo`(墙裂推荐BFSU源~可比清华的快多了(大嘘)~）
 	3. `apt install python python-pip git libxml2 libxslt nano aria2` 
 	4. `pkg i libjpeg-turbo zlib`
 	5. 安装依赖(时间比较长，等待)
 	6. 克隆仓库`git clone https://github.com/LemonFan-maker/Comic_Spider.git`
 	7. 同**电脑操作**

*提示:* 可采用`nano`进行编辑

# TDL

1. 修复错误
2. ~~支持github action 打包下载~~ (初步已实现)
3. 更新img2PDF
4. 下载指定章节
5. 以漫画名称命名目录
6. ,etc
