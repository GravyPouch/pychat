import socket,sys,time,threading,random
from threading import Thread
#defines vars
x = 1
#makes socket eaiser to type
s = socket.socket()
#define server ip or hostname
host = ''
print(" server will start on host : ", host)
port = 8080
#binds the program network interface to the ip and port
s.bind((host,port))

#defines a recive function
def recive(conn,addr):
#loop
    while 1:
#tries to recive pakcets and difine them if the client dissconnects the server searchs for a new client
        try:
            incoming_message = conn.recv(1024)
        except ConnectionResetError:
            print("error client lost")
            print("Dont worry we find a new one")
            print("Spinning up a new thread")
            startfconnections()
            #sets a varabile to decode any messsages
        incoming_message = incoming_message.decode()
        #if the message isnt blank
        if incoming_message != '':
            #this prints the messages then sends it back to client with a tad delay
            print(" Client : ", incoming_message)
            time.sleep(0.1)
            #re encodes the message
            incoming_message = incoming_message.encode('ascii')
            #sends it
            conn.send(incoming_message)
        else:
            continue

def startfrecive(conn,addr):
    #starts a reciving thread to recivce messages
    ftimer = threading.Thread(target=recive(conn,addr))
    ftimer.start()

def connections():
    print("Waiting for connections...")
    #listens for clients then connects them
    s.listen(1)
    conn, addr = s.accept()
    #sends a confirmation message to client
    print(addr, " has joined")
    message = str("Welcome")
    message = message.encode('ascii')
    conn.send(message)
    #starts a thread to start reciving messages
    startfrecive(conn,addr)

def startfconnections():
    # a function to start connection threads
    ftimer = threading.Thread(target=connections)
    ftimer.start()
#starts function
startfconnections()
