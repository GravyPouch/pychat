import socket,sys,time,_thread

exitflag = 0

s = socket.socket()
host = ''
print(" server will start on host : ", host)
port = 8080
s.bind((host,port))

def recive(threadName, delay):
    incoming_message = conn.recv(1024)
    incoming_message = incoming_message.decode()
    print(" Client : ", incoming_message)
    print("")

def connections(threadName, delay):
    print("Waiting for connections...")
    s.listen(1)
    conn, addr = s.accept()
    print(addr, " has joined")
    message = str("Welcome")
    message = message.encode('ascii')
    conn.send(message)
    try:
         _thread.start_new_thread( connections, ("Thread-1", 2, ) )
         _thread.start_new_thread( recive, ("Thread-2", 4, ) )
    except:
        print ("Error: unable to start thread")




try:
   _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass
