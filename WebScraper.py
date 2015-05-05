#Note: Only works with websites using HTTP on school proxy. 

import collections
import urllib2
import re
import inputbox

arrayWords = []

print "Web Scraper"
proxi = raw_input("Are you on CHS school proxy? yes or no: ")
url = raw_input("Enter URL: ")

#url = 'http://www.lipsum.com/'
if proxi == "yes":
    proxy = urllib2.ProxyHandler({'https': 'http://mitchell.dunn5:1234@10.15.138.20:8080'})
    auth = urllib2.HTTPBasicAuthHandler()
    opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler, urllib2.HTTPSHandler())
    urllib2.install_opener(opener)
else:
    pass

req = urllib2.Request("http://"+url)
resp = urllib2.urlopen(req)
respData = resp.read()

#print respData
#. = Any Character, * = 0 or more repetitions, ? = 0 or 1 repetitions
paragraphs = re.findall(r'>(.*?)<',str(respData))

for eachP in paragraphs:
    arrayWords.append(eachP)

wordstream = str(arrayWords).lower().split()

ignoredwords = ["the","to","in","on","of","and","i","a","'\\xef\\xbb\\xbf',","'&nbsp;',",
                "'',","',","'","'&#160;',","'/*',",":","[","]","-","'","&","'']"]
punctuation = [".","?","!",")","(",":",";","'s","-","[","]"]

wordstream = [item for item in wordstream if item not in ignoredwords]

for word in wordstream:
        for punct in punctuation:
            if punct in word:
                word = word.replace(punct,"")

sortedWords = collections.Counter(wordstream).most_common(50)
print sortedWords
