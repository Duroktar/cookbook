Get movie information from the web and have Jarvis read you a summary.

1. Unpack contents into folder on your computer and keep note of the path for instruction #3.
2. Open config.ini file in notepad and set port and key for LINKS Web Service.
3. Enter this command in LINKS under SHELL -
  Command: look up movie {that=test_dictation}
  Response: 
  Action: -hi1CMD /m /c "echo {that} > **PATH_TO_INSTALL_FOLDER**\dictation.txt | python.exe **PATH_TO_INSTALL_FOLDER**\movieSearch.py"
  Profile: main
4. Have fun :)

Link to download -
https://drive.google.com/open?id=0BxC7Vg_reMwnR0w5X0luZFhUeGc

Feel free to e-mail me with any questions or if you need help setting it up @ duroktar@gmail.com


By: traBpUkciP
