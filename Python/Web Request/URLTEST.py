import urllib2
response = urllib2.urlopen('http://pythonforbeginners.com/')
print response.info()
html = response.read() # do something
response.close()  # best practice to close the file