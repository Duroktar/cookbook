~LINKS APi.ai plugin /Python~
  

Instructions:
1. Unpack zip file.
2. Open config file and fill in your port and key.
 (The SessionID can be left blank. It auto fills on the first connection)
3. Enter these custom commands into links.
 Command: Smart bot {that=test_dictation}
 Response:
 Action: -hi1CMD /m /c "echo {that} > **PATH_TO_INSTALL_FOLDER**\dictation.txt | **PATH_TO_INSTALL_FOLDER**\linksapiai.exe"
4. Keeps track of session ID! (See config file)
5. Have fun :)
*. See below for instructions to run in pure Python.

  Example Session -
   User: Smart bot what's the weather in Boston?
   APi.ai bot: The weather in Boston is blah, blah...

*Remember APi.ai bots (agents) need to be programmed to do stuff before they're
really useful. This merely acts as a means of voice interaction with the API.*  


**IF YOU WANT TO RUN AS A PYTHON FILE AND NOT EXE**
 You need to get the ConfigParser, iniparse & apiai libraries, which are all
 downloadable from pip. 
  ex: 
   C:\>python.exe -m pip install apiai
   C:\>python.exe -m pip install iniparse
   C:\>python.exe -m pip install ConfigParser

 Then change command to -
 Command: -hi1CMD /m /c "echo {that} > **PATH_TO_INSTALL_FOLDER**\dictation.txt | python.exe **PATH_TO_INSTALL_FOLDER**\linksapiai.py"


Please e-mail any bugs, questions or suggestions to duroktar@gmail.com. 
