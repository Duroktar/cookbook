#  - LINKS - ALICE Bot
#
# By: traBpUkciP (2016)


import aiml     # AI-Markup Language library
import datetime
import time
import urllib   # library for dealing with web stuff through Python
import sys, os


path = os.path.dirname(os.path.abspath(sys.argv[0]))

BRAIN_FILE = path + "/bot_brain_ALICE.brn"
k = aiml.Kernel()
k.bootstrap(brainFile=BRAIN_FILE)


def talk(text):
    # THIS URL NEEDS TO BE SET TO YOUR PORT AND KEY ACCORDINGLY
    # THIS PART ONLY WORK IF YOU HAVE LINKS WEB REQUEST SETTINGS ON DEFAULT
    url = 'http://localhost:54657/?action=[Speak("' + text + '")]&key=1234ABC'  #set default talk to jarvis address
    #newurl = url.replace("placeholder", text)  #fill in text to be spoken
    urllib.urlopen(url)

def userInput():
    f = open( path + "/dictation.txt")
    a = f.read()
    f.close()
    if a == "False":
        return False
    else:
        print "---------------------------------------------------------------------------------"
        print "Input from LINKS detected!"
        aliceSpeak(a)

def clearInput():
    f = open( path + '/dictation.txt', 'w')
    f.write("False")
    f.close()

def writeHistory(i):
    f = open( path + '/history.txt', 'a')
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    a = st + ": " + i
    print a
    print "---------------------------------------------------------------------------------"
    f.write(a)
    f.write('\n')
    f.close()

def aliceSpeak(feed):
    message = feed
    writeHistory(message)
    clearInput()
    bot_response = k.respond(message)
    talk(bot_response)
    main()


def main():
    while userInput() == False:
        time.sleep(.1)
        print "working"
        continue

try:
    while True:
        main()
except KeyboardInterrupt:
    pass























