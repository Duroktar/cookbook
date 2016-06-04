from lxml import html
import requests
import urllib2
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

# builds url
url = "http://www.ask.com/web?q="
_phrase = "yes it is" 
phrase = _phrase.replace(" ", "+")
w_url = url + phrase
print w_url

# reads html
data = urllib2.urlopen(w_url)
html = data.read()

# finds answer
parsed_html = BeautifulSoup(html)
print parsed_html.body.find('span', attrs={'class':'sa_headline'}).text

	
	



