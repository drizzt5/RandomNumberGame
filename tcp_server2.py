# https://www.webcodegeeks.com/python/python-sockets-example/



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
        self.condition = True
        self.winners = []
        self.losers = []






    def run(self):
        print("New Round Starting!")
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

            listen = threading.Thread(target=self.listen)
            listen.isDaemon = True
            listen.start()



    def listen(self):
        client, address = self.sock.accept()
        self.clientList.append(address)
        listenThread = threading.Thread(target=self.listenToClient, args=(client, address))
        listenThread.isDaemon = True
        listenThread.start()


    def listenToClient(self, client, address):
        size = 1024
        number = self.number
        while self.condition == True:
            try:
                data = client.recv(size)
                data = data.decode()
                try:
                    data = int(data)
                except:
                    print(data)

                if isinstance(data, int):

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


                else:
                    raise Exception('Client disconnected')
            except:
                client.close()
                return False

        #After while loop closes
        win = "win"
        win = win.encode()
        lose = "lose"
        lose = lose.encode()

        client.send(win)
        client.close()

    def determineWinners(self):
        try:
            closest = (min(self.guessedNumbers.values(), key=lambda x: abs(int(x) - self.number)))
            for key in self.guessedNumbers:
                if self.guessedNumbers[key]==closest:
                    print(key, " wins!")
                    self.winners.append(key)
                else:
                    self.losers.append(key)

            #self.game_time = 0
        except: #incase no one enters a number
            print("No one wins...")



    def endFunction(self):
        print("End of Game")

        self.determineWinners()





        self.condition = False
        # result = str(self.sock.shutdown(2))
        # print(result)
        # self.sock.close()
        time.sleep(5)
        print("Restarting game in 5 seconds...")

        self.number = random.randrange(0, 101, 2)
        self.condition = True
        self.clientList = []

        t = 5
        while t > 0:
            mins, secs = divmod(t, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(timeformat)
            time.sleep(1)
            t -= 1
        self.run()

        #ThreadedServer('', port_num, game_time).run()



if __name__ == "__main__":
    #port_num = int(input("Port? "))
    port_num = 2468
    #game_time = int(input("How long would you like to wait for players?"))
    game_time = 10
    reset = game_time

    ThreadedServer('', port_num, game_time).run()

