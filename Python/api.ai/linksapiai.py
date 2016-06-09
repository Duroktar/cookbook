#!/usr/bin/env python
# -*- coding: utf-8 -*-
import links
import sys
import json
import os
try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

CLIENT_ACCESS_TOKEN = 'd90d496b98f6425bad5bbdee8b1ee1b2'


def main():
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    request.lang = 'en'  # optional, default value equal 'en'
    
    """ 
    This is where the user input comes in. 
    Uncomment links.get_input() and delete "How are you today"
    once integrated into links.
    """
    request.query = "How are you today?"  # links.get_input()

    print "Sending  -{}-  to api.ai ".format(request.query)
    print "\n ===================================\n"

    links.write_history(request.query)

    response = request.getresponse()

    # print type(response)

    new_response = response.read()

    # print type(new_response)

    jresponse = json.loads(new_response)
    # print "Json: "
    # print jresponse
    # print "==================================="
    print jresponse['result']['fulfillment']['speech']

    if jresponse['result']['fulfillment']['speech']:
        final = jresponse['result']['fulfillment']['speech']
        print "Response from api.ai: " + final
        links.talk(final)
    else:
        print "Exception"



if __name__ == '__main__':
    main()














