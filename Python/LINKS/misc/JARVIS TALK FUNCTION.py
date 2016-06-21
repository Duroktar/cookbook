import urllib
import urlparse


def talk(text):
    url = 'http://localhost:54657/?action=[Speak("_replace")]&key=ABC1234'
    newurl = url.replace("_replace", text)
    urllib.urlopen(newurl)

talk("Whats up")
