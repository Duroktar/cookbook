# coding: utf-8

import urllib
import datetime
import time
import sys
import os
import json
import ctypes

PATH = os.path.dirname(os.path.abspath(sys.argv[0]))
SEARCH = ""

def getInput():

    print "Opening dictation.txt"
    f = open(PATH + "\dictation.txt")
    print "Got it.."
    x = f.read()
    print "Reading search string.."
    print "Search string: " + x
    f.close()
    global SEARCH
    SEARCH = x
    return x


def buildUrl(x):
    phrase = x.replace(" ", "+")
    print "---------------"
    print "Building URL"
    url = "http://www.omdbapi.com/?t=_replace_&y=&plot=short&r=json"
    w_url = url.replace("_replace_", phrase)
    print "Url: " + w_url + "----------------"
    return w_url


def strip_non_ascii(string):
    # Returns the string without non ASCII characters
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)


def getJson(url):
    w_url = url
    print "Sending request"
    print "Request: " + w_url
    data = urllib.urlopen(w_url).read()
    print "--------------------------------------"
    print "Converting to json:"
    jsonData = json.loads(data)
    print jsonData
    print "--------------------------------------"
    if jsonData['Response'] == 'False':
        return "Nothing found for {}.".format(SEARCH)
    else:
        title = jsonData['Title']
        date = jsonData['Year']
        genre = jsonData['Genre']
        directors = jsonData['Director']
        actors = jsonData['Actors']
        plot = jsonData['Plot']
        movie = "Released in {}, {} is an {} film directed by {} and starring {}. \
            The movie is summarized as follows. . {}".format(date, title, genre, directors, actors, plot)
        return movie


def writeHistory(i):
    f = open(PATH + '\history.txt', 'a')
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    a = st + ": " + i
    print a
    f.write(a)
    f.write('\n')
    f.close()


def talk(text):
    # THIS URL NEEDS TO BE SET TO YOUR PORT AND KEY ACCORDINGLY
    # THIS PART ONLY WORK IF YOU HAVE LINKS WEB REQUEST SETTINGS ON DEFAULT
    try:
        url = 'http://127.0.0.1:54657/?action=[Speak("placeholder")]&key=1234ABC&request=enable'
        newurl = url.replace("placeholder", text)  # fill in text to be spoken
        urllib.urlopen(newurl)
    except IOError:
        print "LINKS web server not accepting request. Check port and key settings in user options under web settings."
        ctypes.windll.user32.MessageBoxA(0, "Check LINKS web settings under user options. Make sure port:54657 & key:1234ABC match. Copy and paste this into your browser afterwards to see if they're enabled. http://127.0.0.1:54657/?action=[Speak('Test')]&key=1234ABC&request=enable", "Can't communicate with LINKS!", 1)

def main():
    time.sleep(.3)
    print "Starting LINKS/Wiki engine.."
    print "Success.."
    print "----------------------------"
    print "Getting User Input"
    data = getInput()
    url = buildUrl(data)
    resp = getJson(url)
    talk(resp)

main()
