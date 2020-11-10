## Jumble - Client-Side ##

from jumble import jumbleClient
from socket import socket, SOCK_STREAM, AF_INET

# Set defaults for TCP connection setup
serverHost = 'localhost'
serverPort = 50008
connType = SOCK_STREAM
addrFamily = AF_INET

# Make TCP socket object and connect to server
sockobj = socket(addrFamily, connType)
sockobj.connect((serverHost, serverPort))

# Begin game
jumbleClient(sockobj)

# Close socket
sockobj.close()
