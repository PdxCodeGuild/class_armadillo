
import random

welcome_screen = input("Are you feeling lucky?")

possible_random_questions = ["without a doubt", "ask again later", "not likely", 
"do you like to suffer", "sooner rather than later", "not this year", 
"I thought you enjoyed being on lockdown"]

user = input("Will the quarantine be lifted soon? ")

random.choice(possible_random_questions)

print(random.choice)

for x in possible_random_questions:
  print(x) 
  if x == "without a doubt":
      break