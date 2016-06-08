# coding: utf-8

import urllib
import datetime
import time
import sys
import os
import ctypes
import wikipedia

PATH = os.path.dirname(os.path.abspath(sys.argv[0]))
QUERY = ""
CONFIRM = False


def getConfirm(con):
    global CONFIRM


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


def searchWiki(text):
    x = wikipedia.search(text)
    y = wikipedia.page("Dogs")
    print "Title: "
    print y.title
    print "-----------------------------------------------------------"
    print "Content: "
    print y.content
    print "-----------------------------------------------------------"
    print "Categories: "
    print y.categories
    print "-----------------------------------------------------------"
    print "Sections: "
    print y.sections
    for section in y.sections:
        talk(section)
    print "-----------------------------------------------------------"
    print "Summary: "
    print y.summary


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


searchWiki('dogs')
