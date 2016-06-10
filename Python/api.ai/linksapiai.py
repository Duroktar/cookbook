#!/usr/bin/env python
# -*- coding: utf-8 -*-
import links
import sys
import json
import os
import ConfigParser
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


def main():

    ai = apiai.ApiAI(CLIENTKEY)

    request = ai.text_request()

    request.lang = 'en'  # optional, default value equal 'en'

    request.query = links.get_input()

    # print "Sending  -{}-  to api.ai ".format(request.query)
    # print "\n ===================================\n"

    links.write_history(request.query)

    response = request.getresponse()

    # print type(response)

    new_response = response.read()

    # print type(new_response)

    jresponse = json.loads(new_response)
    # print "Json: "
    # print jresponse
    # print "==================================="
    # print jresponse['result']['fulfillment']['speech']

    if jresponse['result']['fulfillment']['speech']:
        response = jresponse['result']['fulfillment']['speech']
        final = strip_non_ascii(response)
        # print "Response from api.ai: " + final
        links.talk(PORT, WEBKEY, final)
    else:
        links.talk(PORT, WEBKEY, "Sorry, no response found.")

def strip_non_ascii(string):
    """ Returns the string without non ASCII characters """
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

if __name__ == '__main__':
    main()
