import urllib2

request = urllib2.Request('http://www.joshuaswan.com')
try:
    urllib2.urlopen(request, timeout=10)
except urllib2.URLError, e:
    print e.reason
