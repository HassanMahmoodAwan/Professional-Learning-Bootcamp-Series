""" Create a Game Which has to guess a word, Number of Tries = 10  """

import random

def get_word():
    passS

def main():
    words = [
    "banana", "yellow", "beacon", "carbon", "church", "flight", "pencil", "animal", 
    "export", "safari", "magnet", "ribbon", "spirit", "custom", "forest", "guitar", 
    "poetry", "bridge", "wealth", "stream", "garlic", "palace", "pocket", "planet", 
    "rubber", "speech", "tunnel", "update", "valley", "window", "vision", "artist", 
    "border", "cactus", "dragon", "hunter", "island", "marble", "nature", "pirate", 
    "ranger", "sponge", "ticket", "voyage", "zebra",  "glance", "clover", "danger"
    ]
    
    word = random.choice(words)
    guessWord = "_" * len(word)
    
    counter  = 0
    while counter < 10:
        print(guessWord, end="\n")
        
        guess = input("Enter your guess: ")
        
        if guess in word:
            index = word.index(guess)
            if guessWord[index] == "_" and index != -1:
                guessWord = list(guessWord)
                guessWord[index] = guess
                guessWord = "".join(guessWord)
            elif guessWord[index] != "_":
               index = word[index+1:].index(guess)
               if index != -1 and guessWord[index] == "_":
                   guessWord[index] = guess
               else:
                    print("You have already guessed this letter")
        
            
        if guessWord == word:
            print("Congratulations, You have guessed the word", "and in ", counter, "tries")          
            break        
        
        
        if guess in "0123456789[]',./<>?:{}|_+" or len(guess) > 1:
            print("Invalid input, Please enter a single character")
            counter +=1
            print("Number of Tries Left: ", counter)
            continue
        
        counter += 1
        print("Number of Tries Left: ", 10 - counter)
    else:
        print("You have reached the limit of 10 tries")

if __name__ == "__main__":
    main()