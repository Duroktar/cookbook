import urllib   # library for dealing with web stuff through Python


def talk(text):   #function to make jarvis say something USE THIS FUNCTION IN YOUR CODE
    url = 'http://slayernet:54657/?action=[Speak("placeholder")]&key=1234ABC'  #set default talk to jarvis address
    newurl = url.replace("placeholder", text)      #fill in text to be spoken
    urllib.urlopen(newurl)      #send web request with new ddata in it

# opens text file, in this case Dagon by HP Lovecraft
with open('F:\AI\dag.txt', 'r') as myfile:    # copues text to myfile (uses WITH OPEN to ensure file is closed when done)
    data = myfile.read().replace(';', '')     # cleans up text a bit

print data   # Print data to screen (essentailly shows you what Jarvis will be reading if your terminal is open

#talk("Hello there")  # make jarvis talk (this is and example)



#  UNCOMMENT NEXT LINE TO MAKE JARVIS READ THE WHOLE STORY
talk(data)           # make jarvis tell a story!

# This uses webrequest to communicate so you can use the pause and resume speech commands to make
# him stop and start again where he left off :)


