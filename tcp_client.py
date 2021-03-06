############################################
# Author: Dillon Glasser
# Program Project for CS3502
# tcp_client code
#
# Starter code:
# http://stackoverflow.com/questions/23828264/how-to-make-a-simple-multithreaded-socket-server-in-python-that-remembers-client
#
###############################################


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
    #I was going to use this number to stop it from asking after the client guesses once.
    data = 666
    while True:
        if data == 666:
            try:
                data = int(input("Enter a number between 1-100: "))
                if data < 1:
                    raise ValueError
                if data > 100:
                    raise ValueError
                break
            except ValueError:
                data = 666
                print("You need to enter a number between 1-100, try again!")

    print(data)
    data = str(data)
    data = data.encode()
    sock.send(data)
    message = sock.recv(1024).decode()

    if message == 'win':
        print("End of Game\nYou Win!")
        return False

    elif message == 'lose':
        print("End of Game\nYou Lose!")
        return False
    else:
        print("\nServer Response:", message, "\n")
        return True



while value == True:
    value = clientRun()

sock.shutdown(2)
sock.close()


#TODO I need to make it so that the winner and loser is returned with the random number, client side.

#TODO I also need to find a way to boot off clients who haven't guessed when the time is up.
