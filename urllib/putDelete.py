import urllib2

request = urllib2.Request("http://www.baidu.com")
request.get_method = 'PUT'
# request.get_method = 'DELETE'

response = urllib2.urlopen(request)
