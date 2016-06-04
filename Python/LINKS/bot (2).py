#     - Example -
# c:\>python F:\JARVIS\xmlscraper.py TestVariable
# By: traBpUkciP


import requests
import urllib   # library for dealing with web stuff through Python
import sys
from xml.etree import ElementTree as ET
from lxml import html
import aiml

# Fetches first argument from command line, ignores rest 
fetch = "\n".join(sys.argv[1:]) 
tree = ET.parse('C:\Users\Charlotte\AppData\Roaming\LINKS\Customization\XML\UserVariables.xml')  #ElementTree.parse('path')
root = tree.getroot()    # Gets root index from tree
# ------------------------------------------------------

kernel = aiml.Kernel()

# kernel.learn("std_startup.xml")
# kenel.respond("load aiml b")
if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")


while !signal:
    message = fetch
    if message == "save":
        kernel.saveBrain("bot_brain.brn")
    else:
        bot_response = kernel.respond(message)
        # Do something with bot_response
		talk(bot_response)

def signal(varName):   #Declare function
    for each in root.findall('Variable'):    # Find all data indexed under 'Variable'
        value = each.find('Value').text      # Find 'Value' of each (optional)
        name = each.find('Name').text        # Find 'Name' of each (optional)
        if name == varName:                  # Check if matches command argument 'varName'
            print(value)                     # Prints results to screen

 
def talk(text):   #function to make jarvis say something USE THIS FUNCTION IN YOUR CODE
    url = 'http://slayernet:54657/?action=[Speak("placeholder")]&key=1234ABC'  #set default talk to jarvis address
    newurl = url.replace("placeholder", text)      #fill in text to be spoken
    urllib.urlopen(newurl) 





# Need to sync this with JARVIS


