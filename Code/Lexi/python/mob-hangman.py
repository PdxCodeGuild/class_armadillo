import random
import string

def load_words():
  with open('english.txt', 'r') as file: # reads file then closes it out
      words = file.read() # reads it
  split_words = words.split('\n') # splits the huge string into a list of words
  #returns it so it can run

  words_more_five = [] # list that we will append to form the for loop
  for word in split_words: #iterate
    if len(word) >= 5: # if this is true
      words_more_five.append(word) # append
  return words_more_five  # return obj

list_words = load_words()

play_word = random.choice(list_words) # generates a random list
play_word = "coding"
# print(list_words[:100]) # prints up to a 100 words

print(play_word)
underscore_word = play_word

# underscores = ['_','_','_','_','_','_','_',...]
underscores = ['_'] * len(play_word)
#underscores = " ".join() #know the syntax delimiter, then join
#returns giant string of chars
#print(underscores)
turns = 0 # starts us at 0
max_turns = int(len(play_word) * 1.75) # how many guesses - so if word is 10 characters, mult that by 1.75
print(max_turns)
guesses = [] #list to append user's letter guess to

while turns <= max_turns:

    print(f"you've guessed {turns} times, you have {10 - turns} left")
    print(f"here are the letters you've guessed: {' '.join(guesses)}\n") #print statements for game
    print(f"Here is the word to guess: {underscores}\n")

    # get a letter from the user
    guessed_letter = input("Enter a letter: ").lower()
    if guessed_letter not in string.ascii_lowercase:
      print("i don't get that ")
      continue

    # check if the user has already guessed that letter
    if guessed_letter in guesses:
      print("you already guessed that ")
      continue


    # check if the input from the user is actually a letter
    guesses.append(guessed_letter)

    # check if the letter is in the chosen word
    if guessed_letter in play_word:
      #if it is, replace the _'s in underscores with that letter
      for i in range(len(play_word)):
        if play_word[i] == guessed_letter:
          underscores[i] = guessed_letter
    else: #if the letter is not in the chosen word
      #increment turns
      turns += 1
      #check if the user lost, if so, exit the loop
      if turns == max_turns:
          print(f"you ran out of guesses, the word was {play_word}")
          break
      print('letter not found')

    #check if we won
    if "_" not in underscores:
      print(f"the word was {play_word}")
      print("YOU WON!")
    break


#underscores = '_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _'
# 0 1 2 3 4 5 6 7
# d r e a d f u l
# _ _ _ _ _ _ _ _


