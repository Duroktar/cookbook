Wikipedia Reader
================
Make Links smarter than ever with the power of Wikipedia!

Download & Install Instructions
-------------------------------
 - Install Python 2.7 and add C:\Python27 and C:\Python27\Scripts to your system path.
   - *How to add Python to windows path* - https://docs.python.org/2/using/windows.html 
 - Download wikisearch.zip and unzip into Links scripts folder.
 - Create your new Shell Tab command!

Links Shell Command
--------------
 **Command goes in LINKS Shell tab**
 - **Command:** Search wikipedia for {that=test_dictation}
 - **Response:** {{!Action!}}
 - **Action:** -ret"python" "%AppData%\LINKS\Customization\Scripts\wikisearch.py" "{that}"
 - **Profile:** main

**SYNTAX IS VERY IMPORTANT. Copy and paste to be sure.**

Usage example
-------------
 - **User:** search wikipedia for Coffee
 - **LINKS:** Searching..

Links will then read a summary of your search which can be paused and resumed using the respective default commands.
Github

Dependancies
------------
 - **MVC: Links Mark II Ai** - *http://mega-voice-command.com/index.html*
 - **Python 2.7** - *https://www.python.org/download/releases/2.7/*
 - **Wikipedia library** - *pip install wikipedia*

Credits
-------
Created by: traBpUkciP

<a href='https://ko-fi.com/A5034CT' target='_blank'><img height='32' style='border:0px;height:32px;' src='https://az743702.vo.msecnd.net/cdn/kofi2.png?v=a' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a> 

Let me know if you have any requests/questions/complaints and I'll try to get to you all as soon as I can. Have fun :) 
