# -*- coding: utf-8 -*-

import sys  

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


logging.basicConfig(filename="shilladfs.log",level=logging.DEBUG)


def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian
    return local_filename


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



#Main
 
url="http://www.shilladfs.com/estore/kr/zh/Domestic-Brand/Makeup/Base/p/454576"
#render the javascript rendered webpage


shop_r = Render(url)



shop_result = str(shop_r.frame.toHtml().toUtf8())
print(shop_result)
tree = html.fromstring(shop_result)
archive_links = tree.xpath('//*[@id="container"]/div/div/div/ul/li/a/img/@data-image')
print archive_links




