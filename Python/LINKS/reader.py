import urllib   # library for dealing with web stuff through Python


def talk(text):   # function to make jarvis say something USE THIS FUNCTION IN YOUR CODE
    url = 'http://slayernet:54657/?action=[Speak("placeholder")]&key=1234ABC'  # set default talk to jarvis address
    newurl = url.replace("placeholder", text)      # fill in text to be spoken
    urllib.urlopen(newurl)      # send web request with new data in it

with open('F:\AI\dag.txt', 'r') as myfile:    # copies text to myfile
    data = myfile.read().replace(';', '')     # cleans up text a bit

print data   # Print data to screen

talk(data)           # make jarvis tell a story!




