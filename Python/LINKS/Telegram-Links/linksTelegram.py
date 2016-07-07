import re
import os
import sys
import time
import datetime
import requests
import ConfigParser


PATH = os.path.dirname(os.path.abspath(sys.argv[0]))

config = ConfigParser.ConfigParser()
config.read(PATH + "\config.ini")
config.sections()
PORT = config.get("LINKS", 'Port')
WEBKEY = config.get("LINKS", 'Key')
LOGIN = config.get("Facebook", 'Login')
PASSWORD = config.get("Facebook", 'Password')
MYFBID = config.get("Facebook", 'fbid')


def get_url_by_id(user_id):
    return


def get_name_from_url(url):
    return


def search_friends(query):
    return


def send_message(who):
    return


def get_last_sent(who):
    return



"""
def user_input():
    f = open(PATH + "/dictation.txt")
    a = f.read()
    f.close()
    if a == "":
        return False
    else:
        print "=" * 20
        print "Input from LINKS detected!"
        clear_input()
        write_history(a)
        search_friends(a)
"""


def clear_input():
    open(PATH + '/dictation.txt', 'w').close()
    return


def write_history(i):
    f = open(PATH + '/history.txt', 'a')
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    a = st + ": " + i
    print a
    print "=" * 20
    f.write(a)
    f.write('\n')
    f.close()


def read_unread_messages():
    return


def get_unread_messages():
    return


# Needs PEP-8
def cleanup(dirty):
    string = str(dirty)
    bad_chars = '<>()'
    url_pattern = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    a = "".join(c for c in string if c not in bad_chars)
    b = a.strip('USER')
    friend_name = url_pattern.sub('', b)
    friend_info = friend_name
    return friend_info


def strip_non_ascii(string):
    """ Returns the string without non ASCII characters """
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)


def main():
    return


try:
    # clear_terminal_screen()
    print "***Logged in to Telegram***"
    while True:
        if __name__ == '__main__':
            main()
except KeyboardInterrupt:
    pass


