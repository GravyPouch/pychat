import socket,sys,time,threading

s = socket.socket()
host = socket.gethostname()
print(" server will start on host : ", host)
port = 8080
s.bind((host,port))

def recive():
    incoming_message = conn.recv(1024)
    incoming_message = incoming_message.decode()
    print(" Client : ", incoming_message)
    print("")

def connections():
    print("Waiting for connections...")
    s.listen(1)
    conn, addr = s.accept()
    print(addr, " has joined")
    message = str("Welcome")
    message = message.encode('ascii')
    conn.send(message)
    try:
        _thread.start_new_thread( connections, ("Thread-connect", 2, ) )
        _thread.start_new_thread( recive, ("Thread-recive", 4, ) )
    except:
        print ("Error: unable to start thread")



connections()
