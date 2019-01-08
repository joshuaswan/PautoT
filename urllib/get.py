import urllib2
import urllib

values = {}
values['username'] = 'joshuaswan@sina.com'
values['password'] = "XXXXX"
data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login"
geturl = url + "?" + data
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)
print response.read()
print geturl
print url + "/" + data
