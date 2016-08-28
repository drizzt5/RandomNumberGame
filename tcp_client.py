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
value = True
sock.connect((host,port))



def clientRun():
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
    message = sock.recv(1024).decode()

    disCon = "Disconnecting now"
    disCon = disCon.encode()

    if message == 'win':
        print("End of Game \n You Win!")
        sock.send(disCon)
        return False

    elif message == 'lose':
        print("End of Game \n You Lose!")
        sock.send(disCon)
        return False
    else:
        print("response: ", message)
        return True



while value == True:
    value = clientRun()

sock.shutdown(2)
sock.close()
