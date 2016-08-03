# coding: utf-8

import time
import wikipedia
import pytronlinks as Pytron


def search_wiki(text):
    SECTION_COUNT = 0
    x = wikipedia.search(text)
    y = wikipedia.page(x[0])
    sections = y.sections
    summary = y.summary
    for i in sections:
        x = y.section(i)
        if x == "":
            continue
        else:
            SECTION_COUNT += 1
            continue
    summary = AI.strip_non_ascii(summary)
    summary = AI.strip_bad_chars(summary)
    return summary


def main():
    time.sleep(.15)
    query = AI.Get('Pytron')
    result = search_wiki(query)
    AI.talk(result)
    print(result)

if __name__ == '__main__':
    AI = Pytron.Client()
    main()

