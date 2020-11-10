## Jumble - Main Game ##

# Randomizer
import random

# Open file of words
# Each word is followed by blank spaces
f = open('wordlist.txt')
words = f.readlines()
f.close()

# Default
LINE_LENGTH = 1024

# Jumble Server #
# Begin and keep running the game
## Pick a random word from the file ## Remove the white space from the word and turn it into a list
## Remove letter from word's list at random and append them to a new empty list
## Send the list of jumbled words back to the client to guess and wait for response
## Test if clients response matches the orignal word ## Send back an appropriate message indicating if client won or not
def jumbleServer(connection):
    
    while True:
        word = words[random.randrange(len(words))]
        while len(word) > 5 or len(word) == 0: word = words[random.randrange(0, len(words))]
        
        word = word.rstrip()
        old_word = word
        word = list(word)
        jumbled_word = []
        
        while word: jumbled_word.append(word.pop(random.randrange(len(word))))
            
        jumbled_word = " ".join(jumbled_word)
        connection.send(f"{jumbled_word}\nType your answer: \n".encode())
        
        match_word = connection.recv(LINE_LENGTH).decode()
        if not match_word: break
        
        new_word = match_word + '\n'
        connection.send("You win.".encode()) if new_word in words and set(match_word) == set(old_word) else connection.send(f"The answer is {old_word}".encode())
      
        
# Jumble Client #
# Begin and keep running the game until client no longer wants to play
## Recieve jumbled word
## Guess the word and send back response
## Server will send back a response indicating if client guessed correctly or not
def jumbleClient(socketObject):
    
    while True:
        print(f"\nJumbled Word: {socketObject.recv(LINE_LENGTH).decode()}")

        match_word = input()
        if not match_word: break
        socketObject.send(match_word.encode())
        
        print(f"{socketObject.recv(LINE_LENGTH).decode()}")