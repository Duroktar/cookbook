-LINKS Cleverbot module *Requires Python 2.7- 
by:traBpUkciP

Install-
1. unpack zip file

2. open config file and make sure your settings match.

3. Requires Cleverbot v1.0.2 and ConfigParser python libraries 
"python.exe -m pip install cleverbot --upgrade"
"python.exe -m pip install configparser --upgrade"

4. Enter these custom commands into links.

This will start the Chat session-
  Command: start clever bot chat
  Response:
  Action:  -hi1**PATH_TO_INSTALL_FOLDER**\linkscleverbot.py


This is to chat once it's running-
  Command: cleverbot {that=test_dictation}
  Response:
  Action: -hi1CMD /m /c "echo {that} > **PATH_TO_INSTALL_FOLDER**\dictation.txt"

4. Say "End chat" to close cleverbot chat session. The chat session will automatically time out 5 minutes after the last detected chat request.

5. Have fun :)

NOTE: I can turn this into an .exe if I get enough requests. Then you don't need python to run it at all. Send an e-mail with your thoughts. (bottom of page)

**PowerUsers**- You can enter dictation manually into the dictation.txt file that resides in the folder with linkscleverbot.py. It will be picked up on save by the cleverbot.

IMPORTANT: Do not rename file to cleverbot.py or it will not work. (it's the name of the lib it uses, so ya can't do it)

Thanks to ApatheticEuphoria for the idea to make this happen.

e-mail questions to duroktar@gmail.com

