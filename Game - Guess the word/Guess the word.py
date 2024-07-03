import random

with open('words.txt', 'r') as f:
    words = f.read().splitlines()
# Random word selection
def word_choice ():
    word = random.choice(words)
    return word
word_choice()

random_arr = []
guess_arr = []
hidden_word = []


# The number of players
players_number = int(input("Enter the number of players  "))

# Adding the players' names to the list
players_name = []
for i in range(players_number):
    player = input("Enter your name ")
    players_name.append(player)


# Creating a dictionary with player names and score
players = {}
for name in players_name:
    players[name]=0

# Ask the player how many words he would like to guess
words_number = int(input("How many words would you like to guess? "))
for a in range(words_number):
    random_word = word_choice()

# Checking that the drawn word is a new word
    while random_word in random_arr:
        random_word = word_choice()
    random_arr.append(random_word)

    # Hiding the word
    for q in random_word:
        hidden_word.append(" _ ")

    # Checking that the word has not yet been discovered
    while " _ " in hidden_word:

        # A loop that goes through the entire list of players
        for i in range(len(players_name)):
            print (hidden_word)
          
            play =input(f"{players_name[i]}  Guess only one letter  score =  {players[players_name[i]]} ")
            # A check that the player guesses only one letter without having already guessed it
            while play in guess_arr or len(play)>1:
                play =input(f"{players_name[i]}  Guess only one letter: score =  {players[players_name[i]]} ")
            guess_arr.append(play)

            # Check that the guess is correct
            for j in range (len(random_word)):
                if play == random_word[j]:
                    hidden_word[j] = play
                    print(hidden_word)
                    players[players_name[i]]+=1
    hidden_word =[]
    guess_arr = []
random_arr = []


        

    
 
