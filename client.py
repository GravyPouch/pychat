import socket,sys,time,threading
from threading import Thread
x = 5
s = socket.socket()
host = input(str("Please enter the ip/hostname of the server : "))
port = 8080
try:
    s.connect((host,port))
except:
    print("cannot connect to server try again.")

def recive():
    while 1:
        incoming_message = s.recv(1024)
        incoming_message = incoming_message.decode()
        print(" Server : ", incoming_message)
        print("")

def send():
    while 1:
        message = input(": ")
        message = message.encode('ascii')
        s.send(message)

print("Connected to chat server")
threading.Thread(target=recive())

while 1:
    pass
