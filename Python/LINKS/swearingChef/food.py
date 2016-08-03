from __future__ import division
import os, sys
import itertools
import requests
import getpass
import random
import pytronlinks as pytron
import ConfigParser


PATH = os.path.dirname(os.path.abspath(sys.argv[0]))
Config = ConfigParser.ConfigParser()
Config.read(PATH + "\config.ini")
Config.sections()
CONFIG_PORT = Config.get("LINKS", 'Port')
CONFIG_WEBKEY = Config.get("LINKS", 'Key')
KEY = None
try:
    CONFIG_APIKEY = Config.get("food2fork", 'Key')
    if CONFIG_APIKEY:
        KEY = CONFIG_APIKEY
except Exception as e:
    pass


AI = pytron.Client()
random.seed()


def reverse_enumerate(iterable):
    """
    Enumerate over an iterable in reverse order while retaining proper indexes
    """
    return itertools.izip(reversed(range(len(iterable))), reversed(iterable))

print("     *** Welcome to the bad ass motherfucking recipe finder!!! ***")
AI.talk("Welcome to the badass motherfucking recipe finder!!!")
print("            -Powered by the motherfucking food2fork API- \n")
AI.talk("-Powered by the motherfucking food to fork API!!")


if not KEY:
    print("           **Enter yo muthafuckin' food2fork API key !!** ")
    AI.talk("Enter your food to fork API key motherfucker!!")
    while True:
        KEY = getpass.getpass(">>> ")
        if not KEY or len(KEY) < 10:
            print("       *** QUIT MESSING AROUND YOU CLUMSY ASS MOTHERFUCKER!! ***")
            AI.talk("       *** QUIT MESSING AROUND, YOU CLUMSY ASS MOTHERFUCKER!! ***")
            continue
        else:
            break

search = "http://food2fork.com/api/search?key={}&q=".format(KEY)
recipe = "http://food2fork.com/api/get?key={}&rId=".format(KEY)

while True:
    try:
        print("      *** Now give me some fucking ingredients to work with!! ***")
        AI.talk("Now give me some ingredients to work with you silly motherfucker!!")
        q = input(">>> ")
        if q == 'q':
            quit()
        speech = "{}?. Good choice you crazy bastard.".format(str(q))
        AI.talk(speech)
        url = "{}{}".format(search, q)
        r = requests.get(url)
        j = r.json()

        if not j['count']:
            print("        *** PICK SOMETHING BETTER ASS HAT!!! ***")
            AI.talk("PICK SOMETHING BETTER ASS HAT!!!")
            continue

        while True:
            try:
                for index, elem in enumerate(j['recipes']):
                    try:
                        print(index, elem['title'].encode('ascii'))
                    except Exception as e:
                        print(str(index) + " UNKNOWN MOTHERFUCKER!")

                while True:
                    AI.talk("Now take your pick motherfucker!")
                    print(" -Take your pick motherfucker! [0] or [q]uit " or '0')
                    q = input(">>> ") or '0'
                    if q == 'q':
                        quit()
                    if not q.isdigit():
                        print("      *** PICK A NUMBER MOTHERFUCKER!! ***")
                        AI.talk("YOU GOTTA PICK A NUMBER MOTHERFUCKER!!")
                        continue
                    elif int(q) > int(j['count']):
                        print("   *** THAT'S NOT A VAILD SELECTION MOTHERFUCKER!!! ***")
                        AI.talk("YOU GOTTA PICK A NUMBER MOTHERFUCKER!!")
                        continue
                    else:
                        break

                AI.emulate_speech('stop talking')

                rId = j['recipes'][int(q)]['recipe_id']
                url2 = "{}{}".format(recipe, rId)
                try:
                    r2 = requests.get(url2)
                    j2 = r2.json()
                except Exception as e:
                    print("   *** SOMETHING WENT WRONG MOTHERFUCKER!!! ***")

                print("        - INGREDIENTS LIST FOR YA MOTHERFUCKER! -")
                title = str(j2['recipe']['title'])
                title_speech = [
                    "Good, fucking, choice. ",
                    "Couldn't have picked a better one myself you sly motherfucker!",
                    "Wow. Just fucking wow. I was gonna pick that one you magical motherfucker!",
                    "Sounds like a party.",
                    "Hot fucking dog man! You're a real fucking winner ain't ya?",
                    "Can I axe you something? Are you in my fucking mind right now?",
                ]
                title_speech_ending = [
                    "Anyways. Here's what you're gonna need to put all this fucking shit together.",
                    "Now get your fucking shoes on fam, we're gone to the kitchen!",
                    "Now get your ass to the kitchen cause shit's about tho get lit!",
                    "Now get in the motherfucking kitchen and grab apron motherfucker!",
                    "So I hope you ready for some fire son, sheeit.",
                ]
                a = random.choice(title_speech)
                b = random.choice(title_speech_ending)
                speech = a + " " + b
                AI.talk(speech)
                print(j2['recipe']['title'])

                for words in j2['recipe']['ingredients']:
                    try:
                        if words:
                            amounts = [
                                'pound', 'cups', 'tablespoons', 'teaspoons',
                                'pounds', 'cup', 'tablespoon', 'teaspoon',
                                'cloves', 'clove', 'strips', 'slices', 'tsp',
                            ]

                            slang = [
                                'motherfucking', 'fucking', 'huge ass',
                                'god damn', 'shitty old', 'fucking dirty old',
                                'old shitty', 'dirty old fucking', 'dirty old',
                            ]

                            slang_after = [
                                'of fucking', 'of some fucking',
                                'of shitty old', 'of dirty old',
                                'of expired', 'of moldy',

                            ]

                            post = [
                                ' Which is a shit ton.', ' And believe me. thats a fuck ton.',
                                ' Holy fuck thats a lot.', ' Because who cares about looking good right?',
                            ]
                            word_list = words.split()
                            # it = iter(enumerate(word_list))
                            for i, word in reverse_enumerate(word_list):
                                if word in amounts:
                                    random.seed()
                                    rndm = random.random()
                                    if rndm <= 0.40:
                                        curse = random.choice(slang)
                                        word_list.insert(i, curse)
                                        # next(islice(it, 1, 1), None)
                                    elif rndm >= 0.60:
                                        curse = random.choice(slang_after)
                                        if word_list[i + 1] == 'of':
                                            word_list[i + 1].pop()
                                        word_list.insert(i + 1, curse)
                                        # next(islice(it, 1, 1), None)

                            if 'cups' and 'sugar' in word_list:
                                f = word_list[0]
                                if f[0].isdigit() and int(f[0]) > 2:
                                    word_list.append(random.choice(post))

                            words = " ".join(word_list)
                            print(words)
                            AI.talk(words)
                    except Exception as e:
                        print(e)

                finale = [
                    "Put all that shit together and BAM motherfucker. - You got some bad ass motherfucking",
                    """Well I'll be fucking damned. You made it this far you dense bastard And here I thought
                        you wouldn't even make past the fucking title. Congratulations. You just made """,
                    "Mix it all up. Stir it around a bit. Shit in it. I don't give a fuck. It ain't my ",
                    "How about that. You did good motherfucker. That's some good ass looking",
                    "At this point if any of it looks edible you did better than me. So good for you bastard.",
                ]
                end_speech = random.choice(finale) + " " + title
                AI.talk(finale)
                print("        - NOW THAT'S IT MOTHERFUCKER!! - ")

                AI.talk("Now. Pick again for fucks sake. Or search for something totally fucking different.!")
                x = input(" -Pick again or search something else motherfucker!! - [q]uit [s]earch [p]ick ") or 'p'
                AI.emulate_speech('stop talking')
                if x[0] == 'q':
                    print("      ***QUITTER!!! Have a great fucking day!!***")
                    AI.talk("FUCKING QUITTER!!! Well that's ok.. I'll be seeing you again real soon anyways. Ha-ha-ha!!")
                    quit()
                if x[0] == 's':
                    print(' SEARCH AGAIN MOTHERFUCKER!!!')
                    break
                if x[0] == 'p':
                    continue
                else:
                    continue
            except Exception as e:
                print(e)
                print("  *** MAKE SOME SENSE MOTHERFUCKER!!! ***")
                AI.talk("MAKE SOME SENSE MOTHERFUCKER!!!")
                input("")

    except Exception as e:
        print(">>> MOTHERFUCKER I AIN'T GOT ALL DAY!!")
        AI.talk("MOTHERFUCKER I AIN'T GOT ALL DAY!!")
