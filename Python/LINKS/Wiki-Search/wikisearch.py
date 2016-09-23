# coding: utf-8
import os, sys
import time
try:
    import wikipedia
except ImportError:
    print "Starting initial setup."
    import subprocess
    FNULL = open(os.devnull, 'w')
    retcode = subprocess.call(['pip', 'install', 'wikipedia'], stdout=FNULL, stderr=subprocess.STDOUT)
    import wikipedia
    
query = sys.argv[1:]

def main():
    time.sleep(.05)
    result = search_wiki(query)
    print(result)

def search_wiki(text):
    x = wikipedia.search(text)
    y = wikipedia.page(x[0])
    summary = y.summary.replace(';', ',').replace('"', "'").encode('utf-8')
    return summary    
    
if __name__ == '__main__':
    main()

