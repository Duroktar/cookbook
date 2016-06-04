'''
 Simple alert box. Same effect as alert() in JavaScript.

'''
import ctypes  # An included library with Python install.

##  You could use an import and single line code like this:
##  ctypes.windll.user32.MessageBoxA(0, "Your text", "Your title", 1)

##  Or define a function (Mbox) like so:
def Mbox(title, text, style):
    ctypes.windll.user32.MessageBoxA(0, text, title, style)
Mbox('Your title', 'Your text', 1)


##  Note the styles are as follows:

##  Styles:
##  0 : OK
##  1 : OK | Cancel
##  2 : Abort | Retry | Ignore
##  3 : Yes | No | Cancel
##  4 : Yes | No
##  5 : Retry | No 
##  6 : Cancel | Try Again | Continue