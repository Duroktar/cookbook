# coding: utf-8

import datetime
import time
import sys
import os
import urllib
import ctypes
import wikipedia

PATH = os.path.dirname(os.path.abspath(sys.argv[0]))
QUERY = ""


def get_input():
    global QUERY
    print "Opening dictation.txt"
    f = open(PATH + "\dictation.txt")
    print "Got it.."
    x = f.read()
    print "Reading search string.."
    print "Search string: " + x + "Closing dictation.txt"
    f.close()
    write_history(x)
    QUERY = x
    return x


def search_wiki(text):
    y = wikipedia.page(text)
    title = y.title
    summary = y.summary
    answer = "Retrieving data. {}. {}.".format(title, summary)
    return answer


def write_history(i):
    f = open(PATH + '\history.txt', 'a')
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    a = st + ": " + i
    print "Writing history: "
    print a
    print "-----------------------------"
    f.write(a)
    f.write('\n')
    f.close()


def talk(text):
    # THIS URL NEEDS TO BE SET TO YOUR PORT AND KEY ACCORDINGLY
    # THIS PART ONLY WORK IF YOU HAVE LINKS WEB REQUEST SETTINGS ON DEFAULT
    try:
        url = 'http://127.0.0.1:54657/?action=[Speak("placeholder")]&key=ABC1234&request=enable'
        newurl = url.replace("placeholder", text)  # fill in text to be spoken
        urllib.urlopen(newurl)
    except IOError:
        ctypes.windll.user32.MessageBoxA(0, "CHECK YOUR WEB SERVER SETTING IN LINKS", "Connection error", 1)


def main():
    time.sleep(.3)
    print "Starting LINKS/Wiki engine.."
    print "Success.."
    print "----------------------------"
    print "Getting User Input"
    data = get_input()
    answer = search_wiki(data)
    talk(answer)
    print answer
    return answer


main()
