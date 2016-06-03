# -*- coding: utf-8 -*-
import sys
import urllib2
import requests
def requsts_download(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian
    return local_filename

def urllib2_download(url):
    local_filename= url.split('/')[-1]
    with open(local_filename, 'wb') as f:
        f.write(urllib2.urlopen(url).read())
        f.close()
    print "Download Complete!"        

def urllib2_downloadX(url,local_filename):
    remote_sufix=url.split('/')[-1]
    remote_sufix=url.split('.')[-1]
    local_filename=local_filename+"."+remote_sufix
    try:
        with open(local_filename, 'wb') as f:
            f.write(urllib2.urlopen(url).read())
            f.close()
        print "Download Complete!"
    except Exception,e:
        print e
        
    
url="http://image1.shilladfs.com/files/product/2011/09/16/653510000378_20160228_13514988_ORG_92779_20110916_105133_org_653510000378%60.jpg"
urllib2_downloadX(url,"ddre")

