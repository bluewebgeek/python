# -*- coding: utf-8 -*-

#set default encoding to utf8
import sys



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import urllib2
import time
import requests
from lxml import html
from lxml import etree

from BeautifulSoup  import BeautifulSoup
import codecs
import logging

from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
from PyQt4.QtWebKit import *
from BeautifulSoup import BeautifulSoup


def urllib2_downloadX(url,local_filename):
    remote_sufix=url.split('/')[-1]
    remote_sufix=url.split('.')[-1]
    local_filename=local_filename+"."+remote_sufix
    with open(local_filename, 'wb') as f:
        f.write(urllib2.urlopen(url).read())
        f.close()
    print "Download Complete!"





#render the url

#Take this class for granted.Just use result of rendering.
class Render(QWebPage):  
  def __init__(self, url):  
    self.app = QApplication(sys.argv)  
    QWebPage.__init__(self)  
    self.loadFinished.connect(self._loadFinished)  
    self.mainFrame().load(QUrl(url))  
    self.app.exec_()  
  
  def _loadFinished(self, result):  
    self.frame = self.mainFrame()  
    self.app.quit()
    
chromedriver = "C:\chromewebdriver\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
url='http://www.shilladfs.com/estore/kr/zh/b/whoo'
driver.get(url)
#driver.find_element_by_class_name('pagination-nav--next').click()
driver.find_element_by_xpath("//*[@id='container']/div/div[4]/div/div[2]/ul/li[4]/a").send_keys(Keys.RETURN)
#wait the page to render
time.sleep(10)
result=driver.page_source
#the result is a unicode encoded 
#change to tree, then using xpath to parse the href
tree = html.fromstring(result) 

#store the shop links list
shop_links = tree.xpath('//*[@id="container"]/div/div/div/div/ul/li/div/div[@class="product_over_wrap"]/a/@href')
 
shop_url = "http://www.shilladfs.com"+shop_links[0]
print(shop_url)

driver.get(shop_url)
time.sleep(5)
shop_result=driver.page_source
shop_tree = html.fromstring(shop_result)  

#parse the image link from the shop page
product_images=shop_tree.xpath('//*[@id="container"]/div/div/div/ul/li/a/img/@data-image')
print(product_images)
#parse the brand title
brand_titles=shop_tree.xpath('//*[@id="container"]/div[2]/div[1]/h3/text()')
print(brand_titles[0].strip())
brnd_titl=brand_titles[0].strip()
#parse the product title
product_titles=shop_tree.xpath('//*[@id="container"]/div[2]/div[1]/h3/span/text()')
print(product_titles[0])
#parse the price
product_prices=shop_tree.xpath('//*[@id="container"]/div[2]/div[2]/div[2]/div[1]/dl[1]/dd/span/text()')
print(product_prices[0])

#composite local file name
i=0
while (i<len(product_images)):
    price=product_prices[0][4:]
    flname=brnd_titl+product_titles[0]+price+str(i)
    flname=flname.replace(":", "")
    flname=flname.replace("/", "")
    print(flname)
    urllib2_downloadX(product_images[i],flname)
    i=i+1
