



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


        listenThread = threading.Thread(target=self.listenToClient, args=(client, address))
        listenThread.isDaemon = True
        listenThread.start()



    def run(self):
