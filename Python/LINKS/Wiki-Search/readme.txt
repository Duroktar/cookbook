1. Download required Python libraries (ctypes, wikipedia, ConfigParser)
  ex: (From command line) 
   "python.exe -m pip install ctypes"
   Then repeat for other required packages.

2. unpack zip file
3. open config file and fill in your port and key.
4. Enter these custom commands into links.
Command: search wiki for {that=test_dictation}
Response:
Action: -hi1CMD /m /c "echo {that} > **PATH_TO_INSTALL_FOLDER**\dictation.txt | **PATH_TO_INSTALL_FOLDER**\wikisearch.py"
5. Have fun :)

e-mail questions to duroktar@gmail.com