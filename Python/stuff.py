import urllib
import urlparse



def talk(text):
    url = 'http://127.0.0.1:54657/?action=[Speak("replace")]&key=1234ABC'
    newurl = url.replace("replace", text)
    urllib.urlopen(newurl)

talk("Whats up")