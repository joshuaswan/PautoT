import urllib2
import urllib

url = "http://www.baidu.com"
user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"

values = {}
values['username']='joshuaswan@sina.com'
values['password'] = "XXXXX"
headers = {"User-Agent":user_agent}

data = urllib.urlencode(values)
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
page = response.read()
print page