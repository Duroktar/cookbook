#     - Example -
# c:\>python F:\JARVIS\xmlscraper.py TestVariable
# By: traBpUkciP


from xml.etree import ElementTree as ET
import sys

'''
FUNCTION
   -   varfetch(string)   -

Takes varName as a command line argument
'''

fetch = "\n".join(sys.argv[1:]) # Fetches first argument from command line, ignores rest

tree = ET.parse('C:\Users\Charlotte\AppData\Roaming\LINKS\Customization\XML\UserVariables.xml')  #ElementTree.parse('path')
root = tree.getroot()    # Gets root index from tree

def varfetch(varName):   #Declare function
    for each in root.findall('Variable'):    # Find all data indexed under 'Variable'
        value = each.find('Value').text      # Find 'Value' of each (optional)
        name = each.find('Name').text        # Find 'Name' of each (optional)
        if name == varName:                  # Check if matches command argument 'varName'
            print(value)                     # Prints results to screen



varfetch(fetch)