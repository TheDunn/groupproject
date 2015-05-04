import urllib2
import re

print "Web Scraper"
url = raw_input("Enter URL: ")

#url = 'http://www.lipsum.com/'

req = urllib2.Request(url)
resp = urllib2.urlopen(req)
respData = resp.read()

#. = Any Character, * = 0 or more repetitions, ? = 0 or 1 repetitions
paragraphs = re.findall(r'<p>(.*?)</p>',str(respData))

for eachP in paragraphs:
    print(eachP)
