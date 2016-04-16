# -*- coding: utf-8 -*-
import sys
import os
import urllib2
import time
import requests
from lxml import html
from lxml import etree
import codecs

    
def parse_url (full_url):
    page = requests.get(full_url)
    tree = html .fromstring(page.content)
    shop_url=tree.xpath('//div[@class="shop"]/div[@class="shopList"]/h3[@class="fix"]/a/@href')
    print len(shop_url)
    print shop_url[1]
    return



gallery_info_url="http://gallery.artron.net/Select_Gallery.php?Aclass=&Provice=&artArea=&arttuan=&exhibition=&UserGrade=&Order=1&keyword="
gallery_page = requests.get(gallery_info_url)
tree = html.fromstring(gallery_page.content)
contact = tree.xpath('//div[@class="pw fix z  mt20 serA"]/div[@class="fl lay710 mr20"]/div[@class="ser bg"]/div[@class="bgF"]/div[@class="type"]/p[@id="tab_2"]/b/span/a/text()')
print ("contact name: "+contact[1])
print (len(contact))
for i in xrange(1,len(contact)):
    print (contact[i]+" "+str(i))
#    str= contact[i]
 #   print str
 #   full_url = "http://gallery.artron.net/Select_Gallery.php?Aclass=&Provice=" + str +"&artArea=&arttuan=&exhibition=&Order=1&UserGrade=&keyword=&page=" +"1"
  #  parse_url(full_url)
    
