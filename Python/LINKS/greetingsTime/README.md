greetingsTime
=============

Run this in the shell tab to make links output the time when using
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

traBpUkciP