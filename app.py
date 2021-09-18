from flask import Flask,request,render_template
from threading import Thread
import socket
import sys

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

database={'naveen':'123','kurian':'123','nino':'123'}
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.1.1',1234))
@app.route('/')
def hello_world():
    return render_template("login.html")


@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
        return render_template('login.html',info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('login.html',info='Invalid Password')
        else:
            value = client(name1,pwd)
            sock.close()
            return render_template('home.html',name=str(value))
def client(name1,pwd):
    print(name1)
    print(pwd)
    sock.send(name1.encode())
    sock.send(pwd.encode())
    status = sock.recv(1235).decode()
    print(status)
    return status
if __name__ == '__main__':
    app.debug = True
    app.run()


# def client(name1,pwd):
#     sock.send(name1.encode())
#     sock.send(pwd.encode())
#     status = sock.recv(1235).decode()
#     status =status+"naveen"
#     if( status== "failed"):
#         print("authentication Failed")
#         exit()
#     print(status)
    
    
#     def send():
#         while True:

#             sock.close()

#     def receive():
#         while True:
#             sock.close()
    
#     t1 = Thread(target =  send)
#     t2 = Thread(target = receive)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     return status