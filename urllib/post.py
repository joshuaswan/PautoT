import urllib2
import urllib

# values = {"username":"joshuaswan@sina.com","password":"XXXXXXX"}
values = {}
values['username'] = 'joshuaswan@sina.com'
values['password'] = "XXXXX"
data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)
print response.read()
# print values
