# assignment: programming assignment 1
# author: Ugonna Ezeokoli
# date: 1/19/2023
# file: hangman.py is a program that makes user guess each letter of a word until they get the word or run out of attempts
# input: User inputs size of the word and amount of attempts they have to guess. User also inputs each character to guess word and if they want to play again or not.
# output: Outputs if user wins game or not, It also outputs if the user guessed the right letter or not. 

from random import choice, random, randint

dictionary_file = "dictionary.txt"   # make a dictionary.txt in the same folder where hangman.py is located

# write all your functions here

# make a dictionary from a dictionary file ('dictionary.txt', see above)
# dictionary keys are word sizes (1, 2, 3, 4, …, 12), and values are lists of words
# for example, dictionary = { 2 : ['Ms', 'ad'], 3 : ['cat', 'dog', 'sun'] }
# if a word has the size more than 12 letters, put it into the list with the key equal to 12

# This function makes a dictionary where the key is a number that represents size of word and value of key is a list of words that have size of key
def import_dictionary (filename) :
    with open(filename) as file:
      contents = file.readlines()
    words = "".join(contents)
    words = words.split("   ")
    words = "".join(words)
    words = words.split("\n")
    dictionary = {}
    max_size = 12
    try :
        for i in range(2,13):
          list = []
          for word in words:
            if i == len(word):
              list.append(word)
          dictionary[i] = list
            
    except Exception :
        pass
    return dictionary

# print the dictionary (use only for debugging)
def print_dictionary (dictionary) :
    max_size = 12
    print(dictionary) 

# get options size and lives from the user, use try-except statements for wrong input
def get_game_options () :
    try:
      size = int(input("Please choose a size of a word to be guessed [3 – 12, default any size]:\n"))
      print(f"The word size is set to {size}")
    except:
      size = randint(3,12)
      print("A dictionary word of any size will be chosen.")
    try:
      lives = int(input("Please choose a number of lives [1 – 10, default 5]:\n"))
    except:
      lives = 5
    print(f"You have {lives} lives.")
    return (size, lives)


# MAIN

if __name__ == '__main__' :
  # Turns words from file into a clean list of individual words
  

  
    # make a dictionary from a dictionary file
    dictionary = import_dictionary(dictionary_file)
    

    # print the dictionary (use only for debugging)
    # print_dictionary(dictionary)    # remove after debugging the dictionary function import_dictionary

    # print a game introduction
    print("Welcome to the Hangman Game!")
    # START MAIN LOOP (OUTER PROGRAM LOOP) 
    while True:
      chosen_letters = []
      lost = 0
    # set up game options (the word size and number of lives)
      size,lives = get_game_options()
      hidden_letters = []
      for i in range(size):
        hidden_letters.append("__")
    # select a word from a dictionary (according to the game options)
      
      
    # use choice() function that selects an item from a list randomly, for example:
    # mylist = ['apple', 'banana', 'orange', 'strawberry']
    # word = choice(mylist)
      special_word = choice(dictionary[size]).upper()
      copy_special_word = special_word[::]
      if '-' in special_word:
          hidden_letters[special_word.find('-')] = '-'
        # START GAME LOOP   (INNER PROGRAM LOOP)
      while True:
        # format and print the game interface:
        # Letters chosen: E, S, P                list of chosen letters
        # __ P P __ E    lives: 4   XOOOO        hidden word and lives
        chsnletters = ", ".join(chosen_letters)
        hidletters = " ".join(hidden_letters)
        print(f"Letters chosen: {chsnletters}")
        print(f"{hidletters}\t lives: {lives} {'X'*lost}{'O'*(lives)}")
        # ask the user to guess a letter
        if copy_special_word == "".join(hidden_letters):
          print(f'Congratulations!!! You won! The word is {copy_special_word}!')
          break
        elif lives == 0:
          print(f"You lost! The word is {copy_special_word}!")
          break
        while True:
          try:
            letter = input("Please choose a new letter >\n").upper()
            if not letter.isalpha():
              raise ValueError
            elif len(letter) != 1:
              raise ValueError
            elif letter in chosen_letters:
              print("You have already chosen this letter.")
              continue
            elif letter not in chosen_letters:
              chosen_letters.append(letter)
            break
          except:
            pass
        # update the list of chosen letters

        # if the letter is correct update the hidden word,
        if letter in special_word:
          print("You guessed right!")
          for i in range(special_word.count(letter)):
            hidden_letters[special_word.find(letter)] = letter
            special_word = special_word[:special_word.find(letter)] + "0" + special_word[special_word.find(letter)+1:]
        else:
          lives -= 1
          lost +=1
          if lives == 0:
            continue
          else:
            print("You guessed wrong, you lost one life.")
            
      play_or_end = input("Would you like to play again [Y/N]?\n")
      if play_or_end.upper() == "Y":
        continue
      else:
        print('Goodbye!')
        break
        # else update the number of lives
        # and print interactive messages      
        
        # END GAME LOOP   (INNER PROGRAM LOOP)

        # check if the user guesses the word correctly or lost all lives,
        # if yes finish the game

    # END MAIN LOOP (OUTER PROGRAM LOOP)

    # ask if the user wants to continue playing, 
    # if yes start a new game, otherwise terminate the program

