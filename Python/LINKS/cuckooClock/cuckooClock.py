import pytronlinks as pytron
import time


def main():
    """ Uses Pytron library to interface with Links and act as a cuckoo clock.
      Speaking the time on the hour every hour while running silently in the background.

    """
    while True:
        try:
            cur_time = time.localtime()
            hour = cur_time.tm_hour
            min = cur_time.tm_min
            sec = cur_time.tm_sec

            if hour > 12:
                hour -= 12
            else:
                hour = hour

            if min == 59 and sec == 0:
                chime = "Cuckoo clock. It's almost {} o'clock.".format(hour)
                AI.talk(chime)

            if not min and not sec:
                chime = "Cuckoo clock. It's {} o'clock.".format(hour)
                AI.talk(chime)

            if min < 58:
                time.sleep(58 - min)
            time.sleep(0.3)
        except Exception as e:
            break

if __name__ == '__main__':
    print "Pytron Cuckoo Clock "
    print time.ctime()
    AI = pytron.Client()
    main()
