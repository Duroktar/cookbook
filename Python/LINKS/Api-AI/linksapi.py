#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
import json
import ConfigParser
try:
    import apiai
except ImportError:
    print "Starting initial setup."
    import subprocess
    FNULL = open(os.devnull, 'w')
    retcode = subprocess.call(['pip', 'install', 'apiai'], stdout=FNULL, stderr=subprocess.STDOUT)
    import apiai

QUERY = " ".join(sys.argv[1:])

PATH = os.path.dirname(os.path.abspath(sys.argv[0]))

try:
    Config = ConfigParser.ConfigParser()
    Config.read(PATH + "\config.ini")
    Config.sections()
    CLIENTKEY = Config.get("APIKey", 'clientkey')
    SESSION_ID = Config.get("APIKey", 'sessionid')
except Exception:
    print """There was a problem loading your config file. 
             Check that the file actually exists and
             that your a.p.i. key is entered properly."""

def main():
    ai = apiai.ApiAI(CLIENTKEY)
    request = ai.text_request()
    if SESSION_ID != "":
        request.session_id = SESSION_ID
    request.lang = 'en'
    request.query = QUERY
    response = request.getresponse()
    new_response = response.read()
    jresponse = json.loads(new_response)
    try:
        if jresponse['status']['errorDetails']:
            print "Your api client key is invalid. Please check your config file."
            return
    except:
        if SESSION_ID == "":
            key = jresponse['id']
            Config.set("APIKey", 'SessionID', key)
            with open(PATH + "\config.ini", 'w') as configfile:
                Config.write(configfile)
    if jresponse['result']['fulfillment']['speech'] == "":
        print "I don't have an answer for that"
        quit()
    else:
        response = jresponse['result']['fulfillment']['speech']
        print response.replace(';', ',').replace('"', "'").encode('utf-8')

def strip_non_ascii(string):
    """ Returns the string without non ASCII characters """
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

if __name__ == '__main__':
    main()
