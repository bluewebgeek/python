# -*- coding: utf-8 -*-
# This script is created by Ciger of Blue Web Geek @http://github.com/bluewebgeek/
#---------------------------------------------------------------------------------
# Date         |Author                  |Description
#---------------------------------------------------------------------------------
# 2016/4/15    |Ciger                   |visit github.com/bluewebgeek/ for tutorials and source codes
#---------------------------------------------------------------------------------
# What does this script do?
# This script will go this website url http://group.amorepacific.com/content/company/global/our-brand/all-brands.html#nohref
# to get all the img href link , and download the file to the current folder
#---------------------------------------------------------------------------------
# Logic
# 1 get the link from http://www.lgcare.com/global/brand/list.jsp?type=BEAUTIFUL
# 2 the the url from step1 (like http://www.lgcare.com/global/brand/detail.jsp?gbn=1&bid1=C065) and get the image down
import os
import urllib2
import time
import requests
from lxml import html
from lxml import etree
import codecs
import logging
logging.basicConfig(filename="grap_the_image.log",level=logging.DEBUG)

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

url_prefix="http://www.lgcare.com/global/brand/detail.jsp?gbn=1&bid1="
url_sufix_list=["C021","C082","C022","C068","C076","C065","C067","C074","C088","C054","C073","C017","C070","H127","C060","C035","C062","H078","C001","C075","C072"]
loopcnt=len(url_sufix_list)
for i in  xrange(1,loopcnt):
    print i
    url=url_prefix+url_sufix_list[i]
    print url
    gallery_page = requests.get(url)
    tree = html.fromstring(gallery_page.content)
    image_urls = tree.xpath('//*[@id="headArea"]/div/img/@src')
#print the number of items in the list
    print(image_urls[0])
    download_file(image_urls[0])
    image_urls = tree.xpath('//*[@id="contArea"]/div/div[1]/div[1]/p[1]/img//@src')
#print the number of items in the list
    print(image_urls[0])
    download_file(image_urls[0])
#main loop

 
