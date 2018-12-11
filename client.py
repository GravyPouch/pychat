import socket,sys,time,threading,sys
from threading import Thread
#setting up some variables for later use
x = 5
#making calling the socket eaiser
s = socket.socket()
#entering server
host = input(str("Please enter the ip/hostname of the server : "))
port = 8080
#tries to connect to provided ip and port
try:
    s.connect((host,port))
except:
    #if it cant it will exit the program
    print("cannot connect to server try again.")
    sys.exit()
#defines how the program interprets recived packets
def recive():
    #loop
    while 1:
        #Defines the packet size and what to call it
        incoming_message = s.recv(1024)
        #decodes the message from byte like object to str
        incoming_message = incoming_message.decode()
        #if the message is something it will print it.
        if incoming_message != '':
            print("Server: ", incoming_message)
        else:
            continue
#a function to start a reciving thread
def startfrecive():
    frecive = threading.Thread(target=recive)
    frecive.start()
#a function to send text to server
def send():
    while 1:
        #gets input
        message = input("// ")
        #encodes it for transport
        message = message.encode('ascii')
        #sends it
        s.send(message)
#a function to start a thread to send things
def startfsend():
    fsend = threading.Thread(target=send)
    fsend.start()

print("Connected to chat server")
#starts threads
startfrecive()
startfsend()
