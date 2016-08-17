# Starter code taken from:
#   http://stackoverflow.com/questions/23828264/how-to-make-a-simple-multithreaded-socket-server-in-python-that-remembers-client
#
# Countdown code:
#  http://stackoverflow.com/questions/25189554/countdown-clock-0105
#
# Advice on background threads:
# http://sebastiandahlgren.se/2014/06/27/running-a-method-as-a-background-thread-in-python/
#
# More examples: https://shakeelosmani.wordpress.com/2015/04/13/python-3-socket-programming-example/
#
#
# Min examples: http://stackoverflow.com/questions/12141150/from-list-of-integers-get-number-closest-to-a-given-value
#
#
#
# Stopping: http://stackoverflow.com/questions/323972/is-there-any-way-to-kill-a-thread-in-python
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
        self.clientList = []


    def listen(self):
        self.sock.listen(20)
        while True:
            client, address = self.sock.accept()
            self.clientList.append(address)

            if len(self.clientList) >= 2:
                counterThread=threading.Thread(target = self.countdown)
                counterThread.isDaemon = True
                counterThread.start()
            #client.settimeout(60)

            #threading.Thread(target = self.countdown())
            listenThread = threading.Thread(target = self.listenToClient,args = (client,address))
            listenThread.isDaemon = True
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

                    if self.game_time == 0:


                else:
                    raise 'Client disconnected'
            except:
                client.close()
                return False

    def countdown(self):
        print("At least two players have connected! Starting Game Time!: ")
        t = self.game_time
        while t > 0:
            time.sleep(0)

            mins, secs = divmod(t, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(timeformat)
            time.sleep(1)
            t -= 1
        print('End of round!\n')
        try:
            closest = (min(self.guessedNumbers.values(), key=lambda x: abs(int(x) - self.number)))
            for key in self.guessedNumbers:
                if self.guessedNumbers[key]==closest:
                    print(key, " wins!")
            self.game_time = 0
        except: #incase no one enters a number
            print("No one wins...")
            self.game_time = 0





if __name__ == "__main__":
    # TODO: Implement a way to stop the server from command prompt
    # TODO: Countdown for 2 players to join, otherwise shutdown (?)
    # TODO: Countdown until no longer taking guesses
    # TODO: Compare guesses to random number, return victory/defeat messages
    # TODO: restart the game

    #port_num = int(input("Port? "))
    port_num = 2468
    #game_time = int(input("How long would you like to wait for players?"))
    game_time = 5
    reset = game_time

    #while game_time != 0:

    ThreadedServer('',port_num,game_time).listen()




