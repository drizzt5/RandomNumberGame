# Starter code taken from:
#   http://stackoverflow.com/questions/23828264/how-to-make-a-simple-multithreaded-socket-server-in-python-that-remembers-client
#
# Countdown code:
#  http://stackoverflow.com/questions/25189554/countdown-clock-0105
#
# Advice on background threads:
# http://sebastiandahlgren.se/2014/06/27/running-a-method-as-a-background-thread-in-python/
#
#
#

import random
import time
import socket
import threading

class ThreadedServer(object):
    def __init__(self, host, port, game_time):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.number = random.randrange(0, 101, 2)
        self.game_time = game_time # Time for the players to actually join the game
        self.guessedNumbers = {}





    def listen(self):
        self.sock.listen(20)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)

            #threading.Thread(target = self.countdown())

            listenThread = threading.Thread(target = self.listenToClient,args = (client,address))
            listenThread.daemon = True
            listenThread.start()


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


                    #Store each clients guessedNumbers
                    #self.guessedNumbers.append(data)

                    client.send(response)

                    # The good thing is that this only saves the latest guess
                    self.guessedNumbers[threading.get_ident()] = data
                   # self.guessedNumbers["hi"] = data

                    print(self.guessedNumbers)


                    #print("Current number of clients: ", (threading.active_count()-1))
                    #print(threading.enumerate())
                else:
                    raise 'Client disconnected'
            except:
                client.close()
                return False

    def countdown(self):
        t = self.game_time
        while t:
            mins, secs = divmod(t, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(timeformat)
            time.sleep(1)
            t -= 1
        print('Goodbye!\n')



if __name__ == "__main__":
    # TODO: Implement a way to stop the server from command prompt
    # TODO: Countdown for 2 players to join, otherwise shutdown (?)
    # TODO: Countdown until no longer taking guesses
    # TODO: Compare guesses to random number, return victory/defeat messages
    # TODO: restart the game

    #port_num = int(input("Port? "))
    port_num = 2468
    #game_time = int(input("How long would you like to wait for players?"))
    game_time = 10

    ThreadedServer('',port_num,game_time).listen()




