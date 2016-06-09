import urllib   # library for dealing with web stuff through Python


def talk(text):  # function to make jarvis say something USE THIS FUNCTION IN YOUR CODE
    url = 'http://127.0.0.1:54657/?action=[Speak("placeholder")]&key=1234ABC'  # set default talk to jarvis address
    newurl = url.replace("placeholder", text)      # fill in text to be spoken
    urllib.urlopen(newurl)      # send web request with new data in it

# opens text file, in this case Dagon by HP Lovecraft
with open('F:\AI\dag.txt', 'r') as myfile:    # copies text to myfile
    data = myfile.read().replace(';', '')     # cleans up text a bit

print data   # Print data to screen (prints what Jarvis will be reading to the terminal)

talk("Hello there")  # make jarvis talk (this is an example)


# UNCOMMENT NEXT LINE TO MAKE JARVIS READ THE WHOLE STORY
# talk(data)           # make jarvis tell a story!

# This uses web requests to communicate so you can use the pause and resume speech commands to make
# him stop and start again where he left off :)


