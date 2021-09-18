import socket
import sys

clientlist={"kurian":"Kurian,availabe is rice:1kg,wheat:10kg","nino":"Nino,availabe is rice:2kg,wheat:15kg","naveen":"Naveen,availabe is rice:3kg,wheat:12kg"}

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

    print(username,"+",password)
    print(clientlist[str(username)])
    conn.send(str(clientlist[str(username)]).encode())
s.close()
    	


