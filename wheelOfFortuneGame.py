phrases = ["hello world","python programming","wheel of fortune"]

import random
#choose a random phrase
phrase = random.choice(phrases)
phrase_letters = set(phrase)
alphabet = set("abcdefghijklmnopqrstuvwxyz")
phrase_guessed = set()
incorrect_guesses = set(phrase)

#the amount of money the player has
money = 0

#a function to print the current game state
def print_game_state():
      print("phrases:",end="")
      for letter in phrase:
            if letter in phrase_guessed:
                  print(letter,end="")
            else:
                  print("_",end="")
      print("")
# the main game
while True:
      #print the current game state
      print_game_state()
      print("Icorrect Guesses",end="")
      for letter in incorrect_guesses:
            print(letter,end="")
      print("")
      
      #Get the player next guessed
      guess = input("Guessed a letter or phrase: ").lower()
      #check if the input is a letter or phrase
      if len(guess)==1:
            if guess not in alphabet:
                  print("Invalid input. Try again.")
                  continue
            #check if the guess is correct
            if guess in phrase_letters:
                  phrase_guessed.add(guess)
                  if phrase_guessed==phrase_letters:
                        print("You win! The phrase was "+phrase)
                        break
            else:
                  incorrect_guesses.add(guess)
                  if len(incorrect_guesses)==6:
                        print("You lose! The phrase was "+phrase)
                        break
      else:
            #check if the guess is correct
            if guess==phrase:
                  print("You win! The phrase was "+phrase)
                  break
            else:
                  incorrect_guesses.add(guess)
                  if len(incorrect_guesses)==6:
                        print("You lose! The phrase was "+phrase)
                        break
                      
                      
                

              