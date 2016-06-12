#!/usr/bin/env python
# -*- coding: utf-8 -*-
import links
import sys
import json
import os
import ConfigParser
from iniparse import INIConfig

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai


PATH = os.path.dirname(os.path.abspath(sys.argv[0]))

Config = ConfigParser.ConfigParser()
Config.read(PATH + "\config.ini")
Config.sections()
PORT = Config.get("LINKS", 'Port')
WEBKEY = Config.get("LINKS", 'Key')
CLIENTKEY = Config.get("APIKey", 'ClientKey')
DEVKEY = Config.get("APIKey", 'DevKey')
SESSION_ID = Config.get("APIKey", 'SessionID')


def main():
    ai = apiai.ApiAI(CLIENTKEY)
    request = ai.text_request()
    print "Session: " + SESSION_ID
    if SESSION_ID != "":
        print "ID: " + SESSION_ID
        request.session_id = SESSION_ID
    request.query = links.varfetch("LastSubject")
    # print SESSION_ID
    # print "Sending  -{}-  to api.ai ".format(request)
    # print "\n ===================================\n"
    links.write_history(request.query)
    response = request.getresponse()
    # print type(response)
    new_response = response.read()
    # print type(new_response)
    jresponse = json.loads(new_response)
    # print type(jresponse)
    # print "Json: "
    # print jresponse
    # print "==================================="
    # print jresponse['result']['fulfillment']['speech']
    if SESSION_ID == "":
        key = jresponse['id']
        cfg = INIConfig(open(PATH + "\config.ini"))
        cfg.APIKey.SessionID = " " + key
        f = open(PATH + "\config.ini", 'w')
        print >> f, cfg
        f.close()

    try:
        if jresponse['status']['errorDetails']:
            print "Your api client key is invalid. Please check your settings in the config file."
            return
    except:
        if jresponse['result']['fulfillment']['speech'] == "":
            print "Nothing found for that query."
            return
        else:
            response = jresponse['result']['fulfillment']['speech']
            final = strip_non_ascii(response)
            print final
            # links.talk(PORT, WEBKEY, final)
    """
    if 'result''fulfillment''speech' in jresponse:
            r
"""

def session_key():
    return

def strip_non_ascii(string):
    """ Returns the string without non ASCII characters """
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

if __name__ == '__main__':
    main()
