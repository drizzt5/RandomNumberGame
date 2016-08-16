# Code taken from:
# http://stackoverflow.com/questions/23828264/how-to-make-a-simple-multithreaded-socket-server-in-python-that-remembers-client
#
#
#
#
#

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

### ask for info
#host = input("Server hostname or ip? ")
#port = int(input("Server port? "))

### Test data
host = "localhost"
port = 2468

sock.connect((host,port))

while True:

    # if data == "exit":
    #     break
    while True:
        try:
            data = int(input("Enter a number between 1-100: "))
            if data < 1:
                raise ValueError
            if data > 100:
                raise ValueError
            break
        except ValueError:
            print("You need to enter a number between 1-100, try again!")

    # ints cant be encoded?
    data = str(data)
    data = data.encode()
    sock.send(data)
    print("response: ", sock.recv(1024))