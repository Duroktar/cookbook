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
SECTION_COUNT = 0


def get_confirm(self):
    global CONFIRM
    return self


def get_input():
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


def search_wiki(text):
    x = wikipedia.search(text)
    y = wikipedia.page(text)
    title = y.title
    sections = y.sections
    summary = y.summary
    print "Search results:"
    print x
    print "------------------------------------------------------------------------------------------------"
    print "Title: "
    print title
    print "--------------------------------------------------------------------------------------------------"
    print "Sections: The new way.."
    print type(sections)
    for i in sections:
        global SECTION_COUNT
        x = y.section(i)
        if x == "":
            continue
        else:
            print "----------------------------------------------------------------------------------------------"
            print "{}: ".format(i)
            print x.strip()
            print type(x)
            SECTION_COUNT += 1
            continue
    print "------------------------------------------------------------------------------------------------"
    print "Summary: "
    print summary


def write_history(i):
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
    print "----------------------------"
    # x = get_input()
    # y = search_wiki(x)


search_wiki("horses")
