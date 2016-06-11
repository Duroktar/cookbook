# coding: utf-8

import urllib
import datetime
import time
import sys
import os
import ctypes
import wikipedia
import ConfigParser

PATH = os.path.dirname(os.path.abspath(sys.argv[0]))
QUERY = ""
CONFIRM = False
SECTION_COUNT = 0
Config = ConfigParser.ConfigParser()
Config.read(PATH + "\config.ini")
Config.sections()
PORT = Config.get("LINKS", 'Port')
WEBKEY = Config.get("LINKS", 'Key')


def get_confirm(self):
    global CONFIRM
    return self


def get_input():
    global QUERY
    # print "Opening dictation.txt"
    f = open(PATH + "\dictation.txt")
    # print "Got it.."
    x = f.read()
    # print "Reading search string.."
    # print "Search string: " + x + "Closing dictation.txt"
    f.close()
    QUERY = x
    return x


def search_wiki(text):
    x = wikipedia.search(text)
    # print x
    # print x[0]
    y = wikipedia.page(x[0])
    # print y
    title = y.title
    sections = y.sections
    summary = y.summary
    # print "Search results:"
    # print x
    # print "------------------------------------------------------------------------------------------------"
    # print "Title: "
    # print title
    # print "--------------------------------------------------------------------------------------------------"
    # print "Sections: The new way.."
    # print type(sections)
    for i in sections:
        global SECTION_COUNT
        x = y.section(i)
        if x == "":
            continue
        else:
            # print "----------------------------------------------------------------------------------------------"
            # print "{}: ".format(i)
            # print x.strip()
            # print type(x)
            SECTION_COUNT += 1
            continue
    # print "------------------------------------------------------------------------------------------------"
    # print "Summary: "
    return summary


def write_history(i):
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
        print finalurl
        urllib.urlopen(finalurl)
    except IOError:
        talk(PORT, WEBKEY, "LINKS web server not accepting request. "
                           "Check port and key settings in user options under web settings.")
        ctypes.windll.user32.MessageBoxA(0, "Check LINKS web settings under user options. "
                                            "Make sure port & key match your config file.")


def strip_non_ascii(string):
    """ Returns the string without non ASCII characters """
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

def strip_bad_chars(string):
    bad_chars = '"=:;/{}<>'
    a = "".join(c for c in string if c not in bad_chars)
    return a


def main():
    time.sleep(.15)
    # print "Starting LINKS/Wiki engine.."
    # print "----------------------------"
    initial = get_input()
    search = search_wiki(initial)
    strip = strip_non_ascii(search)
    clean = strip_bad_chars(strip)
    answer = str(clean)
    # print answer
    # print type(answer)
    # print "==============================="
    talk(PORT, WEBKEY, answer)


#  talk(PORT, WEBKEY, "hello")
main()
