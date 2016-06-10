# coding: utf-8


def get_input():
    print "Opening dictation.txt"
    f = open(PATH + "\dictation.txt")
    print "Got it.."
    x = f.read()
    print "Reading search string.."
    print "Search string: " + x + "Closing dictation.txt"
    f.close()
    print "Writing history"
    return x


def build_url(_phrase):
    print "---------------"
    print "Building URL"
    phrase = _phrase.replace(" ", "+")
    url = "https://en.wikipedia.org/w/api.php?format=json&action=query&redirects=1" \
          "&prop=extracts&exintro=&explaintext=&titles=_replace_"
    w_url = url.replace("_replace_", phrase)
    print "Url: " + w_url + "----------------"
    return w_url


def write_history(i):
    f = open(PATH + '\history.txt', 'a')
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    a = st + ": " + i
    print a
    f.write(a)
    f.write('\n')
    f.close()


def talk(text):
    # THIS URL NEEDS TO BE SET TO YOUR PORT AND KEY ACCORDINGLY
    # THIS PART ONLY WORK IF YOU HAVE LINKS WEB REQUEST SETTINGS ON DEFAULT
    try:
        url = 'http://127.0.0.1:54657/?action=[Speak("placeholder")]&key=ABC1234&request=enable'
        newurl = url.replace("placeholder", text)  # fill in text to be spoken
        urllib.urlopen(newurl)
    except IOError:
        ctypes.windll.user32.MessageBoxA(0, "CHECK YOUR WEB SERVER SETTING IN LINKS", "Connection error", 1)