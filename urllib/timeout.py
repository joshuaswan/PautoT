import urllib2
import urllib

response = urllib2.urlopen("http://www.baidu.com", timeout=10)

values = {}
values['username'] = 'joshuaswan@sina.com'
values['password'] = "XXXXX"

data = urllib.urlencode(values)
response = urllib2.urlopen("http://www.baidu.com", data, 10)
