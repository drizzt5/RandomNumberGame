# Code taken from:
#   http://stackoverflow.com/questions/23828264/how-to-make-a-simple-multithreaded-socket-server-in-python-that-remembers-client
#
#
#
#
#

import random
import socket
import threading

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.number = random.randrange(0, 101, 2)

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()


    def listenToClient(self, client, address):
        size = 1024
        number = self.number
        while True:
            try:
                data = client.recv(size)
                if data:
                    # Set the response to echo back the recieved data
                    response = (str(number)).encode()
                    #print("{} wrote:".format(self.client_address[0]))
                    client.send(response)
                else:
                    raise 'Client disconnected'
            except:
                client.close()
                return False




if __name__ == "__main__":
    # TODO: Implement a way to stop the server from command prompt

    #port_num = int(input("Port? "))
    port_num = 2468


    ThreadedServer('',port_num).listen()



