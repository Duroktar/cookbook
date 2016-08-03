# coding: utf-8

import time
import datetime
import os
import sys
import ConfigParser
import urllib
import pytronlinks
from cleverbot import Cleverbot



PATH = os.path.dirname(os.path.abspath(sys.argv[0]))

Config = ConfigParser.ConfigParser()
Config.read(PATH + "\config.ini")
Config.sections()
PORT = Config.get("LINKS", 'Port')
WEBKEY = Config.get("LINKS", 'Key')
ANSWER = ""
TIMEOUT = 0

cb = Cleverbot()
print "Cleverbot chat started"
print "======================"


def ask_cleverbot(query):
    global ANSWER
    global TIMEOUT
    TIMEOUT = 0
    ANSWER = cb.ask(query)
    talk(ANSWER)
    main()


def user_input():
    f = open(PATH + "/dictation.txt")
    a = f.read()
    f.close()
    if a == "":
        return False
    elif a == "end chat":
        talk("Ending chat session. Goodbye.")
        exit()
    else:
        print "================================================================"
        print "Input from LINKS detected!"
        clear_input()
        write_history(a)
        ask_cleverbot(a)


def clear_input():
    open(PATH + '/dictation.txt', 'w').close()


def write_history(i):
    f = open(PATH + '/history.txt', 'a')
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    a = st + ": " + i
    print a
    print "================================================================"
    f.write(a)
    f.write('\n')
    f.close()


def talk(text):
    # THIS URL NEEDS TO BE SET TO YOUR PORT AND KEY ACCORDINGLY
    # THIS PART ONLY WORK IF YOU HAVE LINKS WEB REQUEST SETTINGS ON DEFAULT
    try:
        url = 'http://127.0.0.1:_port_/?action=[Speak("_placeholder_")]&key=_passkey_&request=enable'
        addport = url.replace("_port_", PORT)
        addkey = addport.replace("_passkey_", WEBKEY)
        finalurl = addkey.replace("_placeholder_", text)  # fill in text to be spoken
        # print finalurl
        urllib.urlopen(finalurl)
    except IOError:
        print "IO Error"
        return


def main():
    global TIMEOUT
    print "working"
    while not user_input():  # == False:
        if TIMEOUT >= 1500:  # 3000 == 10 minutes (proportional to time.sleep(0.2)
            talk("Chat session timed out.")
            exit()
        time.sleep(0.2)
        TIMEOUT += 1
        continue


talk("Clever bot chat session initiated. Say, end chat, to end session.")

try:
    while True:
        main()
except KeyboardInterrupt:
    pass
