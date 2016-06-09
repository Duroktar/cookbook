# Links - ALICE - Debug Console Logger
#
# By: traBpUkciP

import urllib   # library for dealing with web stuff through Python
import aiml
import time
import datetime
import sys, os


path = os.path.dirname(os.path.abspath(sys.argv[0]))

BRAIN_FILE = path + "/bot_brain_ALICE.brn"
# This loads the AIML Brain file
k = aiml.Kernel()
k.bootstrap(brainFile=BRAIN_FILE)


def talk(text):
    # THIS URL NEEDS TO BE SET TO YOUR PORT AND KEY ACCORDINGLY
    # THIS PART ONLY WORK IF YOU HAVE LINKS WEB REQUEST SETTINGS ON DEFAULT
    url = 'http://127.0.0.1:54657/?action=[Speak("placeholder")]&key=1234ABC'  #set default talk to jarvis address
    newurl = url.replace("placeholder", text)  #fill in text to be spoken
    urllib.urlopen(newurl)



def userInput():
    print "success"
    print "opening dictation file"
    f = open( path + "/dictation.txt")
    print "success"
    print "reading dictation file into a"
    a = f.read()
    print "success"
    print "save and close dictation file"
    f.close()
    print "success"
    print "checking if a is false"
    print "a = " + a
    if a == "False":
        print "a is false"
        return False
    else:
        print "userInput detected!"
        print "---------------------------------------------------------------------------------"
        aliceSpeak(a)

def clearInput():
    print "getting ready to set dictation file to false"
    f = open( path + '/dictation.txt', 'w')
    print "opened file"
    f.write("False")
    print "reset to false"
    f.close()
    print "clearing Inputs"



def writeHistory(i):
    print "getting ready to set history file"
    print "initializing variables"
    a = ""
    ts = ""
    print "success"
    print "opening history file"
    f = open( path + '/history.txt', 'a')
    print "success"
    print "getting timestamp"
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    print "success"
    print "creating history string"
    a = st + ": " + i
    print a
    print "success"
    print "writing that string to file"
    f.write(a)
    f.write('\n')
    print "success"
    print "saving history"
    f.close()
    print "success"
    print "back to aliceSpeak"

def aliceSpeak(feed):
    print "entering aliceSpeak function"
    print "assigning variables"
    message = feed
    print "success"
    print "recording userInput into history file"
    writeHistory(message)
    print "success"
    print "resetting all data"
    clearInput()
    print "success"
    print "asking Alice"
    bot_response = k.respond(message)
    print "success"
    print "Alice is ready to respond"
    talk(bot_response)
    print "success"
    print "looping back to main"
    main()


def main():
    print "entering main function"
    print "going to userInput function"
    while userInput() == False:
        print "check successful"
        print "no userInput detected in main, sleeping"
        time.sleep(.3)
        print "success"
        print "no input found, looping"
        continue


try:
    while True:
        main()
except KeyboardInterrupt:
    pass
























