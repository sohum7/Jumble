## Jumble - Server-Side ##

from jumble import jumbleServer
from socket import socket, SOCK_STREAM, AF_INET
import time, _thread as thread

# Set defaults for TCP connection setup
myHost = ''                                      # '' means local host
myPort = 50008
connType = SOCK_STREAM
addrFamily = AF_INET

# Bind server to port and start listening for client
sockobj = socket(addrFamily, connType)              # TCP socket object
sockobj.bind((myHost, myPort))
sockobj.listen(5)

# Current time on the server
def now():
    return time.ctime(time.time())

# Begin game with client
# Each client is handled by its own thread
# Keep playing the game until client would like to no longer play
# Close game once done
def handleClient(connection):
    time.sleep(2)
    
    jumbleServer(connection)
        
    connection.close()

# Server listens at port until process is killed
# A thread is created to communicate with the client process and handleClient function is used
def dispatcher():
    while True:
        connection, address = sockobj.accept()
        print('Server connected by', address, end=' ')
        print('at', now())
        thread.start_new_thread(handleClient, (connection,))

# Run dispatcher function
dispatcher()
