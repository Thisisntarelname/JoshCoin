import hashlib
import random
import requests
import time


def redeemHash(number):
  url = 'https://JoshCoinServer.codeeatspennies.repl.co/redeem' 
  data = {'name': 'Alice', 'number':(number)} 
  requests.post(url,data = data)
  print("sent")
  time.sleep(10)
  getTargetHash()
  
  
def crackHash(hash):
  print("New hash detected; trying to crack")
  i=0
  numList=[]
  while i<1000000000:
    tempNum = random.randrange(3, 99999)
    numList.append(tempNum)
    m = bytes(tempNum)
  
    test = (hashlib.sha512(m).hexdigest())
    if test == hash:
      print("Found:  ", i)
      redeemHash(i)
      print(numList)
      break
    else:
      pass
      
    
    i = i+1
  

def getTargetHash():
  #GET request to a json file contsaining the target hash hoste don the serrver
  URL = 'https://JoshCoinServer.codeeatspennies.repl.co/static/targetHash.txt'
  r = requests.get(url = URL)
  print(URL)
  print(r)
  data = r.content
  data = str(data)
  data = data.replace("b'", "")
  data = data.replace("'", "")
  print(data)

  if data == hash:
    pass
  else:
    crackHash(data)




def buy():  
  url = 'https://JoshCoinServer.codeeatspennies.repl.co/buy' # sets the url variable to the url you're gonna be sending the post request to
  data = {'name': 'alice', 'value':8, 'action':'buy-soda'} # the data you want to send
  requests.post(url,data = data) # actually does the post request (you can replace data = data with json = data if your server accepts json encoded data)
  print("sent")

getTargetHash()