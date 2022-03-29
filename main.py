import hashlib
import random
import requests



num = random.randrange(1, 10)
print ("number to find:  ", num)
n = bytes(num)
hash = (hashlib.sha512(n).hexdigest())

i=0
while i<1000000:
  m = bytes(i)

  test = (hashlib.sha512(m).hexdigest())
  if test == hash:
    print("Found:  ", i)
    break
    
  
  i = i+1
  
url = 'https://JoshCoinServer.codeeatspennies.repl.co' # sets the url variable to the url you're gonna be sending the post request to
data = {'key':'7'} # the data you want to send
requests.post(url,data = data) # actually does the post request (you can replace data = data with json = data if your server accepts json encoded data)
print("sent")