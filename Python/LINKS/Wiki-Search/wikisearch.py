# coding: utf-8

import urllib
import datetime
import time
import sys, os
import json
import flatdict
import ctypes

PATH = os.path.dirname(os.path.abspath(sys.argv[0]))
QUERY = ""

def getInput():
    global QUERY
    print "Opening dictation.txt"
    f = open(PATH + "\dictation.txt")
    print "Got it.."
    x = f.read()
    print "Reading search string.."
    print "Search string: " + x + "Closing dictation.txt"
    f.close()
    QUERY = x
    return x


def buildUrl(_phrase):
    print "---------------"
    print "Building URL"
    phrase = _phrase.replace(" ", "+")
    url = "https://en.wikipedia.org/w/api.php?format=json&action=query&redirects=1&prop=extracts&exintro=&explaintext=&titles=_replace_"
    w_url = url.replace("_replace_", phrase)
    print "Url: " + w_url + "----------------"
    return w_url


def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)


def getJson(url):
    w_url = url
    print "Sending request"
    print "Request: " + w_url
    data = urllib.urlopen(w_url).read()
    print type(data)
    # print "Response: " + data
    print "--------------------------------------"
    print "Converting to json"
    jsonData = json.loads(data)
    print type(jsonData)
    print "--------------------------------------"
    flat = flatdict.FlatDict(jsonData)
    for key in flat:
        if "extract" in key:
            x = key
            key = flat[x]
            answer = strip_non_ascii(key)
            return answer
        else:
            return "No match found for, " + QUERY
    exit()


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
        url = 'http://127.0.0.1:54657/?action=[Speak("placeholder")]&key=1234ABC&request=enable'  #set default talk to jarvis address
        newurl = url.replace("placeholder", text)  #fill in text to be spoken
        urllib.urlopen(newurl)
    except IOError:
        ctypes.windll.user32.MessageBoxA(0, "CHECK YOUR WEB SERVER SETTING IN LINKS", "Can't communicate to links!", 1)

def main():
    time.sleep(.3)
    print "Starting LINKS/Wiki engine.."
    print "Success.."
    print "----------------------------"
    print "Getting User Input"
    data = getInput()
    url = buildUrl(data)
    resp = getJson(url)
    print "Response: " + resp
    talk(resp)


main()
