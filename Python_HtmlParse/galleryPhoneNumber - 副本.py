# -*- coding: utf-8 -*-
#get all the gallery number from http://gallery.artron.net/
#gallery index page 
# http://gallery.artron.net/Select_Gallery.php?Aclass=&Provice=%E5%8C%97%E4%BA%AC&artArea=&arttuan=&exhibition=&Order=1&UserGrade=&keyword=&page=129
# 1. loop through index page get the gallery url
#go to the url page  and get the phone number
import sys
import os
import urllib2
import time
import requests
from lxml import html
from lxml import etree
import codecs
prefix="http://gallery.artron.net/Select_Gallery.php?Aclass=&Provice=%E5%8C%97%E4%BA%AC&artArea=&arttuan=&exhibition=&Order=1&UserGrade=&keyword=&page="

def Main():
#create the new output file with name beijing_gallery[1].csv
        first_rec = "英文称谓,名,中间名,姓,中文称谓,单位,部门,职务,商务地址 街道,商务地址 街道 2,商务地址 街道 3,商务地址 市/县,商务地址 省/市/自治区,商务地址 邮政编码,商务地址 国家/地区,住宅地址 街道,住宅地址 街道 2,住宅地址 街道 3,住宅地址 市/县,住宅地址 省/市/自治区,住宅地址 邮政编码,住宅地址 国家/地区,其他地址 街道,其他地址 街道 2,其他地址 街道 3,其他地址 市/县,其他地址 省/市/自治区,其他地址 邮政编码,其他地址 国家/地区,助理的电话,商务传真,商务电话,商务电话 2,回电话,车载电话,单位主要电话,住宅传真,住宅电话,住宅电话 2,ISDN,移动电话,其他传真,其他电话,寻呼机,主要电话,无绳电话,TTY/TDD 电话,电报,Internet 忙闲,办公地点,地点,电子邮件地址,电子邮件类型,电子邮件显示名称,电子邮件 2 地址,电子邮件 2 类型,电子邮件 2 显示名,电子邮件 3 地址,电子邮件 3 类型,电子邮件 3 显示名,附注,工作证号码,关键词,记帐信息,纪念日,经理姓名,类别,里程,敏感度,目录服务器,配偶,其他地址 - 邮箱,商务地址 - 邮箱,身份证编号,生日,私有,缩写,网页,性别,业余爱好,引用者,用户 1,用户 2,用户 3,用户 4,优先级,语言,帐户,职业,助理的姓名,住宅地址 - 邮箱,子女"
        first_rec = first_rec +"\n"
        file = open("galleryPhone.csv", "w")
        #write number, but we need more 
        file.write(first_rec)
        file.close()
#Main Loop
        cnt=1
        while (cnt<130):
                index_url = prefix +bytes(cnt)
                print index_url
                page = requests.get(index_url)
                tree2 = etree.HTML(page.text)
                #parse gallery index page
                #parse to get the link 
                elements = tree2.xpath('//div[@class="shop"]/div[@class="shopList"]/h3[@class="fix"]/a/@href')
                element_idx = 0
                while (element_idx<len(elements)):
                        print elements[element_idx]
                        gallery_url=elements[element_idx]
                        Parse_Gallery_Url(gallery_url)
                        element_idx = element_idx + 1
                cnt = cnt +1
        return
def Parse_Gallery_Url(gallery_url):
#parse gallery info page
#get the number and write to file
        indx = gallery_url.find("/",8)
        if indx>0:
                gallery_id = gallery_url[indx+1:]
                
                print "gallery_url "+gallery_url
                print "gallery number is "+(gallery_id)

                gallery_info_url = gallery_url+"/g_infor"+(gallery_id)+".html"

                print "gallery info url is  " +gallery_info_url

                #get HTTP request from server
                gallery_page = requests.get(gallery_info_url)

                #make a time delay in order to give the server some time to respond
                time.sleep(1)

                tree = html.fromstring(gallery_page.content)
                #parse to get the contact name
                contact = tree.xpath('//div[@id="main"]/div[@class="gallery mt20"]/div[@class="gInfo"]/h1/text()')
                #print ("length of contact"+bytes(len(contact)))
                #print (len(contact))
                print ("contact name: "+contact[0])
                
                #parse to get the phone number
                contac_nbr = tree.xpath('//span[@class="fmE"]/text()')
                if (len(contac_nbr)>0):
                        #contac_nbr[0].decode('utf-8', 'ignore')
                        #contac_nbr[0].decode('gbk', 'ignore')
                        #contac_nbr[0].decode('ascii', 'ignore')
                        #print len(number)
                        #print "Phone number for gallery id "+gallery_id+" is "+contac_nbr[0]
                        #number[0] return the primary phone number
                        #construct record
                        write_str=(",,,,"+contact[0]+",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,"+contac_nbr[0]+",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,"+"\n").encode("utf-8")
                        #append to file
                        file = open("galleryPhone.csv", "a")
                        #write number, but we need more 
                        file.write(write_str)
                        file.close()
                else:
                        print "I can not find any corresponding html element in "+ gallery_info_url
        return
                
Main()  
os.system("PAUSE")
