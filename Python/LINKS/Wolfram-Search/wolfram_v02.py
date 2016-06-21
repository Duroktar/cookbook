# coding: utf-8
import time
import datetime
import os
import sys
import ConfigParser
import urllib
import wolframalpha

PATH = os.path.dirname(os.path.abspath(sys.argv[0]))

Config = ConfigParser.ConfigParser()
Config.read(PATH + "\config.ini")
Config.sections()
PORT = Config.get("LINKS", 'Port')
WEBKEY = Config.get("LINKS", 'Key')
IP = Config.get("LINKS", 'Ip')
WOLFKEY = Config.get("Wolfram", 'Key')

ANSWER = ""
category = ""
definition = ""


def ask_wolf(query):
    global ANSWER
    global category
    global definition
    ANSWER = ""
    category = ""
    definition = ""
    wolfie = wolframalpha.Client(WOLFKEY)
    ANSWER = wolfie.query(query)
    for pod in ANSWER.pods:
        title = pod.title
        print pod.title
        if title == "Definition":  # or "Notable Facts" or "Definitions"
            category = "The Definition"
            definition = pod.text
        elif title == "Notable facts":
            category = "The Notable facts"
            definition = pod.text
        elif title == "Definitions":
            category = "The Definitions"
            definition = pod.text
        elif title == "Result":
            category = "The Result"
            definition = pod.text
        elif title == "Exact result":
            category = "The Result"
            definition = pod.text
        elif title == "Input interpretation":
            category = "Some useful facts"
            definition = pod.text
        elif pod.text:
            print pod.text
        else:
            print "========================================="
            print "         No useful data found           ="
            print "========================================="
    if definition != "":
        links = "{} of {}, {}.".format(category, query, definition)
        split_list = links.split()
        while '|' in split_list:
            split_list.remove('|')
        while 'noun' in split_list:
            split_list.remove('noun')
        while 'interjection' in split_list:
            split_list.remove('interjection')
        while 'verb' in split_list:
            split_list.remove('verb')
        join_list = ' '.join(split_list)
        print links
        talk(join_list)
        main()
    else:
        print "No useful data found"
        talk("No useful data found")
        main()
    main()


def user_input():
    f = open(PATH + "/dictation.txt")
    a = f.read()
    f.close()
    if a == "False":
        return False
    else:
        print "========================================="
        print "Input from " + AINAME + " accepted!"
        print "Input from " + NAME + " accepted!"
        print "A script by Scott Doucet A.K.A traBpUkciP"
        write_history(a)
        clear_input()
        ask_wolf(a)
        url = 'http://' + IP + ':' + PORT + '/?action=[Speak("_placeholder_")]&key=' + WEBKEY + '&request=enable'
        finalurl = url.replace("_placeholder_", "Input accepted. Wait, fetching information...")
        urllib.urlopen(finalurl)


def clear_input():
    f = open(PATH + '/dictation.txt', 'w')
    f.write("False")
    f.close()


def write_history(i):
    f = open(PATH + '/history.txt', 'a')
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    a = st + ": " + i
    print a
    print "========================================="
    f.write(a)
    f.write('\n')
    f.close()


def talk(text):
    # THIS URL NEEDS TO BE SET TO YOUR PORT AND KEY ACCORDINGLY
    # THIS PART ONLY WORK IF YOU HAVE LINKS WEB REQUEST SETTINGS ON DEFAULT
    try:
        url = 'http://' + IP + ':' + PORT + '/?action=[Speak("_placeholder_")]&key=' + WEBKEY + '&request=enable'
        finalurl = url.replace("_placeholder_", text)  # fill in text to be spoken
        # print finalurl
        urllib.urlopen(finalurl)
    except (TypeError, IOError, Exception):
        print "Exception in talk function"
        return


def strip_non_ascii(string):
    """ Returns the string without non ASCII characters """
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)


def strip_bad_chars(string):
    bad_chars = '[]=^_'
    a = "".join(c for c in string if c not in bad_chars)
    a = a.replace("~~", " approximately ")
    a = a.replace(";", ",")
    return a


def encode_squares(text):
    x = text.replace("sqrt", "square root of ")
    return x


def main():
    print "========================================="
    print "=           Detecting input...          =" 
    print "========================================="
    while not user_input():  # == False:
        time.sleep(0.3)
        continue

try:
    while True:
        main()
except KeyboardInterrupt:
    pass
