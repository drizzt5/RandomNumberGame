#######################################################################
# Author: Dillon Glasser
# Program Project for CS3502
#
# Some websites I used for guidance:
#
# More examples:
# https://shakeelosmani.wordpress.com/2015/04/13/python-3-socket-programming-example/
# Min examples:
# http://stackoverflow.com/questions/12141150/from-list-of-integers-get-number-closest-to-a-given-value
# Stopping:
# http://stackoverflow.com/questions/323972/is-there-any-way-to-kill-a-thread-in-python
# Sockets:
# https://www.webcodegeeks.com/python/python-sockets-example/
# Threading:
# http://sebastiandahlgren.se/2014/06/27/running-a-method-as-a-background-thread-in-python/
# Starter code taken from:
# http://stackoverflow.com/questions/23828264/how-to-make-a-simple-multithreaded-socket-server-in-python-that-remembers-client
# Countdown code:
# http://stackoverflow.com/questions/25189554/countdown-clock-0105
########################################################################





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
        self.sock.listen(20)
        self.number = random.randrange(0, 101, 2)
        self.game_time = game_time
        self.guessedNumbers = {}
        self.clientList = []
        self.winners = []
        self.losers = []






    def run(self):
        print("Game will start when ready:")
        while True:
            t = threading.Timer(self.game_time, self.endFunction)

            if len(self.clientList) >= 2:
                print("Starting Game\nCountdown until end of round begins now:")
                t.start()
                t = self.game_time
                while t > 0:
                    mins, secs = divmod(t, 60)
                    timeformat = '{:02d}:{:02d}'.format(mins, secs)
                    print(timeformat)
                    time.sleep(1)
                    t -= 1
                break
            if len(self.clientList) == 0:
                print("Waiting for 2 players...")
                time.sleep(3)
            self.listen()


    def listen(self):
        client, address = self.sock.accept()
        self.clientList.append(address)
        listenThread = threading.Thread(target=self.listenToClient, args=(client, address))
        listenThread.isDaemon = True
        listenThread.start()
        return True


    def listenToClient(self, client, address):
        size = 1024
        number = self.number
        win = "win"
        win = win.encode()
        lose = "lose"
        lose = lose.encode()


        while True:
            try:
                data = client.recv(size)
                data = data.decode()
                try:
                    data = int(data)
                except:
                    print(data)

                if isinstance(data, int):

                    # Set the response
                    #response = (str(number)).encode()
                    response = "\nGuess has been recorded!\nYou can change your guess until the time expires \nor enter the same # to see if you won."
                    response = response.encode()


                    # saves the latest guess
                    self.guessedNumbers[threading.get_ident()] = data


                    #print(self.guessedNumbers)

                    if threading.get_ident() in self.winners:
                        # response = (str(number)).encode()
                        # client.send(response)
                        client.send(win)
                        client.close()
                    elif threading.get_ident() in self.losers:
                        client.send(lose)
                        client.close()
                    else:
                        client.send(response)


                else:
                    raise Exception('Client disconnected')
            except:
                client.close()
                return False

    def determineWinners(self):
        try:
            closest = (min(self.guessedNumbers.values(), key=lambda x: abs(int(x) - self.number)))
            for key in self.guessedNumbers:
                if self.guessedNumbers[key]==closest:
                    print(key, "wins!")
                    self.winners.append(key)
                else:
                    self.losers.append(key)
            #return 0

        # incase no one enters a number
        except:
            print("No one wins...")
            for key in self.guessedNumbers:
                self.losers.append(key)
            #return 1


    def endFunction(self):
        print("End of Game")
        print("The random number was", str(self.number))

        self.determineWinners()

        print("Restarting game in 10 seconds...")
        time.sleep(7)
        t = 3
        while t > 0:
            mins, secs = divmod(t, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(timeformat)
            time.sleep(1)
            t -= 1

        self.number = random.randrange(0, 101, 2)
        self.clientList = []
        self.winners = []
        self.losers = []
        self.guessedNumbers = {}
        self.run()



if __name__ == "__main__":
    #port_num = int(input("Port? "))
    port_num = 2468
    #game_time = int(input("How long would you like to wait for players?"))
    game_time = 10
    reset = game_time

    ThreadedServer('', port_num, game_time).run()

