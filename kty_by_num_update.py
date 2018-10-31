#!/user/bin/python3
#-*-coding:UTF-8-*-

#获取http://bs309.com下所有泰妍图片
#由链接的最后的数字获取图片

import urllib.request
import re
import os
import threading
import time
from bs4 import BeautifulSoup as bs

path=os.path.abspath('.')

def open_url(url):
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0')
    page=urllib.request.urlopen(req)
    html=page.read().decode('utf-8')
    #print(html)
    return html


def get_img(html):
    
    soup=bs(html,'lxml')
    urlList=soup.find_all('img',src=re.compile("https"))
    imgList=[]
    for url in urlList:
        print(url.get('src').lstrip())
        imgList.append(url.get('src').lstrip())
    print("\n共"+str(len(imgList))+"张图片")
    fileName=soup.find('a',href=re.compile("http://bs309.com/xe")).string
    print("\nfileName:"+fileName)
    
    os.chdir(path)
    
    os.mkdir(fileName)
    os.chdir(fileName)
    
    downloads = []
    for each in imgList:
        imgName=each.split("/")[-1]
        down = threading.Thread(target=download, args=[each,imgName])
        downloads.append(down)
        down.start()
    for each in downloads:
        each.join()

def download(url,imgName):
    print('\n[downloading:]'+imgName)
    urllib.request.urlretrieve(url,imgName,None)
    print('\n[download success]:'+imgName)
    
if __name__=='__main__':
    print("#此程序用于下载http://bs309.com/xe/data中的图片#")
    print("\n-----如：http://bs309.com/xe/data/938  输入938即可-----")
    while(True):
        url='http://bs309.com/xe/data/'
        num=input('\n链接最后的数字：')
        time_start=time.time()
        get_img(open_url(url+num))
        time_end=time.time()
        print("\n-----success-----")
        print('\ntime cost',time_end-time_start,'s')
