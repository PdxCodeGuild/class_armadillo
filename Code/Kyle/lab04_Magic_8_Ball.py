# required imports and lists utilized in this program
magic_8_ball_responses = ["'It is certain.'", "'It is decidedly so'", "'Without a doubt.'", "'Yes, definitely'", "'You may rely on it'", "'As I see it, yes'", "'Most likely'", "'Outlook - good'", "'Yes'", "'Signs point to yes'", "'Reply hazy...try again'", "'Ask again later'", "'Better not tell you now'", "'Cannot predict now'", "'Concentrate and ask again'", "'Don't count on it'", "'My reply is no'", "'My sources say no'", "'Outlook...not so good'", "'Very doubtful'"]
import random
import time
affirmatives = ['yes', 'y', 'sure', 'okay', 'fine', 'why not?']
negatives = ['no', 'n', 'nope', 'negative', 'definitely not', 'no way']
time_int = 0

# the intro when you ask the first question. 
def ask_the_magic_8_ball_intro():
  print("You hold in your hands a mysterious artifact. The Famed Magic 8-Ball!")
  time.sleep(time_int)
  print("Ask the Magic 8-Ball whatever truth the mind requires. ")
  time.sleep(time_int)

# the fuction to ask the 8 Ball a question.
def ask_the_magic_8_ball():
  question = input("Please type your question: ")
  print("The Magic 8-Ball starts to glow.")
  time.sleep(time_int)
  print("You begin to see an answer slowly appear.")
  time.sleep(time_int)
  print("It says: ")
  time.sleep(time_int)
  print("...")
  time.sleep(time_int)       
  print(random.choice(magic_8_ball_responses))
  print("")
  
# Welcome text for the user to begin the game.
print("Welcome to Lab 4. May the odds be ever in your favor!")
time.sleep(time_int)
ask_the_magic_8_ball_intro()

# Asks the user if they want to play the game. If yes, runs the program. If not, thanks the user for their time.
magic_8_ball = True

while True:
  play_game = input("Would you like to play this game? ")
  if play_game.lower() in affirmatives:
    ask_the_magic_8_ball()
    break
  elif play_game.lower() in negatives: #attempt to solicit a player to play
    incredulous = input("Really? But it's a Magic 8-Ball. mAgIcAl. MA-GIC. Are you sure you don't want to play? ")
    if incredulous.lower() in affirmatives:
      print("I'm sorry to hear that. Goodbye.")
      magic_8_ball = False
      continue
    elif incredulous.lower() in negatives: # double negative. Force the hand!
      print("See!! I knew you'd come around!! ")
      ask_the_magic_8_ball()
      break
    else:
      print("I'm sorry, I don't understand that response. Please answer again. ") 
  else:
    print("I'm sorry, I don't understand that response. Please answer again. ") 

#magic_8_ball = True
while True:
  play_again = input("Would you like to play again? ")
  if play_again.lower() in affirmatives:
    ask_the_magic_8_ball()
  elif play_again.lower() in negatives:
    print("That is unfortunate, but I appreciate you running this program. Goodbye.")
    magic_8_ball = False
    #follow_up = False
    break
  else:
    print("I'm sorry, I don't understand that response. Please answer again. ")
