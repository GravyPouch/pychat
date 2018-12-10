import socket,sys,time
x = 5
s = socket.socket()
host = input(str("Please enter the hostname of the server : "))
port = 8080
s.connect((host,port))
print("Connected to chat server")
while x > 1:
    incoming_message = s.recv(1024)
    incoming_message = incoming_message.decode()
    print(" Server : ", incoming_message)
    print("")
    message = input(": ")
    message = message.encode()
    s.send(message)
    print("message has been sent...")
    print("")
