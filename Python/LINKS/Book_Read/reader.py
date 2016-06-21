import urllib   # library for dealing with web stuff through Python
import os
import sys

PATH = os.path.dirname(os.path.abspath(sys.argv[0]))

Config = ConfigParser.ConfigParser()
Config.read(PATH + "\config.ini")
Config.sections()
PORT = Config.get("LINKS", 'Port')
WEBKEY = Config.get("LINKS", 'Key')


def talk(port, webkey, text):
    # THIS URL NEEDS TO BE SET TO YOUR PORT AND KEY ACCORDINGLY
    # THIS PART ONLY WORK IF YOU HAVE LINKS WEB REQUEST SETTINGS ON DEFAULT
    try:
        url = 'http://127.0.0.1:_port_/?action=[Speak("_placeholder_")]&key=_passkey_&request=enable'
        addport = url.replace("_port_", port)
        addkey = addport.replace("_passkey_", webkey)
        finalurl = addkey.replace("_placeholder_", text)  # fill in text to be spoken
        # print finalurl
        urllib.urlopen(finalurl)
    except IOError:
        print "IO Error"
        return

with open(PATH + '\dag.txt', 'r') as myfile:    # copies text to myfile
    data = myfile.read().replace(';', '')     # cleans up text a bit

print data   # Print data to screen

talk(data)           # make jarvis tell a story!
