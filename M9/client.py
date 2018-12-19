import socket
s = socket.socket()
s.connect(('127.0.0.1',3128))
Hello="Hello"
s.send((Hello +"\r\n").encode())
greetings=s.recv(10000).decode()
print(greetings)
game="Guess Game Please"
s.send((game +"\r\n").encode())
game=s.recv(10000).decode()
print (game)
running=1
while running:
    guess = input("Enter your guess: ")
    s.send(guess.encode())
    response = s.recv(10000).decode()
    print(response)
    if response.startswith("Correct"):
        running = 0
s.close()