#this script to parse the Artron Gallery Yellow Page to get the contact number 
#the url : http://shop.artron.net/8980/g_infor8980.html
#after analysis, the contact is marked by a span class = "fmE"
import sys
import urllib2
import requests
from lxml import html
page = requests.get("http://shop.artron.net/8980/g_infor8980.html")
tree = html.fromstring(page.content)
#This will create a list of with span class="fmE"
prices = tree.xpath('//span[@class="fmE"]/text()')
print 'Prices: ', prices

print  len(prices)
print  prices[0]

#write the phone number to a file
file = open("galleryPhone.txt", "a")

file.write(prices[0])

 
file.close()
