from threading import Thread
import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.1.1',1234))
sock.send(input("username:").encode())
sock.send(input("password:").encode())
status = sock.recv(1235).decode()
if( status== "failed"):
    print("authentication Failed")
    exit()
print(status)
  
 
def send():
    while True:
        
        sock.close()
    
def receive():
    while True:
          
        sock.close()
  
t1 = Thread(target =  send)
t2 = Thread(target = receive)
t1.start()
t2.start()
t1.join()
t2.join()

