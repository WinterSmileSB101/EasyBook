#!/usr/bin/python
# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import bs4
import urllib
import re
import os
import urllib.request as req
from urllib.request import urlretrieve


class TodayImage(object):
    def __init__(self):
        self.__baseUrl = r'http://wufazhuce.com/'
        self.__workPath = os.path.abspath('..') + r'\temp\OEBPS\images'
        self.__imageName = 'cover.png'
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        # 设置代理 IP，http 不行，使用 https
        proxy = req.ProxyHandler({'https': 's1firewall:8080'})
        auth = req.HTTPBasicAuthHandler()
        # 构造 opener
        opener = req.build_opener(proxy, auth, req.HTTPHandler)
        # 添加 header
        opener.addheaders = [('User-Agent', user_agent)]
        # 安装 opener
        req.install_opener(opener)

    def GetTodayImage(self,path):
        if not isinstance(path,str):
            raise TypeError('bad operand type of path')
        if len(path)>0:
            self.__workPath = path

        if not os.path.exists(self.__workPath):
            os.makedirs(self.__workPath)

        conn = req.urlopen(self.__baseUrl)

        # 以 utf-8 编码获取网页内容
        content = conn.read().decode('utf-8')
        # print(content)

        soup = BeautifulSoup(content,'lxml')
        picList = soup.select('div.item')
        # print(picList)
        # print(picList[0].a.img['src'])
        imageUrl = picList[1].a.img['src']
        # todayText = picList[1].select('div.fp-one-cita')[0].a.get_text()
        self.StoreImage(imageUrl)

    def StoreImage(self,imageUrl):
        if not isinstance(imageUrl,str):
            raise TypeError('bad operand type of imageUrl')

        if not os.path.exists(self.__workPath+'/'+self.__imageName):
            if len(imageUrl)==0:
                self.GetTodayImage('')
            else:
                urlretrieve(imageUrl,self.__workPath+'/'+self.__imageName)