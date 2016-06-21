import urllib
import urlparse


def talk(text):
    url = 'http://slayernet:54657/?action=[Speak("replace")]&key=1234ABC'
    newurl = url.replace("replace", text)
    urllib.urlopen(newurl)

talk("Whats up")