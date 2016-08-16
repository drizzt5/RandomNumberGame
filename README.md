# RandomNumberGame
Random Number game for networking

You’re to develop a networked computer game called “Guess that Number!” You’re expected to use Python; but other languages are permitted with the consent of the instructor.

You’re to develop both the server and client programs. The game host starts the game by starting the game server on a specific port (you may choose to fix that port number or make it customizable on the command line). However, the server’s IP address must be a command line option or input via a GUI for the client program. Once started the server picks an integer randomly from 1 to 100 and waits for a fixed amount of time in seconds (variable name: game_time) for the players to join the game. The game_time variable must be customizable from the command line for launching the server.  The server should not start counting down the time until at least two players have joined the game.

A player joins the game by starting the client program. Once joined, the client prompts the player to input an integer from 1 to 100.  

At the end of the game_time period, the server compares all the guesses from the players who have joined and discloses the outcome to all players using messages such as “The number is <> and
your guess is <>. You win with the closest guess / Better luck next time”. The server should start another game immediately after that.

Three-step approach:

While advanced programmers may choose to finish the project in one design effort, a divide-and- conquer approach is suggested as follows:

Step 1: develop a system for one player only – the server simply echoes the player’s guess.

Step 2: Enhance the server code from step 1 to support multiple players using a separate thread for each player.

Step 3: Enhance the server code further to support game logic and starting of new game.

We will conduct labs following this approach. We will use Python examples exclusively in the labs.

Grading:


•	You need to provide via email the source code and instructions for testing your game, and you may be required to demonstrate your game in class.

•	You may borrow code from the Internet, but not from you classmates. You must cite the source for any borrowed code.
 
•	40%  --- messages exchanged between server and clients using UDP or TCP
20%  --- separate server thread used for each client
25%  --- server keeps track of clients and implements game logic
5%  --- command line argument/GUI used for IP address and the game_time variable
5%  --- server starts new game automatically (clearing all players from the game)
5%  --- program style and efficiency

