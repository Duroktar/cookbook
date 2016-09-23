Links API.AI Interface
======================
Api.ai Interface for the MVC: Links Mark II Ai

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

*Or if you have Python installed*
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
