#!/user/bin/python3
#-*-coding:UTF-8-*-

#获取http://bs309.com下所有泰妍图片

import urllib.request
import re
import os

#获取当前文件路径
path=os.path.abspath('.')

#通过传过来的url地址，打开页面，return页面源码
def open_url(url):
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0')
    page=urllib.request.urlopen(req)
    html=page.read().decode('utf-8')
    #print(html)
    return html

#获取页面中的所有符合条件的链接
def page_url(html):
    b=r'<a href="/xe/index.php\?mid=data\&amp\;page=\d\&amp\;document_srl=\d\d\d'
    #urllist=re.findall(a,html)
    urllist1=re.findall(b,html)
    for aa in urllist1:
        #print(aa)
        a=aa.split(';')[-1]
        b=(aa.split(';')[-2]).split('&')[-2]
        print('http://bs309.com/xe/index.php?mid=data&'+b+'&'+a)
        get_img(open_url('http://bs309.com/xe/index.php?mid=data&'+b+'&'+a))

#下载图片
def get_img(html):
    #print('get_img')
    #寻找图片
    p=r'<img src="https([^"]+\.png)"'
    q=r'<img src="https([^"]+\.jpg)"'

    #获取页面标题，作为文件夹名
    b=r'<a href="http://.*">.*</a>'
    urllist=re.findall(b,html)

    #将路径设置为之前定义的路径下
    os.chdir(path)
    
    for i in urllist:
        ii=i.split('>')[-2]
        name=ii.split('<')[-2]

    #创建文件夹
    os.mkdir(name)
    #路径调整至创建的文件夹下
    os.chdir(name)
    
    imglist=re.findall(p,html)
    imglist1=re.findall(q,html)
    for ii in imglist1:
        imglist.append(ii)
    #print(imglist)
    for each in imglist:
        filename=each.split("/")[-1]
        #print(filename)
        urllib.request.urlretrieve('https'+each,filename,None)

if __name__=='__main__':
    url='http://bs309.com/xe/index.php?mid=data&page='

    #获取网站所有泰妍图片
    for i in range(1,7):
        page_url(open_url(url+str(i)))
