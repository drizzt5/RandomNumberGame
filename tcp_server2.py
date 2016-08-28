



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
        self.game_time = game_time
        self.guessedNumbers = {}
        self.clientList = []
        self.condition = True


    def run(self):
        self.sock.listen(20)
        t = threading.Timer(self.game_time, self.endFunction)

        while self.condition == True:
            client, address = self.sock.accept()
            self.clientList.append(address)
            if len(self.clientList) >= 2:
                t.start()

            listenThread = threading.Thread(target=self.listenToClient, args=(client, address))
            listenThread.isDaemon = True
            listenThread.start()


    def listenToClient(self, client, address):
        size = 1024
        number = self.number
        while self.condition == True:
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


                else:
                    raise Exception('Client disconnected')
            except:
                client.close()
                return False



    def endFunction(self):
        print("End of Game")
        self.condition = False
        result = str(self.sock.shutdown(2))
        print(result)
        self.sock.close()
        print("Restarting game in 5 seconds...")
        time.sleep(5)
        ThreadedServer('', port_num, game_time).run()



if __name__ == "__main__":
    #port_num = int(input("Port? "))
    port_num = 2468
    #game_time = int(input("How long would you like to wait for players?"))
    game_time = 1
    reset = game_time

    #while game_time != 0:
    ThreadedServer('',port_num,game_time).run()