#     - Example -
# c:\>python F:\JARVIS\xmlscraper.py TestVariable
# By: traBpUkciP


import requests
import urllib   # library for dealing with web stuff through Python
import sys
from xml.etree import ElementTree as ET
from lxml import html
import aiml
import os

# Fetches first argument from command line, ignores rest 
# fetch = "\n".join(sys.argv[1:]) 
tree = ET.parse('C:\Users\Charlotte\AppData\Roaming\LINKS\Customization\XML\UserVariables.xml')  #ElementTree.parse('path')
root = tree.getroot()    # Gets root index from tree
# ------------------------------------------------------

kernel = aiml.Kernel()

last = ""
# kernel.learn("std_startup.xml")
# kenel.respond("load aiml b")
if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")


def talk(text):   							 #function to make jarvis say something USE THIS FUNCTION IN YOUR CODE
    url = 'http://slayernet:54657/?action=[Speak("placeholder")]&key=1234ABC'  #set default talk to jarvis address
    newurl = url.replace("placeholder", text)      #fill in text to be spoken
    urllib.urlopen(newurl)
	

def userInput():
	for line in open("F:\JARVIS\Chatbot\Kirk_Brain\py\dictation.txt"):pass
	return line

			
def main():
	message = userInput()
	bot_response = kernel.respond(message)
	# Do something with bot_response
	talk(bot_response)      #respond with J.A.R.V.I.S.

main()


	
# Need to sync this with JARVIS


