import time


def main():
    """ Run this in the shell tab to make links output the time when using
      more than one wordlist in the command & response. See example..


    :Example:

    Place greetingsTime.py in the Links scripts folder.
      ( ie: %AppData%\LINKS\Customization\Scripts\ )

    Command: {greet=test_greetings} what time is it?
    Resonse: {{greet}}. It's {{!Action!}}.
    Action: -ret"python" "%AppData%\LINKS\Customization\Scripts\greetingsTime.py"
    Profile: Main

    Example usage -
        User: Good afternoon, what time is it?
        Links: Morning. It's 8:20am.

    """
    try:
        
        cur_time = time.localtime()
        hour = cur_time.tm_hour
        min_ = cur_time.tm_min
        # sec = cur_time.tm_sec

        if hour > 12:
            hour -= 12
            chime = "{}:{}am".format(hour, min_)
        else:
            hour = hour
            chime = "{}:{}pm".format(hour, min_)
            
        print chime

        # AI.talk(chime)

    except Exception as e:
        pass

if __name__ == '__main__':
    main()
