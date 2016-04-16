#will parse http://gallery.artron.net/Select_Gallery.php?Aclass=&Provice=%E5%8C%97%E4%BA%AC&artArea=&arttuan=&exhibition=&Order=1&UserGrade=&keyword=&page=130
#to get the url link for gallery shop
#signature sytanx:
#div with class="shopList"
#a href in this div
import sys
import urllib2
import requests
from lxml import html
from lxml import etree
page = requests.get("http://gallery.artron.net/Select_Gallery.php?Aclass=&Provice=%E5%8C%97%E4%BA%AC&artArea=&arttuan=&exhibition=&Order=1&UserGrade=&keyword=&page=129")
tree1 = html.fromstring(page.content)
#This will create a list of with div class="shopList"
tree2 = etree.HTML(page.text)

#shopList = tree.xpath("//div[@class="shopList"]/text()")
#shopList = tree.xpath("//div[@class='shop']/div[@class='shopList']/h3[@class='fix']")
#shopList = tree.xpath("//div[@class='shop']/div[@class='shopList']/h3[@class='fix']")
#print html.tostring(tree1)
elements = tree2.xpath('//div[@class="shop"]/div[@class="shopList"]/h3[@class="fix"]/a/@href')

print len(elements)
#print etree.tostring(elements[0])
print elements[0]
