import requests

a =
b = 
r = requests.get("www.ask.com", timeout=5)

print(r)
print(r.text)