import urllib2

url = "http://www.ask.com/web?q="
phrase = "butterfly" 


w_url = url + phrase
data = urllib2.urlopen(w_url)
html = data.read()


print html
