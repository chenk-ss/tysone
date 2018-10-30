#!/user/bin/python3
#-*-coding:UTF-8-*-

#获取http://bs309.com下所有泰妍图片
#由链接的最后的数字获取图片

import urllib.request
import re
import os
import threading
import time

path=os.path.abspath('.')

def open_url(url):
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0')
    page=urllib.request.urlopen(req)
    html=page.read().decode('utf-8')

    return html


def get_img(html):
    p=r'<img src="https([^"]+\.png)"'
    q=r'<img src="https([^"]+\.jpg)"'
    b=r'<a href="http://.*">.*</a>'
    urllist=re.findall(b,html)
    os.chdir(path)
    for i in urllist:
        ii=i.split('>')[-2]
        name=ii.split('<')[-2]
    os.mkdir(name)
    os.chdir(name)
    imglist=re.findall(p,html)
    imglist1=re.findall(q,html)
    for ii in imglist1:
        imglist.append(ii)
    downloads = []
    for each in imglist:
        filename=each.split("/")[-1]
        down = threading.Thread(target=download, args=['https'+each,filename])
        downloads.append(down)
        down.start()
    for each in downloads:
        each.join()
        #urllib.request.urlretrieve('https'+each,filename,None)
def download(url,filename):
    print('\ndownloading:'+url)
    urllib.request.urlretrieve(url,filename,None)
    print('\n[download success]:'+url)
    
if __name__=='__main__':
    url='http://bs309.com/xe/data/'
    num=input('页面最后一串代码：')
    time_start=time.time()
    get_img(open_url(url+num))
    time_end=time.time()
    print('time cost',time_end-time_start,'s')
