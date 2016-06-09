# CHECKIO
# Guido van Rossum, the author of Python, is one of our most famous player. 
# He is writing some really wonderful code reviews for our player solutions.


#  Exception Handling like a pro
'''
def func(str_number, radix)
	try:
        n = int(str_number, radix)
        return n
    except ValueError:
        return -1
		

		'''



# AWESOME Idea for how to handle 'len() - 1' situations 
# so as not to get 'index outside the list or array' errors.

'''
numbers = [32, 4]
s = 0

i = len(numbers) # return value is 1 higher than the last index number of the list 

while i != 0:
    i -= 1  #	deal with it first!
    s += numbers[i]   # Instead of here with s += numbers[i - 1]

print "The sum is: ", s
'''


# For accepting user input
'''
variable = raw_input('User prompt:')
print variable

'''


# Python KEYWORDS List
''' 

and       del       from      not       while
as        elif      global    or        with
assert    else      if        pass      yield
break     except    import    print
class     exec      in        raise
continue  finally   is        return 
def       for       lambda    try

'''

# Iteresting note about void functions
''' 

Functions that perform an action but DON'T RETURN A VALUE, 
are considered void functions DO NOT have a return value. 
If you try to assign the result of a VOID FUNCTION to a variable
it RETURNS 'None' which is a special TYPE of value. (Like a string
or a float)

'''

# Continue usage
'''
num = 0

while (num < 1000):
	num = num + 1
    if (num % 2) == 0:
      continue
    print num
'''

# The different Objects

import sys


def function(): pass


print type(1)         # int
print type("")        # str
print type([])        # list
print type({})        # dict
print type(())        # tuple
print type(object)    # type
print type(function)  # function
print type(sys)       # module
