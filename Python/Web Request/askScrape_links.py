from lxml import html
import requests
import urllib
import urllib2
import datetime
import time
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

	
def talk(text):
    # THIS URL NEEDS TO BE SET TO YOUR PORT AND KEY ACCORDINGLY
    # THIS PART ONLY WORK IF YOU HAVE LINKS WEB REQUEST SETTINGS ON DEFAULT
    url = 'http://127.0.0.1:54657/?action=[Speak("placeholder")]&key=1234ABC'  #set default talk to jarvis address
    newurl = url.replace("placeholder", text)  #fill in text to be spoken
    urllib.urlopen(newurl)

def userInput():
    f = open("dictation.txt")
    a = f.read()
    f.close()
    if a == "False":
        return False
    else:
        print "---------------------------------------------------------------------------------"
        print "Input from LINKS detected!"
        getAnswer(a)

def clearInput():
    f = open('dictation.txt', 'w')
    f.write("False")
    f.close()

def writeHistory(i):
    f = open('history.txt', 'a')
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    a = st + ": " + i
    print a
    print "---------------------------------------------------------------------------------"
    f.write(a)
    f.write('\n')
    f.close()


	
# builds url
def buildUrl(_phrase):
	url = "http://www.ask.com/web?q="
	phrase = _phrase.replace(" ", "+")
	w_url = url + phrase
	return w_url

# reads html
def getAnswer(feed):
	message = feed
	writeHistory(message)
	clearInput()
	w_url = buildUrl(message)
	data = urllib2.urlopen(w_url)
	html = data.read()
	try:
		soup = BeautifulSoup(html)
		answer = soup.body.find('div', attrs={'class':'sa_abstract'}).text
		print answer
		talk(answer)
	except(AttributeError, TypeError, KeyError) as e:
		try:
			answer = soup.body.find('span', attrs={'class':'sa_headline'}).text
			print answer
			talk(answer)
		except(AttributeError, TypeError, KeyError) as e:
			print "no tags found on ask.com"
			
def main():
    while userInput() == False:
        time.sleep(.1)
        print "working"
        continue
		
try:
    while True:
        main()
except KeyboardInterrupt:
    pass