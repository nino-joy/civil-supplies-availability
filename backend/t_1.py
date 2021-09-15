import socket
import sys

users =[{"kurian":"abcd"},{"nino":"1234"},{"naveen":"qwerty"}]
clientlist=[]

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print ("Socket successfully created")
s.bind(('127.0.1.1', 1234))         
s.listen(4)
print ("listening")

while True:
    conn,addr = s.accept()
    print(str(addr) + "connection requested\n")
    username = str(conn.recv(1235).decode())
    password = str(conn.recv(1235).decode())
    if {username:password} in users :
        clientlist.append(conn)
        print("Authenticated  ",addr)
        conn.send(str("Authentication Successfull").encode())
        
        
    else:
        conn.send(str("failed").encode())           	    
s.close()
    	


