# coding: utf-8

import urllib
import datetime
import time
import sys
import os
import json
import ctypes
import ConfigParser


PATH = os.path.dirname(os.path.abspath(sys.argv[0]))
SEARCH = ""
Config = ConfigParser.ConfigParser()
Config.read(PATH + "\config.ini")
Config.sections()
PORT = Config.get("LINKS", 'Port')
WEBKEY = Config.get("LINKS", 'Key')


def getInput():
    global SEARCH
    # print "Opening dictation.txt"
    f = open(PATH + "\dictation.txt")
    # print "Got it.."
    x = f.read()
    # print "Reading search string.."
    # print "Search string: " + x
    f.close()
    SEARCH = x
    return x


def buildUrl(x):
    phrase = x.replace(" ", "+")
    # print "---------------"
    # print "Building URL"
    url = "http://www.omdbapi.com/?t=_replace_&y=&plot=short&r=json"
    w_url = url.replace("_replace_", phrase)
    # print "Url: " + w_url + "----------------"
    return w_url


def strip_non_ascii(string):
    # Returns the string without non ASCII characters
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)


def getJson(url):
    global SEARCH
    w_url = url
    # print "Sending request"
    # print "Request: " + w_url
    data = urllib.urlopen(w_url).read()
    # print "--------------------------------------"
    # print "Converting to json:"
    jsonData = json.loads(data)
    # print jsonData
    # print "--------------------------------------"
    if jsonData['Response'] == 'False':
        return "Nothing found."
    else:
        title = jsonData['Title']
        date = jsonData['Year']
        genre = jsonData['Genre']
        directors = jsonData['Director']
        actors = jsonData['Actors']
        plot = jsonData['Plot']
        movie = "Released in {}, {} is a {} film directed by {} and starring {}. \
            The movie is summarized as follows. . {}".format(date, title, genre, directors, actors, plot)
        return movie


def writeHistory(i):
    f = open(PATH + '\history.txt', 'a')
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    a = st + ": " + i
    # print a
    f.write(a)
    f.write('\n')
    f.close()


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
        ctypes.windll.user32.MessageBoxA(0, "Check LINKS web settings under user options. "
                                            "Make sure port & key match your config file.")


def main():
    time.sleep(.3)
    # print "Starting LINKS/Wiki engine.."
    # print "Success.."
    # print "----------------------------"
    # print "Getting User Input"
    data = getInput()
    url = buildUrl(data)
    resp = getJson(url)
    talk(PORT, WEBKEY, resp)

main()
