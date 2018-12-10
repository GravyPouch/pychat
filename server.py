import socket,sys,time,_thread,threading
from threading import Thread

exitflag = 0
x = 1
s = socket.socket()
host = ''
print(" server will start on host : ", host)
port = 8080
s.bind((host,port))

def timelapse(x):
    while 1:
        time.sleep(1)
        x = x + 1
        print(x)

def recive(x,conn,addr):
    incoming_message = conn.recv(1024)
    incoming_message = incoming_message.decode()
    print(" Client : ", incoming_message)
    print("")

def connections(x):
    print("Waiting for connections...")
    s.listen(1)
    conn, addr = s.accept()
    print(addr, " has joined")
    message = str("Welcome")
    message = message.encode('ascii')
    conn.send(message)


connectionmaker = threading.Thread(target=connections(x))
print("hwllo")
connectionmaker.start()

while 1:
   pass

  #https://www.tutorialkart.com/python/python-multithreading/#example
