import urllib2

req = urllib2.Request("http://blog.csdn.net/cqcre")
try:
    urllib2.urlopen(req, timeout=5)
except urllib2.HTTPError, e:
    if hasattr(e, "reason"):
        print e.code
except urllib2.URLError, e:
    print e.reason
else:
    print "OK"
