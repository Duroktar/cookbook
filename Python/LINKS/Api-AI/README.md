Links API.AI Interface
======================
Api.ai Interface for the MVC: Links Mark II AI on Windows.

Install
-------
 - Unzip files into links scripts folder.
 - Enter your API.Ai Client Key in the config.ini file.
 - Enter shell command into Links
 
Links Shell Command
-------------------
**Enter this command in Links *Shell* tab**
 - **Command:** api bot {that=test_dictation}
 - **Response:** {{!Action!}}
 - **Action:** -ret"%AppData%\LINKS\Customization\Scripts\linksapi.exe" "{that}"
 - **Profile:** main


**Or if you have Python 2.7 installed**
 - **Command:** api bot {that=test_dictation}
 - **Response:** {{!Action!}}
 - **Action:** -ret"python" "%AppData%\LINKS\Customization\Scripts\linksapi.py" "{that}"
 - **Profile:** main

Usage
-----
 - **User:** api bot hello whats up
 - **ApiBot:** Hello! How are you today?
 - **User:** api bot whats the weather today in florida
 - **ApiBot:** The weather in .... blah blah

Credits
-------
Created by: traBpUkciP

<a href='https://ko-fi.com/A5034CT' target='_blank'><img height='32' style='border:0px;height:32px;' src='https://az743702.vo.msecnd.net/cdn/kofi2.png?v=a' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a> 

Let me know if you have any requests/questions/complaints and I'll try to get to you all as soon as I can. Have fun :) 
