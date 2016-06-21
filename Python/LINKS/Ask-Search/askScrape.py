import urllib
import datetime
import time
try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup


def talk(text):
    # THIS URL NEEDS TO BE SET TO YOUR PORT AND KEY ACCORDINGLY
    # THIS PART ONLY WORK IF YOU HAVE LINKS WEB REQUEST SETTINGS ON DEFAULT
    text = strip_bad_chars(text)
    url = 'http://127.0.0.1:54657/?action=[Speak("_placeholder")]&key=ABC1234'  # set default talk to jarvis address
    newurl = url.replace("_placeholder", text)  # fill in text to be spoken
    urllib.urlopen(newurl)


def user_input():
    f = open("dictation.txt")
    a = f.read()
    f.close()
    if a == "False":
        return False
    else:
        print "---------------------------------------------------------------------------------"
        print "Input from LINKS detected!"
        get_answer(a)


def clear_input():
    f = open('dictation.txt', 'w')
    f.write("False")
    f.close()


def write_history(i):
    f = open('history.txt', 'a')
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    a = st + ": " + i
    print a
    print "---------------------------------------------------------------------------------"
    f.write(a)
    f.write('\n')
    f.close()


def build_url(_phrase):
    url = "http://www.ask.com/web?q="
    phrase = _phrase.replace(" ", "+")
    w_url = url + phrase
    return w_url


def get_answer(feed):
    message = feed
    write_history(message)
    clear_input()
    w_url = build_url(message)
    data = urllib.urlopen(w_url)
    page = data.read()
    soup = BeautifulSoup(page)

    """
    try:
        test = soup.find_all('span', class_='sa_headline').text   # (div='sa_headline')
        print test
    except TypeError as e:
        print e
    """

    try:
        test = str(soup.findAll('div', attrs={'class': 'sa_headline_block'}))
        test2 = remove_html_markup(test)
        print strip_bad_chars(test2)
        talk(strip_bad_chars(test2))
        main()
    except Exception as e:
        print e

    try:
        answer = soup.find('div', attrs={'class': 'sa_abstract'}).text
        print answer
        talk(answer)
    except(AttributeError, TypeError, KeyError):
        try:
            answer = soup.find('span', attrs={'class': 'sa_headline'}).text
            print answer
            talk(answer)
        except(AttributeError, TypeError, KeyError):
            print "no tags found on ask.com"
    main()


def strip_bad_chars(string):
    bad_chars = '":;/{}<>[]'
    a = "".join(c for c in string if c not in bad_chars)
    b = a.replace('=', 'equals')
    return b


def remove_html_markup(s):
    tag = False
    quote = False
    out = ""

    for c in s:
            if c == '<' and not quote:
                tag = True
            elif c == '>' and not quote:
                tag = False
            elif (c == '"' or c == "'") and tag:
                quote = not quote
            elif not tag:
                out = out + c

    return out


def main():
    print "working"
    while not user_input():
        time.sleep(.2)
        continue


if __name__ == '__main__':
    main()
